print("---- EJERCICIOS EXTRA DE ITERABLES Y LISTAS - 5")

user_list = []
four_letter_list = []

print("Escriba cinco palabras una por una: ")

for i in range(5):
    user_list.append(input(f"Palabra {i+1}: "))
    if len(user_list[i]) > 4:
        four_letter_list.append(user_list[i])

print(f"Las palabras que tienen más de cuatro letras son: {four_letter_list}")