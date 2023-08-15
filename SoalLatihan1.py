# -*- coding: utf-8 -*-
"""
Created on Thu Oct 28 17:19:50 2021

@author: Farid
"""

#stats.py
from math import erf, sqrt

#define constants
H1 = 0.25 #Peluang Bisul tanpa gejala
H2 = 0.15 #Peluang Campak tanpa gejala
H3 = 0.25 #Peluang Panu tanpa gejala
H4 = 0.25 #Peluang Kutil tanpa gejala
H5 = 0.10 #Peluang Cacar tanpa gejala
H1G = 0.33 #peluang Bisul gejala gatal-gatal
H2G = 0.34 #peluang Campak gejala gatal-gatal
H3G = 0.33 #peluang Panu gejala gatal-gatal
H2D = 0.8 #peluang Campak gejala demam
H5D = 0.2  #peluang Cacar gejala demam
H1R = 0.75 #peluang Bisul gejala peradangan folikuler kecil & merah membesar
H2R = 0.1 #peluang Campak gejala peradangan folikuler kecil & merah membesar
H5R = 0.15 #peluang Cacar gejala peradangan folikuler kecil & merah membesar

#Penyakit yang diderita orang berdasarkan gejala gatal-gatal dan demam
print(f'Gejala Gatal-gatal\n')
#Probabilitas gatal-gatal Bisul
prob = (H1G*H1)/((H1G*H1)+(H2G*H2)+(H3G*H3))
print(f'Probabilitas gatal-gatal Bisul')
print(f'P(H|E) = {(H1G*H1)/((H1G*H1)+(H2G*H2)+(H3G*H3))} \n')

#Probabilitas gatal-gatal Campak
prob1 = (H2G*H2)/((H1G*H1)+(H2G*H2)+(H3G*H3))
print(f'Probabilitas gatal-gatal Campak')
print(f'P(H|E) = {(H2G*H2)/((H1G*H1)+(H2G*H2)+(H3G*H3))}\n')

#Probabilitas gatal-gatal Panu
prob2 = (H3G*H3)/((H1G*H1)+(H2G*H2)+(H3G*H3))
print(f'Probabilitas gatal-gatal Panu')
print(f'P(H|E) = {(H3G*H3)/((H1G*H1)+(H2G*H2)+(H3G*H3))}\n\n')
print(f'Gejala Demam\n')

#Probabilitas demam Campak 
prob3 = (H2D*H2)/((H2D*H2)+(H5D*H5))
print(f'Probabilitas demam Campak')
print(f'P(H|E) = {(H2D*H2)/((H2D*H2)+(H5D*H5))}\n')

#Probabilitas demam Cacar 
prob4 = (H5D*H5)/((H2D*H2)+(H5D*H5))
print(f'Probabilitas demam Cacar')
print(f'P(H|E) = {(H5D*H5)/((H2D*H2)+(H5D*H5))}\n\n')
print(f'Diagnosa berdasarkan gejala gatal-gatal dan demam\n') 

#Probabilitas terkena Penyakit Campak 
prob5 = ((H2G*H2)/((H1G*H1)+(H2G*H2)+(H3G*H3))) + ((H2D*H2)/((H2D*H2)+(H5D*H5)))
print(f'Probabilitas Penyakit Campak')
print(f'P(H|E) = {((H2G*H2)/((H1G*H1)+(H2G*H2)+(H3G*H3))) + ((H2D*H2)/((H2D*H2)+(H5D*H5)))}\n\n')
print(f'Diagnosa berdasarkan gejala peradangan folikuler kecil & merah yang membesar\n')

#Penyakit yang diderita oleh orang berdasarkan gejala peradangan folikuler kecil & merah yang membesar
prob6 = (H1R*H1)/((H1R*H1)+(H2R*H2)+(H5R*H5))
print(f'Probabilitas Penyakit Bisul')
print(f'P(H|E) = {(H1R*H1)/((H1R*H1)+(H2R*H2)+(H5R*H5))}')
