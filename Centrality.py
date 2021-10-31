#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 10 21:37:59 2021

@author: gopal
"""

import csv
import os
import numpy as np

#os.chdir('/Users/gopal/OneDrive/Sep-2019 onwards/Quota optimization/RemoteLocationsCentrality')
file_tickets=open('12951_tickets.csv')
csvreader= csv.reader(file_tickets)

tt = {'MMCT':0,'BVI':30, 'ST':263, 'BRC':392, 'RTM':653, 'NAD':695, 'KOTA':920, 'NDLS':1384}
Demand = np.zeros((8,8))
stns = list(tt.keys())
rows=[]
i=0
for row in csvreader:
    rows.append(row)

for i in range(1,len(rows)):
    row = rows[i]
    r= stns.index(row[1])
    c= stns.index(row[2])
    Demand[r,c]=float(row[4])+float(row[5])   

#compute centrality
centrality={}
outdegree ={}
indegree={}
num_stops =len(stns)
for i in range(num_stops):
    weight = tt[stns[i]]/tt[stns[num_stops-1]]
    outd = sum(Demand[i,:]) 
    ind= sum(Demand[:,i])
    outdegree[stns[i]] = outd 
    indegree[stns[i]] = ind
    centrality[stns[i]]= round((1-weight) * outd + weight * ind,1)

print(centrality)