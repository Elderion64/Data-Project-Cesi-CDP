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


def create_csv(time, vehicles, list_distance) :
    with open('DataPathfinder_time.csv', 'w') as csvFileDataTime :
        writer = csv.writer(csvFileDataTime)
        column_list = ['Temps de calcul']
        writer.writerow(column_list)
        writer.writerow(time)
        csvFileDataTime.close()
            
    with open('DataPathfinder_vehicles.csv', 'w') as csvFileDataVehicles :
        writer = csv.writer(csvFileDataVehicles)
        column_list = ['Nombre de véhicule']
        writer.writerow(column_list)
        writer.writerow(vehicles)
        
        csvFileDataVehicles.close()

    with open('DataPathfinder_road.csv', 'w') as csvFileDataRoad :
        writer = csv.writer(csvFileDataRoad, delimiter='\n')
        column_list = ['Distance parcouru par les véhicules']
        writer.writerow(column_list)
        writer.writerows(list_distance)
        
        csvFileDataRoad.close()
