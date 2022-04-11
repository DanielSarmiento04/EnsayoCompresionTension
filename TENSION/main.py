# -*- coding: utf-8 -*-
"""
Created on Sun Feb 27 12:09:29 2022

@author: Daniel
"""

from matplotlib import pyplot as plt
import math as mt
import recurso.Graphmethods as gm
archivo = open('./TENSION/specimen.dat')  # Open document   For reead
# archivoDatos = open('./TENSION/Datos.txt', 'w')  # Open document   For write
fuerzas, desplazamientos, tiempos, esfuerzos, deformaciones = [], [], [], [], []  # Declare empty lists for each data list

""" specimen information """
diametro = 1/2  # in
l0 = 40  # cm

""" Convert to SI """
diametro *= (2.54/100)  # m
area = mt.pi*(pow(diametro, 2))/4  # m^2
l0 *= 10  # mm

for linea in archivo:
    try:
        fuerza, desplazamiento, tiempo = linea.replace('\n', '').split("\t")
        fuerzas.append(float(fuerza))
        desplazamientos.append(float(desplazamiento))
        tiempos.append(float(tiempo))
        
        esfuerzos.append(float(fuerza)/area)
        deformaciones.append((float(desplazamiento))/l0)
    except:
        pass

value = 100
# gm.GraphForceDisplacement(fuerzas, desplazamientos)
gm.GraphStressStrain(esfuerzos, deformaciones, value)
archivo.close()

