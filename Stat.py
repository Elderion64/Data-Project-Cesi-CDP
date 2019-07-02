# -*- coding: utf-8 -*-
"""
Created on Tue Jul  2 13:29:20 2019
@author: antoi
"""
import numpy as np
from random_matrice import MatRoad
from faker import Faker
from scipy import stats


i = 0
nbrColumn = len (MatRoad.matrice_symm)
nbr = nbrColumn - 1
toListMatRoad = []
     
class GenerateListMatRoad :

    while (nbr > 0) :
        arrayMatRoad = [MatRoad.matrice_symm[i,:]]   
        
        arrayToListMatRoad= arrayMatRoad[-1]
        arrayToListMatRoad = np.ndarray.tolist(arrayToListMatRoad)
        "print (toList)"

        test = arrayToListMatRoad[-nbr:]
        "print (toList)"
        
        toListMatRoad.extend(test)   
        "print (toList)"
           
        i += 1
        nbr -= 1

    print (toListMatRoad)

class StatistiqueMatRoad :
    nbrItems = int(len(toListMatRoad))
    print("nombres d'echantillons : ", nbrItems)
    
    Q1 = np.percentile(toListMatRoad, 25)
    print("quartile 1 :", Q1)
    
    mediane = np.percentile(toListMatRoad, 50)
    print("médiane :", mediane)
    
    Q3 = np.percentile(toListMatRoad, 75)
    print("quartile 3 :", Q3)
    
    intervalle= Q3- Q1
    print("intervalle : ",intervalle)
    
    mode=np.median(toListMatRoad)
    print("mode :",mode)
    
    moyenne=np.mean(toListMatRoad)
    print("moyenne :",moyenne)
    
    variance=np.var(toListMatRoad)
    print("variance :",variance)
    
    deviantion=np.std(toListMatRoad)
    print("déviation :",deviantion)
    
    minimum=np.min(toListMatRoad)
    print("minimum :",minimum)
    
    maximum=np.max(toListMatRoad)
    print("maximum :",maximum)

    
   