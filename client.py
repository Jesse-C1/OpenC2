import socket
import json

HOST = "10.10.94.118"
#HOST = "127.0.0.1" #local
PORT = 1433

data = None 
with open("createBucket.json") as file:
    tempdata = json.load(file)
    data = tempdata
data = json.dumps(data)

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    s.sendall(bytes(data,encoding = "utf-8"))


    