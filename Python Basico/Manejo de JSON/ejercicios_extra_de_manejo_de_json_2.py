import json

def pokemon_data(path):
    try:
        with open(path,'r', encoding="utf-8") as file:
            data_list = json.load(file)
        return data_list
    except FileNotFoundError as err:
        print("No se encontro el archivo json.")

def pokemon_list_of_types(data_list):
    pokemon_types_list = []
    for i in range(len(data_list)):
        if data_list[i]['type'] not in pokemon_types_list:
            pokemon_types_list.append(data_list[i]['type'])
    return pokemon_types_list

def list_to_string(data_list):
    result_string = ''
    for i in range(len(data_list)):
        if i == 0:
            result_string = data_list[i]
        else:
            result_string = result_string + ", " + data_list[i]
    return result_string

def user_input_pokemon_type(message):
    flag = True
    while flag:
        try:
            user_input = input(f"Ingrese el tipo de Pokemon que desea buscar ({message}): ")
            flag = False
        except ValueError as err:
            print("Dato invalido. Intente otra vez.")
            flag = True
    return user_input

def find_pokemon_by_type(user_option, pokemon_data_list):
    result_list = []
    for i in range(len(pokemon_data_list)):
        if pokemon_data_list[i]['type'].lower() == user_option.lower():
                result_list.append(pokemon_data_list[i]['name'])
    return result_list
    
def print_pokemon_by_type(data_list, pokemon_type):
    print(f"Los Pokemones que existen del tipo '{pokemon_type}' son: ")
    for i in range(len(data_list)):
        print(f"{i+1}. {data_list[i]}")

def main():
    print("---- EJERCICIOS EXTRA DE MANEJO DE JSON - 2")
    print("Ver Pokemones por tipo \n")
    read_json_file = pokemon_data('pokemon.json')
    if read_json_file != None:
        user_selection = user_input_pokemon_type(list_to_string(pokemon_list_of_types(read_json_file)))
        print_pokemon_by_type(find_pokemon_by_type(user_selection,read_json_file), user_selection)

if __name__ == '__main__':
    main()