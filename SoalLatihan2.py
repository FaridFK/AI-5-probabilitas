# -*- coding: utf-8 -*-
"""
Created on Thu Oct 28 18:13:04 2021

@author: Farid
"""

# stats.py
from math import erf,sqrt

# define constants
#A = tempat untuk membangun pemancar 
PQ1 = 0.4 #peluang pemancar dibangun di tengah kota
PQ2 = 0.3 #peluang pemancar dibangun di kaki bukit 
PQ3 = 0.5 #peluang pemancar dibangun di tepi pantai 
PAQ1 = 0.03 #peluang gangguan sinyal pemancar dibangun di tengah kota
PAQ2 = 0.05 #peluang gangguan sinyal pemancar dibangun di kaki bukit 
PAQ3 = 0.08 #peluang gangguan sinyal pemancar dibangun di tepi pantai 

#Calculating probability Berapakah probabilitas terjadinya gangguan sinyal ?
print(f'PQ1 = 0.4')
print(f'PQ2 = 0.3')
print(f'PQ3 = 0.5')
print(f'PAQ1 = 0.03')
print(f'PAQ2 = 0.05')
print(f'PAQ3 = 0.08\n')
print(f'Probabilitas terjadinya gangguan sinyal')
print(f'P(A)={(PQ1*PAQ1) + (PQ2*PAQ2) + (PQ3*PAQ3)}\n')
print(f'Probabilitas telah terbangun pemancar di kaki bukit ')
print(f'P(A)={((PQ2*PAQ2))/((PQ1*PAQ1) + (PQ2*PAQ2) + (PQ3*PAQ3))}\n')
