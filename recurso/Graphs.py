from matplotlib import pyplot as plt


def GraphStressStrain(esfuerzos,deformaciones,value ) -> None:
    """This functioon has to get a listor tuple with data """

    esfuerzoFractura = esfuerzos[-1]
    deformacionFractura = deformaciones[-1]
    plt.plot(deformaciones, esfuerzos)
    plt.scatter(deformacionFractura, esfuerzoFractura, color='red')
    plt.scatter(deformaciones[value], esfuerzos[value], color='black')
    plt.grid()
    plt.title('Diagrama de Esfuerzo vs Deformacion')
    plt.ylabel('Esfuerzo [KPa]')
    plt.xlabel('Deformaciones')
    plt.show()
