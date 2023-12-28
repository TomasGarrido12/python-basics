# Tipos basicos (number, string, lists, etc): https://docs.python.org/es/3.12/tutorial/introduction.html
# Control de flujo (for, while, etc): https://docs.python.org/es/3.12/tutorial/controlflow.html

# Vamos a hacer un ejercicio para familiarizarnos con el lenguaje y los tipos de datos

# La idea es hacer un programa en que el usuario adivine un numero entero del 1 al 100,
# dandole pistas si el numero ingresado es mayor o menor.
# En caso de ser igual, dar un mensaje tipo "Adivinaste!" o algo asi.

# Para generar un numero aleatorio en un rango podemos usar `from random import randint` como en este ejemplo
from random import randint

def play():
    guess = randint(1, 100)
    name = input("Ingresa tu nombre:")
    
    print(f"Hola {name}! Este es un numero aleatorio: {guess}")

play()

# Nota
# Está bueno anotar los aprendizajes, por ejemplo para este ejercicio que es de exploración, diferencias con lenguajes que ya utilizaste antes.
# (podés trackearlo en Notion, Github, o donde te sea cómodo).

# Bonus 1
# Mismo ejercicio, pero solo tiene 5 oportunidades, si el usuario usa las 5 poner un cartel "Perdiste, intenta de nuevo!" o algo asi y salir.

# Bonus 2
# Mostrar al final todas las adivinanzas fallidas del usuario (tal vez haya alguna estructura de datos que nos pueda servir para esto? 🤔)
