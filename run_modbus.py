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

print(z[0])

