import socket 

client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
client.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
client.bind(("",37020))
while True:
	data, adrr = client.recvfrom(1024)
	print("Mensaje recibido:  %s" %data)