import socket 
import time 
from struct import *

server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)
server.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)

server.settimeout(0.2)
server.bind(("", 44444))
message  = pack('H',4)
while True:
	server.sendto(message, ('<broadcast>', 37020))
	print("Mensaje enviado")
	time.sleep(1)