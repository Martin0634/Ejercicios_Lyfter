import csv

def write_csv_file(path, data):
    try:
        with open(path, 'x', encoding='utf-8', newline='') as file:
            headers = data[0].keys()
            writer = csv.DictWriter(file, fieldnames=headers, delimiter='\t')
            writer.writeheader()
            writer.writerows(data)
    except:
        with open(path, 'a', encoding='utf-8', newline='') as file:
            headers = data[0].keys()
            writer = csv.DictWriter(file, fieldnames=headers, delimiter='\t')
            writer.writerows(data)
    print("Archivo creado.")

headers = ['Nombre', 'Genero', 'Desarrollador', 'Clasificacion ESRB']

user_option = 0

while user_option != 2:
    data_collection = [0]
    new_entry = {}
    print("MENU DE OPCIONES")
    print("1. Agregar registro")
    print("2. Salir")
    try:
        user_option = int(input("Elija una opcion: "))
        if user_option > 2 or user_option < 1:
            raise ValueError("Opcion no valida. Elija una opcion del menu:")
    except ValueError as err:
        print("Invalido. Elija una opcion (y/n). ")
        user_option = 0
    
    if user_option == 1:
        for i in headers:
            new_entry[i] = input(f"Digite {i}: ")
        data_collection[0] = new_entry
        write_csv_file('videogames_data_tab_separator.csv',data_collection)
    
print("Hasta pronto!")