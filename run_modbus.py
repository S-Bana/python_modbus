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

# print("*"*50)
# print(dict_ip_address)
# print("*"*50)
# print(dict_usual_parameters)

# === 
