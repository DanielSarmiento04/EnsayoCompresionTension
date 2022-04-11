from matplotlib import pyplot as plt

def GraphStressStrain(esfuerzos:list[float],deformaciones:list[float],value:int ) -> None:
    """This functioon has to get a listor tuple with data """
    esfuerzoFractura = esfuerzos[-1]
    deformacionFractura = deformaciones[-1]
    plt.plot(deformaciones, esfuerzos)
    plt.scatter(deformacionFractura, esfuerzoFractura, color='red')
    plt.scatter(deformaciones[value], esfuerzos[value], color='black')
    plt.grid()
    plt.title('Diagrama de Esfuerzo vs Deformacion')
    plt.ylabel('Esfuerzo [KPa]')
    plt.xlabel('Deformaciones [mm/mm]')
    plt.show()


"""" Create a function to grapic the Force-displacement curve """
""" The function get a list of Force and a list of Displacement and a value to plot """

def GraphForceDisplacement(fuerzas:list[float],desplazamientos:list[float],value:int) -> None:
    """This function has to get a list of Force and a list of Displacement and a value to plot """
    fuerzaFractura = fuerzas[-1]
    desplazamientoFractura = desplazamientos[-1]
    plt.plot(desplazamientos, fuerzas)
    plt.scatter(desplazamientoFractura, fuerzaFractura, color='red')
    plt.scatter(desplazamientos[value], fuerzas[value], color='black')
    plt.grid()
    plt.title('Diagrama de Fuerza vs Desplazamiento')
    plt.ylabel('Fuerza [KN]')
    plt.xlabel('Desplazamientos [mm]')
    plt.show()
    