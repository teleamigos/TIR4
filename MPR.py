"""-----------------------------------------------------------------------------
---------------------------------MPR-----------------------------------------"""

file=open('Nodes.txt','r')
d=dict()
lines=file.readlines()
for line in lines:
    line=line.split('\n')[0]
    Nodes=line.split(';')[0]
    line=line[2:]
    Neighbor=line.split(',')
    d[Nodes]=Neighbor
n_ord=[]
for n in d['2']:
    N_v=len(d[n])
    n_ord.append((n,N_v))
aux=0
n_ord_aux=[]
for n in n_ord:
    if n[1]>aux:
        n_ord_aux.append(n)
        aux=n[1]
