import csv

def write_csv_file(path, data, headers):
    try:
        with open(path, 'x', encoding='utf-8', newline="") as file:
            headers = data[0].keys()
            writer = csv.DictWriter(file, fieldnames=headers)
            writer.writeheader()
            writer.writerows(data)
            print("Archivo creado.")
    except:
        with open(path, 'a', encoding='utf-8', newline="") as file:
            headers = data[0].keys()
            writer = csv.DictWriter(file, fieldnames=headers)
            writer.writerows(data)
            print("Informacion agregada.")

def user_input(headers):
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
            write_csv_file('videogames_data.csv',data_collection,headers)
    
        if user_option == 2:
            print("Hasta pronto!")

def main():
    headers = ['Nombre', 'Genero', 'Desarrollador', 'Clasificacion ESRB']
    user_input(headers)

if __name__ == '__main__':
    main()