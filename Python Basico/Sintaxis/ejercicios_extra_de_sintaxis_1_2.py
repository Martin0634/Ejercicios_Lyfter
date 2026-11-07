print("---- EJERCICIOS EXTRA DE SINTAXIS - 2")

time_10_minutes = 10*60
res = 0

user_time = int(input("Ingrese la cantidad de segundos: "))
res = time_10_minutes - user_time

if res < 0:
    print("MAYOR")
elif res > 0:
    print(f"Para llegar a 10 minutos faltaron {res} segundos")
else:
    print("IGUAL")