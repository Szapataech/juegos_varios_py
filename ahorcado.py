import random

def ahorcado ():
    
    Palabras = ("AHORCADO", "COMPUTADOR", "PANTALLA", "HIPOPOTAMO", "DESARROLLO", "PYTHON", "MEDELLIN")
    
    palabra_secreta = random.choice(Palabras)
    
    palabra_secreta = palabra_secreta.upper()
    
    Oculta = ["_" for letra in palabra_secreta]  
     
    vidas = 5
    
    while vidas > 0 and "_" in Oculta:
        
        print(" ".join(Oculta))
        
        letra = input("Ingrese una letra: ").upper()
        
        if letra in palabra_secreta:
            for i in range(len(palabra_secreta)):
                if palabra_secreta[i] == letra:
                    Oculta[i] =letra
                    
        else:
            vidas -= 1
            print(f"La letra no está en la palabra, te quedan {vidas} vidas.")
            
    if "_" not in Oculta:
        print("Felicidades, adivinaste la palabra" + "".join(Oculta))
              
    else:
        print("Perdiste, te quedaste sin vidas, la palabra oculta era: " + palabra_secreta)
        
        
        
        
        
ahorcado()      
        
      
    
