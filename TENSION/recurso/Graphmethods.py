from matplotlib import pyplot as plt

""" Create a function that can be used to create a graph from 2 lists """
""" The function get a list for forces and a list for displacements """
""" The function will return a graph with the force and displacement """


def GraphForceDisplacement(Forces: list[float], displacements: list[float]) -> None:
    """ Create a graph with the forces and displacements """
    maxForce = max(Forces)
    displacementMaxForces = displacements[Forces.index(maxForce)]

    plt.plot(displacements, Forces, 'b')
    plt.scatter(displacementMaxForces, maxForce, color='red')
    plt.scatter(displacements[-1], Forces[-1], color='#CCEE20')
    plt.grid()
    plt.title('Diagrama de Fuerza vs Desplazamiento')
    plt.ylabel('Fuerza [KN]')
    plt.xlabel('Desplazamiento [mm]')
    plt.legend(['Fuerza vs Desplazamiento', 'Fractura'])
    plt.show()


def GraphStressStrain(esfuerzos: list[float], deformaciones: list[float], value: int) -> None:
    """ Create a graph with the stresses and strains """
    maxStress = max(esfuerzos)
    strainMaxStress = deformaciones[esfuerzos.index(maxStress)]

    esfuerzoFractura = esfuerzos[-1]
    deformacionFractura = deformaciones[-1]
    plt.plot(deformaciones, esfuerzos)
    plt.plot(strainMaxStress, maxStress, 'ro')
    plt.scatter(deformacionFractura, esfuerzoFractura, color='red')
    plt.scatter(deformaciones[value], esfuerzos[value], color='black')
    plt.grid()
    plt.title('Diagrama de Esfuerzo vs Deformacion')
    plt.ylabel('Esfuerzo [KPa]')
    plt.xlabel('Deformaciones [mm/mm]')
    plt.show()
