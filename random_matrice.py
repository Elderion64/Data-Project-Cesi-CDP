# -*- coding: utf-8 -*-
"Pour pouvoir générer notre dataset des villes aléatoire"
import numpy as np
from faker import Faker
"import matplotlib.pyplot as plt"


"Le seed va nous permettre de recréer la même situation si on la rappelle"
np.random.seed(1)
rand = np.random.randint(1,1000)
"""
print(rand)
print("")
"""

class MatRoad :
    "randint c'est un random d'entier et matrice.T est l'inverse de la matrice"
    matrice = np.random.randint(50,100,size=(rand,rand))
    matrice_symm = (matrice + matrice.T)/2
    np.fill_diagonal(matrice_symm,0)
    """
    print (matrice_symm)
    print("")
    """

class MatEssence :
    matrice_essence = np.random.uniform(low=0.5,high=1.5,size=(rand,rand))
    matrice_essence_symm = (matrice_essence + matrice_essence.T)/2
    np.fill_diagonal(matrice_essence_symm,0)
    matrice_essence_symm = matrice_essence_symm.round(decimals=1)
    """
    print (matrice_essence_symm)
    print("")
    """

class Cities :
    fake = Faker()
    cities_list = []
    i = 0
    fake.seed(1)
    
    while i < rand :
        city = fake.city();
        cities_list.append(city);
        i += 1
    """
    print(cities_list)
    """


"""
plt.plot(matrice_symm)
plt.show
"""