print("---- EJERCICIOS DE ITERABLES Y LISTAS - 5")

user_list = [0,0,0,0,0,0,0,0,0,0]
user_list[0] = int(input("Digite un número: "))
largest = user_list[0]
for i in range(1,len(user_list)):
    user_list[i] = int(input("Digite un número: "))
    if user_list[i] > largest:
        largest = user_list[i]
print (f"Su lista de números es: {user_list} y el número mayor es: {largest}")