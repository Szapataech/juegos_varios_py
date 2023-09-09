from adivianNumero import adivianNumero
from ahorcado  import ahorcado
from calcular  import calcular
from comidas import comidas
from pedir_cita import pedir_cita
from PPyT import PPyT

option = 0

while option != 7:
    print("Qué desea hacer?: \n Adivinar un número: 1 \n Jugar ahorcado: 2 \n calcular el pago por el valor de las horas: 3 \n saber si puede hacer una receta: 4 \n Pedir una cita médica: 5 \n Jugar piedra, papel o tijera: 6 \n salir: 7")
    option = int(input("Elija una opcion: "))
    
    if option == 1:
        adivianNumero()
    elif option == 2:
        ahorcado()
    elif option == 3:
        calcular()
    elif option == 4:
        comidas()
    elif option == 5:
        pedir_cita()
    elif option == 6:
        PPyT()
    elif option == 7:
        print("Saliendo del programa")
    else:
        print("Opción no válida")
        
        
