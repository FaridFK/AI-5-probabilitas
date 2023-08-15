# -*- coding: utf-8 -*-
"""
Created on Thu Oct 28 18:17:20 2021

@author: Farid
"""

#stats.py
from math import erf, sqrt

#define constants
A = 0.5 #kejadian terambilnya bola merah
C = 0.3 #kejadian terambilnya bola dikotak I,II,III
C1 = 1 # Probabilitas terambilnya bola merah dari kotak I
C2 = 0.5 #Probabilitas terambilnya bola merah dari kotak II
C3 = 0 #Probabilitas terambilnya bola merah dari kotak III

#Probabilitas terambilnya bola dikotak I 
prob = (C1*C)/A
print(f'Probabilitas terambilnya bola dikotak I')
print(f'P(C1/A) = {(C1*C)/A}\n')

#Probabilitas terambilnya bola dikotak II 
prob1 = (C2*C)/A
print(f'Probabilitas terambilnya bola dikotak II')
print(f'P(C2/A) = {(C2*C)/A}\n')

#Probabilitas terambilnya bola dikotak III
prob2 = (C3*C)/A
print(f'Probabilitas terambilnya bola dikotak III')
print(f'P(C3/A) = {(C3*C)/A}\n')

#Probabilitas bola terambil dari kotak I, II, dan III
prob3 = ((C1*C)/A) + ((C2*C)/A) + ((C3*C)/A)
print(f'Probabilitas terambilnya bola dikotak I, II, dan III')
print(f'P(A) = {((C1*C)/A) + ((C2*C)/A) + ((C3*C)/A)}\n')
