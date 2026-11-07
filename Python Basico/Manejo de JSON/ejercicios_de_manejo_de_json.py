import json

def pokemon_data(path):
    try:
        with open(path,'r', encoding="utf-8") as file:
            data_list = json.load(file)
        return data_list
    except FileNotFoundError as err:
        print("No se encontro el archivo json.")

def new_pokemon_data(path,data_list):
    new_pokemon = {}
    if len(data_list) == 0:
        print(f"Archivo {path} sin informacion. Por favor verifique.")
    else:
        for i in range(0,1):
            for data_keys in data_list[i].keys():
                if type(data_list[i][data_keys]) is str:
                    new_pokemon[data_keys] = input(f"{data_keys}: ").strip()
                elif type(data_list[i][data_keys]) is int:
                    flag = True
                    while flag:
                        try:
                            new_pokemon[data_keys] = int(input(f"{data_keys}: "))
                            flag = False
                        except ValueError as err:
                            print("Dato invalido. Ingrese un numero")
                            flag = True
                elif type(data_list[i][data_keys]) is float:
                    flag = True
                    while flag:
                        try:
                            new_pokemon[data_keys] = float(input(f"{data_keys}: "))
                            flag = False
                        except ValueError as err:
                            print("Dato invalido. Ingrese un numero.")
                            flag = True
                elif type(data_list[i][data_keys]) is list:
                    flag = True
                    while flag:
                        try:
                            count = int(input("Cuantas habilidades tiene?: "))
                            flag = False
                            new_pokemon[data_keys] = []
                        except ValueError as err:
                            print("Dato invalido. Ingrese un numero:")
                            flag = True
                    for j in range(count):
                        user_input = input("Digite habilidad: ")
                        new_pokemon[data_keys].append(user_input)
                elif type(data_list[i][data_keys]) is dict:
                    new_pokemon[data_keys] = {}
                    for k in data_list[i][data_keys].keys():
                        flag = True
                        while flag:
                            try:
                                new_pokemon[data_keys].update({k: int(input(f"Ingrese {k}: "))})
                                flag = False
                            except ValueError as err:
                                print("Dato no valido. Ingrese un numero.")
                                flag = True
        data_list.append(new_pokemon)
        with open(path, 'w', encoding="utf-8") as result_file:
            json.dump(data_list, result_file, ensure_ascii=False, indent=4)
        print(f"Datos escritos en archivo {path}")

def main():
    print("---- EJERCICIOS DE MANEJO DE JSON - 1")
    print("Agregar un Pokemon \n")
    path = 'pokemon.json'
    pokemon_data_from_file = pokemon_data(path)
    if pokemon_data_from_file is not None:
        new_pokemon_data(path, pokemon_data_from_file)

if __name__ == '__main__':
    main()
