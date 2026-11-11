import csv

def read_csv_file(path):
    try:
        with open(path, 'r', encoding='utf-8') as file:
            data = csv.reader(file)
            data_list = []
            for i in data:
                data_list.append(i)
            for info in range(1,len(data_list)):
                for headers in range(len(data_list[0])):
                    print(f"{data_list[0][headers]}: {data_list[info][headers]}")
                print("")
    except FileNotFoundError as err:
        print("No se encontro el archivo.")
def main():
    print("---- EJERCICIOS EXTRA DE ARCHIVOS CSV - 1 ----")
    read_csv_file('videogames_data.csv')

if __name__ == '__main__':
    main()
