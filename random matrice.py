# -*- coding: utf-8 -*-
"Pour pouvoir générer notre dataset des villes aléatoire"
import numpy as np
from faker import Faker

"import matplotlib.pyplot as plt"

"Le seed va nous permettre de recréer la même situation si on la rappelle"
np.random.seed(1)
rand = np.random.randint(1,1000)
print(rand)

"randint c'est un random d'entier et matrice.T est l'inverse de la matrice"
matrice = np.random.randint(0,50,size=(rand,rand))
matrice_symm = (matrice + matrice.T)
np.fill_diagonal(matrice_symm,0)
print (matrice_symm)

fake = Faker()
fake.city()

cities_list = []
i = 0

while i < rand :
    city = fake.city();
    cities_list.append(city);
    i = i+1
print(cities_list)



"""
plt.plot(matrice_symm)
plt.show
"""