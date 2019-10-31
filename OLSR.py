"""-----------------------------------------------------------------------------
-------------------------------OLSR clase---------------------------------------
1.- Inicializacion
2.- Empaquetado
3.- Desempaquetado
--------------------------------------------------------------------------------
                            Estructura del paquete

1.- Longitud del paquete :16 bits
2.- Numero de secuencia del paquete-16 bits
3.- Typo de Mensaje- 8 bits
4.- Vtime -8 bits(por cuanto tiempo despues de llegado al nodo se toma la informacion)
5.- Tamaño de mensaje 16 bits
6.- Originador de Direccion -32 bits Contiene la direccion de cada nodo,NO ES IP
7.- Tiempo de vida -8 bits El numero de saltos que puede tener
8.- Cuenta de saltos -8 bits
9.- Numero de secuencia de Mensaje
10.- Mensaje
-----------------------------------------------------------------------------"""
import struct
from Message_Hello import*
from Message_TC import*

class OLSR(Message_Hello,Message_TC):
    def __init__(self,IP):
        self.Len_pq=0
        self.PSN=0
        self.TypeM={
        'Hello':127,
        'TC':0
        }
        self.Vtime=2
        self.Len_msj=0
        self.OAdd=IP
        self.TtoL=0
        self.HopC=0
        self.MSN=0
        self.MHello=Message_Hello()
        self.MTC=Message_TC()
    def Empaquetado(self,Message_type,direcciones,Willingness,LC):
        # Dependiendo el tipo de mensaje se manda a llamar a la funcion
        #Empacadora de mensaje Hello o Tc y regresa el mensaje empaquetado para
        # ser sumado al paquete ya hecho
        if Message_type=='Hello':
            msj=self.MHello.Genera(Willingness,direcciones,LC)
            self.TtoL=1
        elif Message_type=='TC':
            msj=self.MTC.Genera(direcciones)
            self.TtoL=4
        else:
            print("Error")
        self.Len_pq=len(msj)
        paquete=pack('!HHBB',self.Len_pq,self.PSN,self.TypeM[Message_type],self.Vtime)
        self.Len_msj=8+len(msj)
        paquete+=pack('!H',self.Len_msj)+self.OAdd.encode('utf-8')
        paquete+=pack('!BBH',self.TtoL,self.HopC,self.MSN)+msj
        return paquete

    def Desempaquetado(self,msj):
        len_msj=unpack('!H',msj[:2])[0]
        len_pq=len(msj)
        msj_rcv=msj[len_pq-len_msj:]
        Neighbor_add=msj[8:len_pq-len_msj-4]
        Neighbor_add=Neighbor_add.decode('utf-8')
        type=unpack('!B',msj[4:5])[0]
        if type==self.TypeM['Hello']:
            neighbors_adds=self.MHello.Desempaqueta_Hello(msj_rcv)
        elif type==self.TypeM['TC']:
            neighbors_adds=self.MTC.Desempaqueta__TC(msj_rcv)
        return Neighbor_add,neighbors_adds
