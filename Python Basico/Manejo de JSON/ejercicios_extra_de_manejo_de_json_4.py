import json

def pokemon_data(path):
    try:
        with open(path,'r', encoding="utf-8") as file:
            data_list = json.load(file)
        return data_list
    except FileNotFoundError as err:
        print("No se encontro el archivo json.")

def get_pokemon_types(data_list):
    pokemon_types = []
    for i in range(len(data_list)):
        if data_list[i]['type'] not in pokemon_types:
            pokemon_types.append(data_list[i]['type'])
    return pokemon_types

def group_pokemon_by_type(data_list, pokemon_type):
    pokemon_by_type = []
    for i in range(len(data_list)):
        if data_list[i]['type'] == pokemon_type:
                pokemon_by_type.append(data_list[i])
    return pokemon_by_type

def get_pokemon_type_level_avg(data_list):
    total_level = 0
    for i in range(len(data_list)):
            total_level += data_list[i]['level']
    try:
        level_avg = total_level / len(data_list)
        return level_avg
    except ZeroDivisionError as err:
        print("No hay Pokemones de este tipo. No se puede calcular el promedio.")

def print_pokemon_level_avg(data_list, types_list):
    for i in range(len(types_list)):
        print(f"Tipo: {types_list[i]}: {get_pokemon_type_level_avg(group_pokemon_by_type(data_list,types_list[i]))}")

def main():
    print("---- EJERCICIOS EXTRA DE MANEJO DE JSON - 4")
    print("Ver el promedio de nivel por tipo de Pokemones \n")
    pokemon_data_from_file = pokemon_data('pokemon.json')
    if pokemon_data_from_file != None:
        pokemon_types = get_pokemon_types(pokemon_data_from_file)
        print_pokemon_level_avg(pokemon_data_from_file,pokemon_types)

if __name__ == '__main__':
    main()