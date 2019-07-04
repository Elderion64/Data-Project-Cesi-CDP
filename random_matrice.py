# -*- coding: utf-8 -*-
"For generated our dataset"
import numpy as np
from faker import Faker

np.random.seed(10)
rand = np.random.randint(1,100)


class MatRoad :
    citiesR = 100
    matrice = np.random.randint(10,50,size=(citiesR,citiesR))
    matrice_symm = (matrice + matrice.T)/2
    np.fill_diagonal(matrice_symm,0)


class Cities :
    citiesR = 100
    fake = Faker()
    cities_list = []
    i = 0
    fake.seed(10)
    
    while i < citiesR :
        city = fake.city();
        cities_list.append(city);
        i += 1
