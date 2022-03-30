# -*- coding: utf-8 -*-
"""
Created on Sat Feb 26 17:54:11 2022

Compresion

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

diametro = 1 #in
l0 = 2 #in

diametro *= (2.54/100) #m
area = mt.pi*(pow(diametro,2))/4 #m^2
l0    *= 25.4    #mm

for linea in archivo:
    # print(linea.replace('\n','').split("\t"))
    if contador >= 5:
        fuerza,desplazamiento,tiempo = linea.replace('\n','').split("\t")
        fuerzas.append(float(fuerza))
        desplazamientos.append(float(desplazamiento))
        tiempos.append(float(tiempo))
        esfuerzo = float(fuerza)/area #Kpa
        esfuerzos.append(esfuerzo)
        deformacion =  (float(desplazamiento))/l0
        deformaciones.append(deformacion)
        print(contador%40)
        string = f'{esfuerzo} \t{deformacion}\t {tiempo} \n'
        archivoDatos.write(str(string))
# =============================================================================
#         if (contador%40)==1:
#             string = f'{esfuerzo} \t{deformacion}\t {tiempo} \n'
#             archivoDatos.write(str(string))
# =============================================================================
    contador += 1
    
fuerzas = [-fuerza for fuerza in fuerzas]
desplazamientos =  [ -desplazamiento for desplazamiento in desplazamientos]
esfuerzos = [-esfuerzo for esfuerzo in esfuerzos]
deformaciones = [-deformacion for deformacion in deformaciones]

value = 150
esfuerzoFractura = esfuerzos[-1]
deformacionFractura = deformaciones[-1]
plt.plot(deformaciones,esfuerzos)
plt.scatter(deformacionFractura,esfuerzoFractura,color='red')
plt.scatter(deformaciones[value],esfuerzos[value],color ='black')
plt.grid()
plt.title('Diagrama de Esfuerzo vs Deformacion')
plt.ylabel('Esfuerzo [KPa]')
plt.xlabel('Deformaciones')
plt.show()

# =============================================================================
# plt.plot(tiempos,deformaciones)
# plt.grid()
# plt.title('Diagrama de Deformacion vs Tiempo')
# plt.ylabel('Deformaciones ε [mm/mm]')
# plt.xlabel('Tiempo [s]')
# plt.show()
# archivo.close()
# archivoDatos.close()
# =============================================================================
