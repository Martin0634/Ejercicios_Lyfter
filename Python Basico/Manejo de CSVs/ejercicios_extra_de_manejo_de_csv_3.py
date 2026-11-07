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

def count_genres(data_list):
    try:
        result_list = [0]
        result_list[0] = data_list[1][1]
        count = 0
        for i in range(2,len(data_list)):
            if data_list[i][1] not in result_list:
                result_list.append(data_list[i][1])
        for j in range(len(result_list)):
            count = 0
            for k in range(1,len(data_list)):
                if data_list[k][1] == result_list[j]:
                    count += 1
            print(f"{result_list[j]}: {count}")
    except IndexError as err:
        print("No se tienen datos. Verifique que el archivo de datos contenga informacion.")

def main():
    print("---- EJERCICIOS EXTRA DE ARCHIVOS CSV - 3 ----")
    file_games_data = read_csv_file('videogames_data.csv')
    if file_games_data != None:
        count_genres(file_games_data)

if __name__ == '__main__':
    main()
