# -*- coding: utf-8 -*-
"""
Created on Tue Jul  2 13:29:20 2019
@author: antoi
"""
import numpy as np
from random_matrice import MatRoad


i = 0
nbrColumnMatRoad = len (MatRoad.matrice_symm)
nbrMatRoad = nbrColumnMatRoad - 1
     
class GenerateListMatRoad :
    toListMatRoad = []

    while (nbrMatRoad > 0) :
        arrayMatRoad = [MatRoad.matrice_symm[i,:]]   
        
        arrayToListMatRoad= arrayMatRoad[-1]
        arrayToListMatRoad = np.ndarray.tolist(arrayToListMatRoad)

        testMatRoad = arrayToListMatRoad[-nbrMatRoad:]
        
        toListMatRoad.extend(testMatRoad)   
           
        i += 1
        nbrMatRoad -= 1
        
    "print (toListMatRoad)"

