# -*- coding: utf-8 -*-
"""
Created on Sat Feb 26 17:54:11 2022

Compresion

@author: Daniel
"""
from matplotlib import pyplot as plt
import math as mt
# import Graphs from folder /recursos/Graphs
from recurso import GraphMethods as gr
# sys.path.append(r'C:\Users\Daniel\Documents\GitHub\COMP\recursos\Graphs') 

archivo = open("./COMP/specimen.dat")  # Open document where is the data

fuerzas, desplazamientos, tiempos, esfuerzos, deformaciones = [
    [], [], [], [], []]

# specimen data
diametro = 1  # in
l0 = 2  # in

# Conversion
diametro *= (2.54/100)  # m
area = mt.pi*(pow(diametro, 2))/4  # m^2
l0 *= 25.4  # mm

for linea in archivo:
    try:
        fuerza, desplazamiento, tiempo = linea.replace('\n', '').split("\t")
        fuerzas.append(float(fuerza)) #KN
        desplazamientos.append(float(desplazamiento)) #mm
        tiempos.append(float(tiempo))  #s
        esfuerzos.append(float(fuerza)/area) #KPa
        deformaciones.append((float(desplazamiento))/l0) #mm/mm
    except:
        pass

fuerzas = [-fuerza for fuerza in fuerzas]
desplazamientos = [-desplazamiento for desplazamiento in desplazamientos]
esfuerzos = [-esfuerzo for esfuerzo in esfuerzos]
deformaciones = [-deformacion for deformacion in deformaciones]

value = 150
gr.GraphStressStrain(esfuerzos, deformaciones, value)
# gr.GraphForceDisplacement(fuerzas, desplazamientos, value)

