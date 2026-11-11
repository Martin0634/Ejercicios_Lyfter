import json

def pokemon_data(path):
    try:
        with open(path,'r', encoding="utf-8") as file:
            data_list = json.load(file)
        return data_list
    except FileNotFoundError as err:
        print(f"No se encontro el archivo {path}.")

def print_pokemon(data_list):
    for i in range(len(data_list)):
        if i == 0:
            print(f"Pokemon {i+1}")
        else:
            print(f"\nPokemon {i+1}")
        for data_keys in data_list[i].keys():
            if type(data_list[i][data_keys]) is str or type(data_list[i][data_keys]) is int or type(data_list[i][data_keys]) is float:
                print(f"{data_keys}: {data_list[i][data_keys]}")
            elif type(data_list[i][data_keys]) is list:
                print(f"{data_keys}: ")
                for j in range(len(data_list[i][data_keys])):
                    print(f"    {data_list[i][data_keys][j]}")

def main():
    pokemon_file_data = pokemon_data('pokemon.json')
    print("---- EJERCICIOS EXTRA DE MANEJO DE JSON - 1")
    print("Ver todos los Pokemones \n")
    if pokemon_file_data != None:
        print_pokemon(pokemon_file_data)

if __name__ == '__main__':
    main()