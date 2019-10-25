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
        lista=[]
        vecinos=[]
        for Node in self.tp:
            if Node !='0':
                L=len(self.tp[Node])
                lista.append((Node,L))
        total=0
        for l in lista:
            total +=l[1]
        i=0
        for nodo in lista:
            aux=self.tp[nodo[0]]
            c=0
            for n in aux:
                for node in self.tp:
                    if n!=node:
                        if n in self.tp[node]:
                            c+=1
            if c>(total/(len(lista)/5)):
                print("Este nodo es MPR",nodo)
                i+=1
        print("tamano",i)
        """self.MPR_tabla.append(MPR_nodo)
        print('Node : {} \t-------> MPR : {}'.format(self.MPR_tabla[i][0],self.MPR_tabla[i][1]))
        MPR=('','')
        aux=0
        i+=1"""
