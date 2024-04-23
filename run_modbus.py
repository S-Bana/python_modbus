# === load packages ============================================
import os
from pymodbus.client import ModbusUdpClient
from pymodbus.payload import BinaryPayloadDecoder
from pymodbus.constants import Endian
from pymodbus.transaction import ModbusRtuFramer as ModbusFramer
import time
import pandas as pd
from datetime import datetime
from multiprocessing import Pool
from dotenv import load_dotenv
import ast

# === load data ============================================
load_dotenv()
dict_ip_address_str = os.getenv("dict_ip_address")
dict_usual_parameters_str = os.getenv("dict_usual_parameters")

dict_ip_address = ast.literal_eval(dict_ip_address_str)
dict_usual_parameters = ast.literal_eval(dict_usual_parameters_str)

ports = [5011,5012]

list_ip = list(dict_ip_address.values())
list_column = list(dict_usual_parameters.keys())
list_address = list(dict_usual_parameters.values())

# print("*"*50)
# print(list_ip)
# print("*"*50)
# print(list_column)
# print("*"*50)
# print(list_address)

# === ip check +=============================================
def check_ip(in_ip):
    response = os.popen(f"ping -c 1 -W 0.1 {in_ip}").read()
    return "100% packet loss" not in response

# === make task =============================================
tasks = [(ip, port, list_address, list_column) for ip in list_ip for port in ports]
'''
This command make a list of 
[
    ip[0],port[0],[list_reg],[list_column],
    ip[0],port[1],[list_reg],[list_column],
    ip[1],port[0],[list_reg],[list_column],
    ip[1],port[1],[list_reg],[list_column],
]
'''
z = tasks[1]
# print(z)

# print(z)

# === make conection to mudbus ================================
def initialize_udp_client(ip, port):
    return ModbusUdpClient(ip, port=port, framer=ModbusFramer,timeout=0.1)

# === read and decode register ================================
def read_and_decode_registers(client, address, count, slave):
    try:
        result = client.read_holding_registers(address=address, count=count, slave=slave)
        if not result.isError():
            decoder = BinaryPayloadDecoder.fromRegisters(result.registers,
                                                         byteorder=Endian.BIG,
                                                         wordorder=Endian.LITTLE)
            return decoder.decode_16bit_int()
    except Exception as e:
        print(f"Error reading data: {e}")
    return None

# === send register to device =================================
def process_ip_port(ip_port_tuple):
    ip_i, port_p, list_address, list_column = ip_port_tuple
    start_time = datetime.now()

    if check_ip(ip_i):
        client = initialize_udp_client(ip_i, port_p)
        
        new_row = []
        for reg_a in list_address:
            data = read_and_decode_registers(client, reg_a, count=1, slave=12)  # Assuming count=1 and slave=12 are constants
            if data is not None:
                new_row.append(int(data))
            else:
                break  # Stop processing this IP if any read fails

        if len(new_row) == len(list_address):
            print("ok")
        
        # close connection mudbus
        client.close()

        # calclute run time process
        end_time = datetime.now()

        # return result and time spend
        return f"Processed {ip_i}:{port_p}, Duration: {end_time - start_time}"
    else:
        return f"Error {ip_i}:{port_p} not found"

# === main method =============================================
# a conditional statement for run main method
if __name__ == "__main__":
    while True:
        # main()
        # print(check_ip(z[0]))
        # print('*'*50)
        # print(initialize_udp_client(ip=z[0],port=z[1]))
        # print('*'*50)
        # print(print(process_ip_port(tasks[0])))
        print('*'*50)

        break