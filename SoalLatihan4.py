# -*- coding: utf-8 -*-
"""
Created on Thu Oct 28 18:19:14 2021

@author: Farid
"""

print("""Diketahui dari 500 mahasiwa yang mengikuti makul : 
      - Matematika = 329
      - Satatistika = 186
      - Fisika = 295
      - Matematika dan Statistika = 83 
      - Matematika dan Fisik = 217
      - Statistika dan Fisika = 63 \n""")
print("""Misalkan :
      - Seluruh Mahasiswa = A
      - Mahasiswa yang mengikuti ketiga mata kuliah = n
      - Matematika = M
      - Fisika = F
      - Statistika = S
      - Matematika dan Statistika = M_S
      - Matematika dan Fisika = M_F
      - Statistika dan Fisika = F_S
      - Matematika dan Statistika = M_S
      - Anggota Himpunan Matematika = X_M
      - Anggota Himpunan Statistika = X_S
      - Anggota Himpunan Fisika = X_F \n""") 
      
A = 500
M = 329
S = 186
F = 295
n = 0 
M_F = 217 - n
M_S = 83 - n
F_S = 63 - n
X_M = 29 + n
X_F = 15 + n
X_S = 40 + n

print("""X_M = M - (M_F - n) - (M_S - n) - n
      X_F = F - (F_S - n) - (M_F - n) - n
      X_S = S - (F_S - n) - (M_S - n) - n \n""")
print("""Maka :
      - X_M = 329 - (217 - n) - (83 - n) - X = 29 + n
      - X_F = 295 - (63 - n) - (217 - n) - X = 15 + n
      - X_S = 186 - (63 - n) - (83 - n) - X = 40 + n \n""")
      
# soal a
n = A - (M_F + M_S + F_S + X_M + X_S + X_F)
print("soal a : \n Mahasiswa yang mengikuti ketiga mata kuliah = n \n n = A - (M_F + M_S + F_S + X_M + X_S + X_F) =", n, "\n")
M_F = 217 - n
M_S = 83 - n
F_S = 63 - n
X_M = 29 + n
X_F = 15 + n
X_S = 40 + n

#soal b
M_NotF = X_M + M_S
print("soal b : \n Matematika tetapi tidak fisika = M_NotF \n M_NotF = X_M + M_S =", M_NotF, "\n")

#soal c 
S_NotM = X_S + F_S
print("soal c : \n Statistika tetapi tidak matematika = S_NotM \n S_NotM = X_S + F_S =", S_NotM, "\n")

#soal d
F_NotS = X_F + M_F
print("soal d : \n Fisika tetapi tidak Statistika = F_NotS \n F_NotS = X_F + M_F =", F_NotS, "\n")

#soal e
MF_NotS = X_M + 217 - n + X_F
print("soal e : \n Matematika atau Fisika tetapi tidak Statistika = MF_NotS  \n MF_NotS = X_M + X_F + (217 - n) =", MF_NotS, "\n")

#soal f
M_NotSF = 29 + n
print("soal f : \n Matematika tetapi tidak Statistika atau Fisika = M_NotSF  \n M_NotSF = 29 + n =", M_NotSF, "\n")
