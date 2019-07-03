# -*- coding: utf-8 -*-
"""
Created on Tue Jul  2 13:29:20 2019
@author: antoi
"""
import numpy as np
from random_matrice import MatRoad,MatEssence
from faker import Faker


i = 0
nbrColumnMatRoad = len (MatRoad.matrice_symm)
nbrMatRoad = nbrColumnMatRoad - 1
toListMatRoad = []
     
class GenerateListMatRoad :

    while (nbrMatRoad > 0) :
        arrayMatRoad = [MatRoad.matrice_symm[i,:]]   
        
        arrayToListMatRoad= arrayMatRoad[-1]
        arrayToListMatRoad = np.ndarray.tolist(arrayToListMatRoad)
        "print (toList)"

        testMatRoad = arrayToListMatRoad[-nbrMatRoad:]
        "print (toList)"
        
        toListMatRoad.extend(testMatRoad)   
        "print (toList)"
           
        i += 1
        nbrMatRoad -= 1

    print (toListMatRoad)

x = 0
nbrColumnMatEssence = len (MatEssence.matrice_essence_symm)
nbrMatEssence = nbrColumnMatEssence - 1
toListMatEssence = []
     
class GenerateListMatEssence :

    while (nbrMatEssence > 0) :
        arrayMatEssence = [MatEssence.matrice_essence_symm[x,:]]   
        
        arrayToListMatEssence= arrayMatEssence[-1]
        arrayToListMatEssence = np.ndarray.tolist(arrayToListMatEssence)

        testMatEssence = arrayToListMatEssence[-nbrMatEssence:]
        
        toListMatEssence.extend(testMatEssence)
        i += 1
        nbrMatEssence -= 1

    print ("\n",toListMatEssence)