# Tipos basicos (number, string, lists, etc): https://docs.python.org/es/3.12/tutorial/introduction.html
# Control de flujo (for, while, etc): https://docs.python.org/es/3.12/tutorial/controlflow.html

# Vamos a hacer un ejercicio para familiarizarnos con el lenguaje y los tipos de datos

# La idea es hacer un programa en que el usuario adivine un numero entero del 1 al 100,
# dandole pistas si el numero ingresado es mayor o menor.
# En caso de ser igual, dar un mensaje tipo "Adivinaste!" o algo asi.

# Para generar un numero aleatorio en un rango podemos usar `from random import randint` como en este ejemplo
from random import randint

#def play():
    #guess = randint(1, 100)
    #name = input("Ingresa tu nombre:")
    
    #print(f"Hola {name}! Este es un numero aleatorio: {guess}")

#play()

# Nota
# Está bueno anotar los aprendizajes, por ejemplo para este ejercicio que es de exploración, diferencias con lenguajes que ya utilizaste antes.
# (podés trackearlo en Notion, Github, o donde te sea cómodo).
#La principal diferencia que noto es que no tenés que definir el tipo de variable.
#Las listas aceptan distintos tipos de variables

# Bonus 1
# Mismo ejercicio, pero el usuario solo tiene 5 oportunidades, si usa las 5 poner un cartel "Perdiste, intenta de nuevo!" o algo asi y salir.

# Bonus 2
# Mostrar al final todas las adivinanzas fallidas del usuario (tal vez haya alguna estructura de datos que nos pueda servir para esto? 🤔)

#----------------------------------------------------------------------------------------------
#Ejercicio 1
random_number = randint(1,100)
print(f"El numero aleatorio es {random_number}")

repuesta = 0
respuestas_fallidas = []

def pepe():
    print("pepe")

def play(random_number, respuesta, respuestas_fallidas):
    oportunidades = 5

    while random_number != respuesta and oportunidades > 0:
        oportunidades -= 1
        respuesta = int(input("Elegi un numero entre el 1 y el 100:"))
        if random_number > respuesta:
            if oportunidades == 0:
                respuestas_fallidas.append(respuesta)
                print("Perdiste, intenta de nuevo!")
                break
            else:
                respuestas_fallidas.append(respuesta)    
                print(f"Te quedaste corto, papá. Te quedan {oportunidades} oportunidad/es")
        elif random_number < respuesta:
            if oportunidades == 0:
                print("Perdiste, intenta de nuevo!")
                break
            else:
                respuestas_fallidas.append(respuesta) 
                print(f"Uff, te pasaste!! Te quedan {oportunidades} oportunidad/es")
        else:
            print(f"Ganaste!! Y te sobraron {oportunidades} oportunidad/es")
            break
    print(f"Estas son los numeros que elegiste, pero que estaban mal: {respuestas_fallidas}")


play(random_number, repuesta, respuestas_fallidas)
#----------------------------------------------------------------------------------------------
# En este ejercicio siento que se podria haber atomizado mucho mas definiento mas funciones.