import socket
import time
from threading import Thread

def Send_Hello(olsr,Vecinos,Willingness):
    time.sleep(1)
    Hello=olsr.Empaquetado('Hello',Vecinos,Willingness)
    print(Hello)
    #s.send(Hello)
