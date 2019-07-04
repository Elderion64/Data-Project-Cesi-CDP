# -*- coding: utf-8 -*-
"""
Created on Tue Jul  2 13:29:20 2019
@author: antoi
"""
import numpy as np
from liste_generator import GenerateListMatRoad

def StatistiqueMatRoad() :
    print("\n"+"General informations for the cities")
    nbrItems = int(len(GenerateListMatRoad.toListMatRoad))
    print("Number of samples : ", nbrItems)
    
    Q1 = np.percentile(GenerateListMatRoad.toListMatRoad, 25)
    print("First Quartile :", Q1, " km")
    
    mediane = np.percentile(GenerateListMatRoad.toListMatRoad, 50)
    print("Median :", mediane, " km")
    
    Q3 = np.percentile(GenerateListMatRoad.toListMatRoad, 75)
    print("Third Quartile :", Q3, " km")
    
    intervalle= Q3- Q1
    print("Interval : ",intervalle, " km")
    
    mode=np.median(GenerateListMatRoad.toListMatRoad)
    print("Mode :",mode, " km")
    
    moyenne=np.mean(GenerateListMatRoad.toListMatRoad)
    moyenne_deci = round(moyenne,2)
    print("Average :",moyenne_deci, " km")
    
    variance=np.var(GenerateListMatRoad.toListMatRoad)
    variance_deci = round(variance,2)
    print("Variance :",variance_deci, " km")
    
    deviation=np.std(GenerateListMatRoad.toListMatRoad)
    deviation_deci = round(deviation,2)
    print("Deflection :",deviation_deci, " km")
    
    minimum=np.min(GenerateListMatRoad.toListMatRoad)
    print("Minimum :",minimum, " km")
    
    maximum=np.max(GenerateListMatRoad.toListMatRoad)
    print("Maximum :",maximum, " km\n")
