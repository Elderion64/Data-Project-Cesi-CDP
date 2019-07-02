# -*- coding: utf-8 -*-
"""
Created on Tue Jul  2 01:27:53 2019

@author: antoi
"""

# -*- coding: utf-8 -*-
"Pour pouvoir générer notre dataset des villes aléatoire"
from random import seed
from random import randint
import numpy as np
import matplotlib.pyplot as plt

"Le seed va nous permettre de recréer la même situation si on la rappelle"
seed(1)
rand = randint(1,1000)
print(rand)
"""
liste =[x for x in range(rand)]
print(liste)
"""

"randint c'est un random d'entier et matrice.T est l'inverse de la matrice"
matrice = np.random.randint(50,100,size=(rand,rand))
matrice_symm = (matrice + matrice.T)/2
np.fill_diagonal(matrice_symm,0)
print (matrice_symm)
print("test")


liste = [matrice_symm[0,:]]
print(liste)
rand2=rand - 1
print (rand2)
liste2= liste[-1]
print(liste2[-137:])


plt.plot(matrice_symm)
plt.show
