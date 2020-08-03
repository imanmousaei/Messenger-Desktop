import socket

from consts import *

# AF_INET6 : ipv6 , SOCK_STREAM : TCP , SOCK_DGRAM : UDP
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server_socket.bind(ip_port)

server_socket.listen(number_of_clients)

connection, address = server_socket.accept()

s = '[SERVER] Hello there'
connection.send(s.encode())
