from random import randint

def play():
    guess = randint(1, 100)
    times = 1
    user_input = int(input("Ingresa un numero del 1 al 100:"))

    while user_input != guess and user_input != -1 and times < 5:
        times += 1
        if (user_input > guess):
            print(f"El numero es menor que {user_input}")
        else:
            print(f"El numero es mayor que {user_input}")
        user_input = int(input("Ingresa otro numero (si queres salir -1):"))

    if times == 5:
        continue_playing = input("Perdiste, quieres intentar de nuevo? (si/no)")
        if (continue_playing == "si"):
            play()
        else:
            print("Tal vez la próxima entonces!")
    elif user_input == guess:
        print(f"Adivinaste! El numero es: {guess}")
    else:
        print("Tal vez la próxima entonces!")

play()

# Bonus

# Se podría decir que hay más de un bug en este programa, por ejemplo si ingresamos un string en lugar de un numero, como se puede solucionar?
# Se puede condicionar al input para que, luego de haber tomado el valor del usuario, valide si es o no un entero (con la funcion isdigit()). En caso de que no sea un entero
# se le vuelve a pedir que ingrese nuevamente un valor
