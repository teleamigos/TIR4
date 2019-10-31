"""-----------------------------------------------------------------------------
------------------------------Clase mi nodo-------------------------------------
1.- Inicia el nodo
2.- Tiene informacion del nodo
3.- Calcula MPR
-----------------------------------------------------------------------------"""
from MPR import*
class MyNode(MPR):
    def __init__(self,IP):
        self.my_address=IP
        self.Neighbor=[]
        #self.MPR=False
        self.tp=dict()
        self.c=0
        self.SoyMPR={}
    def CreaTopologia(self,Nodo):
        self.tp[Nodo[0]]=Nodo[1]
    def AgregaVecino(self,Vecino):
        if Vecino in self.Neighbor:
            print("Ya conocido")
            self.c+=1
        else:
            if Vecino != self.my_address:
                self.Neighbor.append(Vecino)
    def Calcula_MPR(self):
        MPRs=MPR(self.tp)
        MPRs.Busca_MPRs(self.my_address)
        return MPRs.MPR
