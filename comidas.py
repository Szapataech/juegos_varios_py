# Diccionario de alimentos y sus ingredientes
alimentos = {
    "Pizza": ["Masa", "Salsa de tomate", "Queso", "Pepperoni"],
    "Hamburguesa": ["Pan de hamburguesa", "Carne de res", "Lechuga", "Tomate", "Queso", "Mayonesa"],
    "Ensalada": ["Lechuga", "Tomate", "Pepino", "Aceite de oliva", "Vinagre"],
}

# Función para pedir comida y mostrar ingredientes
def pedir_comida_y_mostrar_ingredientes():
    print("Menú de alimentos:")
    for alimento in alimentos.keys():
        print(f"- {alimento}")

    pedido = input("¿Qué alimento te gustaría pedir? ").strip()

    if pedido in alimentos:
        print(f"Ingredientes de {pedido}:")
        for ingrediente in alimentos[pedido]:
            print(f"- {ingrediente}")
    else:
        print(f"{pedido} no está en el menú.")

# Llamamos a la función principal
pedir_comida_y_mostrar_ingredientes()
