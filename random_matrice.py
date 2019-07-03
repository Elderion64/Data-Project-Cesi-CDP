# -*- coding: utf-8 -*-
"Pour pouvoir générer notre dataset des villes aléatoire"
import numpy as np
"Penser à faire 'pip install Faker' pour installer faker"
from faker import Faker
"import matplotlib.pyplot as plt"


"Le seed va nous permettre de recréer la même situation si on la rappelle"
np.random.seed(9)
rand = np.random.randint(1,100)

"""
print(rand)
print("")
"""

class MatRoad :
    citiesR = rand
    "randint c'est un random d'entier et matrice.T est l'inverse de la matrice"
    matrice = np.random.randint(10,50,size=(citiesR,citiesR))
    matrice_symm = (matrice + matrice.T)/2
    np.fill_diagonal(matrice_symm,0)
    """
    print (matrice_symm)
    print("")
    """

class Cities :
    citiesR = rand
    fake = Faker()
    cities_list = []
    i = 0
    fake.seed(9)
    
    while i < citiesR :
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