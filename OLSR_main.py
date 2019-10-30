"""-----------------------------------------------------------------------------
------------------------------Main----------------------------------------------
1.-  Declaracion de variables.
2.-  Establecer conexion.
3.-  Crear Mensaje Hello.
4.-  Enviar mensaje Hello.
-----------------------------------------------------------------------------"""
from Message_Hello import *
from OLSR import *
#from socket import socket, AF_PACKET, SOCK_RAW, htons
import time
from threading import Thread

#s=socket(AF_PACKET,SOCK_RAW,htons(0x0801))
direcciones=['127.0.0.1','132.248.120.131']
OLSRs=OLSR()
OLSRs.Empaquetado('Hello',direcciones)
