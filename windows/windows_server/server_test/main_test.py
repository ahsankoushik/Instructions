import time
import socket
from threading import *

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# host = "65.109.54.50" #tanjim vaiya server
host = "20.213.60.76"  #koushik server


port = 11100
s.connect((host,port))

# Send data to server



supplier = 'HQ'
imei = '111111111111111'
command_code = 'V1'


data = f"*{supplier},{imei},{command_code},144936,A,2342.07924,N,09026.88400,E,1.73,272.65,251122,FFFFFFFF#"



s.send(data.encode())

 

# # Receive data from server

# dataFromServer = s.recv(1024)

 

# # Print to the console

# print(dataFromServer.decode())