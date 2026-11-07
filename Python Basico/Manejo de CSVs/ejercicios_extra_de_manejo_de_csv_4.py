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
        print(f"El archivo de datos '{path}' no existe.")

def developer_count (data_list):
    try:
        input_flag = True
        while input_flag:
            try:
                user_option = input("Escriba un desarrollador: ")
                input_flag = False
            except ValueError as err:
                print(err)
        result_data = []
        for i in range(1,len(data_list)):
            if data_list[i][2].lower() == user_option.lower():
                result_data.append(data_list[i])
        if len(result_data) > 0:
            print(f"Videojuegos desarrolados por {user_option}:")
            for j in range(len(result_data)):
                print(f"- {result_data[j][0]} (Clasificacion: {result_data[j][3]}, Genero: {result_data[j][1]})")
        else:
            print(f"No se encontraron juegos por el desarrolador {user_option}")
    except IndexError as err:
        print("El archivo de datos no contiene informacion.")

def main():
    print("---- EJERCICIOS EXTRA DE ARCHIVOS CSV - 4 ----")
    file_games_data = read_csv_file('videogames_data.csv')
    if file_games_data != None:
        developer_count(file_games_data)

if __name__ == '__main__':
    main()