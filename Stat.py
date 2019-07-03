# -*- coding: utf-8 -*-
"""
Created on Tue Jul  2 13:29:20 2019
@author: antoi
"""
import numpy as np
from random_matrice import MatRoad,MatEssence
from faker import Faker
from liste_generator import GenerateListMatRoad, GenerateListMatEssence

class StatistiqueMatRoad :
    print("\n statistique sur les villes")
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

class StatistiqueMatEssence :
    print("\n statistique sur l'essence")
    nbrItems = int(len(toListMatEssence))
    print("nombres d'echantillons : ", nbrItems)
    
    Q1 = np.percentile(toListMatEssence, 25)
    print("quartile 1 :", Q1)
    
    mediane = np.percentile(toListMatEssence, 50)
    print("médiane :", mediane)
    
    Q3 = np.percentile(toListMatEssence, 75)
    print("quartile 3 :", Q3)
    
    intervalle= Q3- Q1
    print("intervalle : ",intervalle)
    
    mode=np.median(toListMatEssence)
    print("mode :",mode)
    
    moyenne=np.mean(toListMatEssence)
    print("moyenne :",moyenne)
    
    variance=np.var(toListMatEssence)
    print("variance :",variance)
    
    deviantion=np.std(toListMatEssence)
    print("déviation :",deviantion)
    
    minimum=np.min(toListMatEssence)
    print("minimum :",minimum)
    
    maximum=np.max(toListMatEssence)
    print("maximum :",maximum)  