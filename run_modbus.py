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



