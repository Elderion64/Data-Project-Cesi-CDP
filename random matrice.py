# -*- coding: utf-8 -*-
"Pour pouvoir générer notre dataset des villes aléatoire"
from random import seed
from random import randint
import numpy as np
"import matplotlib.pyplot as plt"

"Le seed va nous permettre de recréer la même situation si on la rappelle"
seed(1)
rand = randint(1,1000)
print(rand)

"randint c'est un random d'entier et matrice.T est l'inverse de la matrice"
matrice = np.random.randint(0,50,size=(rand,rand))
matrice_symm = (matrice + matrice.T)
np.fill_diagonal(matrice_symm,0)
print (matrice_symm)

"""
plt.plot(b_symm)
plt.show
"""