import socket
import time
from threading import Thread

def Send_Hello(s,(IP,PORT),olsr,Vecinos,LC,Willingness):
    time.sleep(1)
    Hello=olsr.Empaquetado('Hello',Vecinos,Willingness,LC)
    print(Hello)
    s.send(Hello(IP,PORT))
