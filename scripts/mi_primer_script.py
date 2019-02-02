# Esto es un comentario, y no se ejecuta.

# Importamos el modulo math
import math

# Imprimimos por pantalla Hola estudiantes del curso de Python
print("Hola estudiantes del curso de Python")

flag = True

# Iniciamos un bucle que dura hasta que recibamos un numero correcto, que cambia el valor de flag
while flag:
    
    number = input("¿Cuántos sois hoy en clase?\n")
    
    try:
        # Imprimimos por pantallas una pregunta y capturamos su respuesta, que convertimos a entero
        number = int(number)
        
        if number > 0:
            print("¡Anda! ¡Muy bien! espero que aprendáis mucho")
            
            root = math.sqrt(number)
            print(f"Por cierto, la raiz de {number} es {root}")
            flag = False
        else:
            # LAnzamos un error si el valor es erróneo
            raise ValueError('No puede haber un numero negativo de personas')
    except (ValueError, AttributeError):
        print('Por favor, introduce un número entero y positivo')
        flag = True
    except:
        raise