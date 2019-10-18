"""-----------------------------------------------------------------------------
*******************************MPR**********************************************
1.- Escoge el de mayor No. de aristas
-----------------------------------------------------------------------------"""
class MPR:
    def __init__(self,tp):
        self.tp=dict()
        self.tp=tp

    def Busca_MPRs(self):
        aux=0
        for Node in self.tp:
            for Neighbor in self.tp[Node]:
                    L=len(self.tp[Neighbor])
                    if L>=aux:
                        MPR=(Node,Neighbor)
                        aux=L
            print("Nodo : {} MPR : {} ".format(MPR[0],MPR[1]))
            MPR=('','')
            aux=0
