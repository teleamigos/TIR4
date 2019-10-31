import time
from threading import Thread

def Send_Hello(s,IP,PORT,olsr,Vecinos,LC,Willingness):
    time.sleep(1)
    Hello=olsr.Empaquetado('Hello',Vecinos,Willingness,LC)
    s.sendto(Hello,('<broadcast>',37020))
    #print(Hello)
    #s.close()
def Send_TC(s,IP,PORT,olsr,MPRs,LC,Willingness):
    TC=olsr.Empaquetado('TC',MPRs,'No',0)
    s.sendto(TC,('<broadcast>',37020))

def Recibir(s,mi_nodo):
    time.sleep(1)
