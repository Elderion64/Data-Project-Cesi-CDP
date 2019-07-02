# -*- coding: utf-8 -*-
import numpy as np
from random_matrice import Cities, MatEssence, MatRoad


with open('data.txt', 'w') as writeFile :
    writeFile.write('Liste des villes\n\n')
    writeFile.writelines(Cities.cities_list)
    writeFile.write('\n\n')
    
    writeFile.write('Matrice de la distance entre les villes (en km)\n\n')
    np.savetxt(writeFile, MatRoad.matrice_symm, fmt='%d', delimiter='   ', newline='\n')
    writeFile.write('\n')
    writeFile.write('Matrice de la conssomation d\'essence entre les villes (valeur multiplicatrice)\n\n')
    np.savetxt(writeFile, MatEssence.matrice_essence_symm, fmt='%1.1f', delimiter='  ', newline='\n')


writeFile.close()



