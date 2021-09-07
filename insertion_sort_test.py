#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep  3 17:41:00 2021

@author: dennisblaufuss
"""

import random as rd
from time import perf_counter_ns

A = list(range(0,1000))
rd.shuffle(A)

B = list(range(0,2000))
rd.shuffle(B)

C = list(range(0,3000))
rd.shuffle(C)

D = list(range(0,4000))
rd.shuffle(D)

E = list(range(0,5000))
rd.shuffle(E)

F = list(range(0,6000))
rd.shuffle(F)

G = list(range(0,7000))
rd.shuffle(G)

H = list(range(0,8000))
rd.shuffle(H)


inp = [A,B,C,D,E,F,G,H]

output = []        
      
def insertion (inputs):
    timestart = perf_counter_ns()
    j = 1
    while j < len(inputs):
        key = inputs[j]
        i = j - 1
        while i > -1 and inputs[i] > key:
            inputs[i + 1] = inputs[i]
            i = i - 1
        inputs[i + 1] = key
        j = j + 1
    timeend = perf_counter_ns()
    timespan = timeend - timestart
    return timespan
        
def ins_list (inpu):
    k = 0
    n = len(inpu)
    while k < n:
        timespan= insertion(inpu[k])
        output.append(timespan)
        k += 1 
        
ins_list(inp)   

