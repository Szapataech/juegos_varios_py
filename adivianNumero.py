import random

numero = random.randint(0, 100)
minumero = 101
intentos = 0

print("introduce un numero 1 al 100")

while numero != minumero:
    intentos += 1
    minumero = int(input())
    if minumero > numero:
        print("el numero es más bajo")
    if minumero < numero:
        print("el numero es más alto")

print(f"correcto has necesitado {intentos} intentos")