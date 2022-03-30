# -*- coding: utf-8 -*-
"""
Created on Sun Feb 27 12:09:29 2022

@author: Daniel
"""

from matplotlib import pyplot as plt
import math as mt

archivo = open('specimen.dat') #Open document
archivoDatos = open('Datos.txt','w')
contador = 0
fuerzas = []
desplazamientos = []
tiempos = []
esfuerzos = []
deformaciones = []

diametro = 1/2 #in
l0 = 40 #cm 

diametro *= (2.54/100) #m
area = mt.pi*(pow(diametro,2))/4 #m^2
l0    *= 10    #mm
print(area)
for linea in archivo:
# =============================================================================
#     print(linea.replace('\n','').split("\t"))
# =============================================================================
    try :
        fuerza,desplazamiento,tiempo = linea.replace('\n','').split("\t")
        fuerzas.append(float(fuerza))
        desplazamientos.append(float(desplazamiento))
        tiempos.append(float(tiempo))
        esfuerzo = float(fuerza)/area #Kpa
        esfuerzos.append(esfuerzo)
        deformacion =  (float(desplazamiento))/l0
        deformaciones.append(deformacion)
        string = f'{esfuerzo} \t{deformacion}\t {tiempo} \n'
        archivoDatos.write(str(string))
 #       if (contador%50)==1:
  #          string = f'{esfuerzo} \t{deformacion}\t {tiempo} \n'
   #         archivoDatos.write(str(string))
        contador+=1
    except:    
        contador += 1
    
esfuerzoFractura = esfuerzos[-1]
deformacionFractura = deformaciones[-1]

esfuerzoUltimo = max(esfuerzos)
print(esfuerzoUltimo)
idUltimo = esfuerzos.index(esfuerzoUltimo)
deformacionUltima = deformaciones[idUltimo]
    
# =============================================================================
# fuerzas = [-fuerza foxr fuerza in fuerzas]
# desplazamientos =  [ -desplazamiento for desplazamiento in desplazamientos]
# esfuerzos = [-esfuerzo for esfuerzo in esfuerzos]
# deformaciones = [-deformacion for deformacion in deformaciones]
# 
# =============================================================================
value = 100
plt.plot(deformaciones,esfuerzos)
plt.grid()
plt.title('Diagrama de Esfuerzo vs Deformacion')
plt.scatter(deformacionUltima,esfuerzoUltimo,color ='green')
plt.scatter(deformacionFractura,esfuerzoFractura,color ='red')
plt.scatter(deformaciones[value],esfuerzos[value],color ='black')
plt.ylabel('Esfuerzo [KPa]')
plt.xlabel('Deformaciones [mm/mm]')
plt.show()

# =============================================================================
# plt.plot(desplazamientos,fuerzas)
# plt.grid()
# plt.title('Diagrama de Fuerza vs desplazamiento')
# plt.ylabel('Fuerza [KN]')
# plt.xlabel('Desplazamiento [mm]')
# plt.show()
# =============================================================================

archivo.close()
archivoDatos.close()