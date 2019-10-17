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
aux=0
Nodes_ord=[]
for Node in tp:
    L=len(tp[Node])
    if L>=aux:
        
