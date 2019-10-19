"""-----------------------------------------------------------------------------
*******************************MPR**********************************************
1.- Escoge el de mayor No. de aristas
-----------------------------------------------------------------------------"""
class MPR:
    def __init__(self,tp):
        self.tp=dict()
        self.tp=tp
        self.MPR_tabla=[]
        self.MPR=[]

    def Busca_MPRs(self):
        aux=0
        i=0
        c=0
        for Node in self.tp:
            for Neighbor in self.tp[Node]:
                    L=len(self.tp[Neighbor])
                    if L>=aux:
                        MPR_nodo=(Node,Neighbor)
                        aux=L
            self.MPR_tabla.append(MPR_nodo)
            print('Node : {} \t-------> MPR : {}'.format(self.MPR_tabla[i][0],self.MPR_tabla[i][1]))
            MPR=('','')
            aux=0
            i+=1
