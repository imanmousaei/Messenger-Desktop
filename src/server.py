import socket
from consts import number_of_clients

# AF_INET6 : ipv6 , SOCK_STREAM : TCP , SOCK_DGRAM : UDP
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

ip_port = ('localhost', 8500)

server.bind(ip_port)

server.listen(number_of_clients)

connection, address = server.accept()

connection.send('[SERVER] hello there')
