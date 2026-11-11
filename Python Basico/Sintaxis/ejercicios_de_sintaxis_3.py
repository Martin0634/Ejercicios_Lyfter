import random

print("---- EJERCICIO DE SINTAXIS - 3")

secret_num = random.randint(1, 10)
user_num = int(input("Adivine el número secreto entre 1 y 10: "))

if user_num > 10 or user_num < 0:
    while user_num > 10 or user_num < 0:
        user_num = int(input("Debe ingresar un número entre 1 y 10: "))

while user_num != secret_num:
    print(f"Incorrecto. {user_num} no es el número secreto.")
    user_num = int(input("Intente una vez más: "))
    if user_num > 10 or user_num < 0:
        while user_num > 10 or user_num < 0:
            user_num = int(input("Debe ingresar un número entre 1 y 10: "))

print(f"Correcto! {user_num} es el número secreto")