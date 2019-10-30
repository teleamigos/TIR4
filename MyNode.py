"""-----------------------------------------------------------------------------
------------------------------Clase mi nodo-------------------------------------
1.- Inicia el nodo
2.- Tiene informacion del nodo
3.- Calcula MPR
-----------------------------------------------------------------------------"""

class MyNode:
    def __init__(self):
        self.my_address='127.0.0.1'
        self.Neighbor=[]
        self.MPR=[]
        self.tp=dict()
        self.c=0
    def CreaTopologia(self,Nodo):
        self.tp[Nodo[0]]=Nodo[1]
    def AgregaVecino(self,Vecino):
        if Vecino in self.Neighbor:
            print("Ya conocido")
            self.c+=1
        else:
            self.Neighbor.append(Vecino)
        print(self.Neighbor)
