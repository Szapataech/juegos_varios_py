def calcular_pago_total(cantidad_horas, valor_hora):
    try:
        cantidad_horas = float(cantidad_horas)
        valor_hora = float(valor_hora)
        
        if cantidad_horas >= 0 and valor_hora >= 0:
            pago_total = cantidad_horas * valor_hora
            return pago_total
        else:
            return "La cantidad de horas y el valor por hora deben ser valores positivos."
    
    except ValueError:
        return "Ingrese valores numéricos válidos para la cantidad de horas y el valor por hora."

if __name__ == "__main__":
    cantidad_horas = input("Ingrese la cantidad de horas trabajadas: ")
    valor_hora = input("Ingrese el valor por hora: ")
    
    pago = calcular_pago_total(cantidad_horas, valor_hora)
    
    if isinstance(pago, float):
        print(f"El pago total es: ${pago:.2f}")
    else:
        print(pago)
