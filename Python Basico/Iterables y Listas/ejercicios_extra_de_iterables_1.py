print("---- EJERCICIOS EXTRA DE ITERABLES Y LISTAS - 1")

user_list = []
num = 0
flag = 'y'
count = 0

user_list.append(int(input("Digite el primer número de la lista: ")))
flag = input("Desea ingresar otro número? (y/n): ")

while flag != 'n' and flag != 'N' and flag != 'no':
    user_list.append(int(input("Ingrese un número: ")))
    flag = input("Desea ingresar otro número? (y/n): ")

num = int(input("Digite el número a buscar: "))
for i in range(len(user_list)):
    if user_list[i] == num:
        count += 1
        
print(f"Su lista es {user_list}")
print(f"El número {num} aparece {count} veces")