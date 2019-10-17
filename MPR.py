"""-----------------------------------------------------------------------------
---------------------------------MPR-----------------------------------------"""

import csv
Neighbors=[]
tp=dict()
with open('Nodes.csv', newline='') as File:
    reader = csv.reader(File)
    for row in reader:
        Node=row[0]
        row=row[1:]
        #Neighbors.clear()
        for column in row:
            if column!='':
                Neighbors.append(column)
        tp[Node]=Neighbors
        Neighbors=[]
    File.close()
"""-----------------------------------------------------------------------------
1- ESCOGER EL VECINO CON MAYOR NO. DE VECINOS
2- SI LOS VECINOS TIENEN EL MISMO NO. DE VECINOS, SE ESCOGE AL MENOS ESCOGIDO
3.-SI HAN SIDO ESCOGIDOS EL MISMO NO. DE VECES, ESCOGE AL SEGUNDO MAYOR
-----------------------------------------------------------------------------"""
aux=0
Nodes_ord=[]
for Node in tp:
    for Neighbor in tp[Node]:
            L=len(tp[Neighbor])
            if L>=aux:
                MPR=(Node,Neighbor)
                aux=L
    print("Nodo : {} MPR : {} ".format(MPR[0],MPR[1]))
    MPR=('','')
    aux=0
