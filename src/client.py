import socket
from consts import *

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client_socket.connect(ip_port)

received_data = client_socket.recv(1024)  # 1024 ta 1024 ta char migire az server

print(received_data.decode())