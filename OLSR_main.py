"""-----------------------------------------------------------------------------
------------------------------Main----------------------------------------------
1.-  Declaracion de variables.
2.-  Establecer conexion.
3.-  Crear Mensaje Hello.
4.-  Enviar mensaje Hello.
--------------------------------------------------------------------------------
                                Desarrollo:

1.- Inicializa variables, clase OLSR y el socket UDP.
2.- Si el contador es 0, se abre un hilo para enviar el primer mensaje de Hello.
    *Se envia la direccion del nodo actual
    *Se envia en broadcast
    *Las direcciones de vecinos es un campo vacio.
    *Willingness esta por default en este caso.
3.- Se recibe la informacion (mensaje de Hello de cualquier nodo vecino que fue
    enviada por broadcast).
    *Desempaqueta el mensaje.
    * Guarda la direccion del que la envio Hello
    * Guarda los vecinos conocidos del que manda Hello
4.- Si transcurre un tiempo predeterminado, deja de recibir hello para conocer
    vecinos.
5.- Envia un Hello con la lista de vecinos conocidos en ese nodo a todos sus
    Vecinos por un intervalor de x segundos.En el mensaje Hello se incluye:
    * Direccion del nodo que envia el mensaje Hello.
    * Direciones de cada vecino.
6.- La recepcion de los vecinos de nuestro vecino se hace por un cierto tiempo.
    *La informacion se guarda en listas y cuando termine el tiempo de recibir,
     se toma la mas acutal y se forma la topologia de la red.
7.- Con la informacion colectada de los vecinos se calcula el MPR por cada nodo.
8.- Enviamos mensaje de TC nuestros vecinos.
-----------------------------------------------------------------------------"""
from Message_Hello import *
from OLSR import *
from MyNode import*
import socket
import time
from threading import Thread
from Threads_send import*

sock=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
IP='192.168.100.14'
PORT=5005
olsr=OLSR()
Yo=MyNode()
"""

Hello=olsr.Empaquetado('Hello',[''],'WILL_DEFAULT')#Primer Mensaje es Hello por default.
#Enviar por un sokcet
print(type(Hello))
sock.sendto(Hello,(IP,PORT))"""
#sock.bind((IP,PORT))
c=0
i=0
while i<20:
    if c==0:
        Thread1=Thread(target=Send_Hello,args=(olsr,['127.0.1.1','132.248.120.131'],'WILL_DEFAULT'))
        Thread1.start()
        Thread1.join()
        c+=1
    """
    msj,addr=sock.recvfrom(1024)
    Nodo,Neighbors=olsr.Desempaquetado(msj)
    Yo.AgregaVecino(Nodo)
    """
    sleep.time(1)
    i+=0
