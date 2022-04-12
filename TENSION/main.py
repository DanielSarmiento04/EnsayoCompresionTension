# -*- coding: utf-8 -*-
"""
Created on Sun Feb 27 12:09:29 2022

@author: Daniel
"""

from matplotlib import pyplot as plt
import math as mt
import recurso.Graphmethods as gm
dataFile = open('./TENSION/specimen.dat')  # Open document   For reead
# dataFileDatos = open('./TENSION/Datos.txt', 'w')  # Open document   For write
forces, displacements, times, stresses, strains = [], [], [], [], []  # Declare empty lists for each data list

""" specimen information """
diameter = 1/2  # in
l0 = 40  # cm

""" Convert to SI """
diameter *= (2.54/100)  # m
area = mt.pi*(pow(diameter, 2))/4  # m^2
l0 *= 10  # mm

for line in dataFile:
    try:
        force, displacement, time = line.replace('\n', '').split("\t")
        forces.append(float(force))  #KN
        displacements.append(float(displacement)) #[mm]
        times.append(float(time))   #s
        
        stresses.append(float(force)/area) #[kPa]
        strains.append((float(displacement))/l0) #[mm/mm]
    except:
        pass

value = 100
# gm.GraphForceDisplacement(forces, desplazamientos)
gm.GraphStressStrain(stresses, strains, value)
dataFile.close()

