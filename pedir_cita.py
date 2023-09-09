# Inicializamos una lista de citas disponibles
citas_disponibles = [
    {"fecha": "2023-09-10", "hora": "10:00 AM"},
    {"fecha": "2023-09-10", "hora": "11:00 AM"},
    {"fecha": "2023-09-11", "hora": "9:00 AM"},
    {"fecha": "2023-09-11", "hora": "10:00 AM"},
]

# Función para mostrar citas disponibles
def mostrar_citas_disponibles():
    print("Citas disponibles:")
    for i, cita in enumerate(citas_disponibles):
        print(f"{i + 1}. Fecha: {cita['fecha']}, Hora: {cita['hora']}")

# Función para pedir una cita
def pedir_cita():
    mostrar_citas_disponibles()
    seleccion = input("Seleccione el número de la cita que desea reservar (o 'q' para salir): ")
    
    if seleccion.lower() == 'q':
        return
    
    try:
        seleccion = int(seleccion)
        if 1 <= seleccion <= len(citas_disponibles):
            cita_elegida = citas_disponibles.pop(seleccion - 1)
            print(f"Ha reservado la cita para el {cita_elegida['fecha']} a las {cita_elegida['hora']}.")
        else:
            print("Selección no válida. Por favor, elija un número de cita válido.")
    except ValueError:
        print("Entrada no válida. Ingrese el número de la cita que desea reservar.")

# Ejecutamos el programa
while True:
    opcion = input("1. Ver citas disponibles\n2. Pedir una cita\n3. Salir\nSeleccione una opción: ")
    
    if opcion == '1':
        mostrar_citas_disponibles()
    elif opcion == '2':
        pedir_cita()
    elif opcion == '3':
        break
    else:
        print("Opción no válida. Por favor, elija una opción válida.")