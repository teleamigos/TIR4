"""-----------------------------------------------------------------------------
---------------------------------MPR-----------------------------------------"""

import csv
from MPR import*
Neighbors=[]
tp=dict()
"""---------------------------Lee archivo------------------------------------"""
with open('G122.csv', newline='') as File:
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
MPRs=MPR(tp)# Crea clase MPR
MPRs.Busca_MPRs()
