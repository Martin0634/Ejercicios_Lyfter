import csv

def read_csv_file(path):
    try:
        with open(path, 'r', encoding='utf-8') as file:
            data = csv.reader(file)
            data_list = []
            for i in data:
                data_list.append(i)
        return data_list
    except FileNotFoundError as err:
        print(f"No se encontro el archivo '{path}'")

def search_rating(data_list, rating):
    result_list = []
    result_list.append(data_list[0])
    for i in range(1, len(data_list)):
        if data_list[i][3] == rating.upper():
            result_list.append(data_list[i])
    return result_list

def print_data_list(data_list):
    if len(data_list) == 1:
        print("No se encontraron juegos con esa calificacion")
    else:
        for i in range(1,len(data_list)):
            for headers in range(len(data_list[0])):
                print(f"{data_list[0][headers]}: {data_list[i][headers]}")
            print(" ")

def main():
    print("---- EJERCICIOS EXTRA DE ARCHIVOS CSV - 2 ----")
    file_data_list = read_csv_file('videogames_data.csv')
    if file_data_list != None:
        user_option = input("Ingrese la calificacion a buscar: ")
        print_data_list(search_rating(file_data_list,user_option))

if __name__ == '__main__':
    main()