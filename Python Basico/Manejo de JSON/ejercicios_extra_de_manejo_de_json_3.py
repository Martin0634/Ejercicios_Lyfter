import json

def pokemon_data(path):
    try:
        with open(path,'r', encoding="utf-8") as file:
            data_list = json.load(file)
        return data_list
    except FileNotFoundError as err:
        print("No se encontro el archivo json.")

def print_pokemon_stats(data_list):
    for i in range(len(data_list)):
        print(f"{i+1}: {data_list[i]['name']}")
        print("Stats:")
        for j,k in data_list[i]['stats'].items():
            print(f"    {j}: {k}")
        print("")

def main():
    print("---- EJERCICIOS EXTRA DE MANEJO DE JSON - 3")
    print("Ver estadisticas de todos los Pokemones \n")
    print_pokemon_stats(pokemon_data('pokemon.json'))

if __name__ == '__main__':
    main()