print("---- EJERCICIOS EXTRA DE SINTAXIS - 3")

sum = 0
num = int(input("Digite su número favorito: "))

for counter in range(1,num+1):
    sum += counter

print(f"La suma de 1 a {num} es: {sum}")