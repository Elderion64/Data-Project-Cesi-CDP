# -*- coding: utf-8 -*-
import numpy as np
import csv
from random_matrice import Cities, MatRoad


with open('data.txt', 'w') as txtFile :
    txtFile.write('Liste des villes\n\n')
    txtFile.writelines(Cities.cities_list)
    txtFile.write('\n\n')
    
    txtFile.write('Matrice de la distance entre les villes (en km)\n\n')
    np.savetxt(txtFile, MatRoad.matrice_symm, fmt='%1.1f', delimiter='   ', newline='\n')



txtFile.close()

with open('distance.csv', 'w') as csvFile :
    writer = csv.writer(csvFile, delimiter=';')
    writer.writerow(Cities.cities_list)
    np.savetxt(csvFile, MatRoad.matrice_symm, fmt='%1.1f', delimiter=';', newline='\n')
    
csvFile.close()
