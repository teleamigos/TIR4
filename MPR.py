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

    def Busca_MPRs(self,my_address):
        aux=0
        i=0
        c=0
        lista=[]
        vecinos=[]
        for Node in self.tp:
            if Node !='0':
                L=len(self.tp[Node])
                lista.append((Node,L))
        for nodo in lista:
            #print(nodo)
            c=0
            if nodo[0]!=my_address:
                if nodo[1]>=1:
                    if len(vecinos)==0:
                        vecinos.append(self.tp[nodo[0]])
                        self.MPR.append(nodo[0])
                    else:
                        for v in self.tp[nodo[0]]:
                            if v in vecinos[0]:
                                pass
                            else :
                                vecinos[0].append(v)
                                c+=1
                        if c>1:
                            self.MPR.append(nodo[0])
            """print(vecinos)"""
