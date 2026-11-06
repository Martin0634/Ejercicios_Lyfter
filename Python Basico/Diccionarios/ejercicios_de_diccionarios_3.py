print("---- EJERCICIOS DE DICCIONARIOS - 3")

list_of_keys = ['access_level', 'age']
employee = {
    'name': 'Jhon',
    'email': 'jhon@umbrellacorp.com',
    'access_level': 5,
    'age': 28
}

for i in range(len(list_of_keys)):
    employee.pop(list_of_keys[i])

for i,j in employee.items():
    print(f"{i}: {j}")