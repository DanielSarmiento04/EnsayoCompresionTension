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

dataFile = open("./COMP/specimen.dat")  # Open document where is the data

forces, displacements, times, stresses, strains = [ [], [], [], [], [] ]

# specimen data
diameter = 1  # in
l0 = 2  # in

# Conversion
diameter *= (2.54/100)  # m
area = mt.pi*(pow(diameter, 2))/4  # m^2
l0 *= 25.4  # mm

for line in dataFile:
    try:
        force, displacement, time = line.replace('\n', '').split("\t")
        forces.append(float(force)) #KN
        displacements.append(float(displacement)) #mm
        times.append(float(time))  #s
        stresses.append(float(force)/area) #KPa
        strains.append((float(displacement))/l0) #mm/mm
    except:
        pass

forces = [-force for force in forces]
displacements = [-displacement for displacement in displacements]
stresses = [-esfuerzo for esfuerzo in stresses]
strains = [-deformacion for deformacion in strains]

value = 150
gr.GraphStressStrain(stresses, strains, value)
# gr.GraphForceDisplacement(forces, displacements, value)

