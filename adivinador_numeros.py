from random import randint

intentos = 0
numero_usuario = 0
numero_programa = randint(1, 100)
nombre = input(f"Ingresa tu nombre: ")

print(f"Bueno,{nombre} he pensado un número entre 1 y 100 y tienes solo ocho intentos para adivinar cuál crees que es el número")

while intentos < 8:
    numero_usuario = int(input("Cuál es el número?: "))
    intentos += 1

    if numero_usuario < numero_programa:
        print("Mi numero es mas alto")
    elif numero_usuario > numero_programa:
        print("Mi numero es mas bajo")
    else:
        print(f"Felicidades {nombre} adivinaste en {intentos} intentos")
        break
if numero_usuario != numero_programa:
    print(f"Agotaste todos los intentos. El numero secreto era {numero_programa}")