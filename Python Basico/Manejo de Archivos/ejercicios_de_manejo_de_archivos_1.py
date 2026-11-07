def read_file_by_lines(path):
    try:
        with open(path, 'r') as file:
            content = file.readlines()
        for i in range(len(content)):
            content[i] = content[i].strip()
        return content
    except FileNotFoundError as err:
        print(f"El archivo {path} no existe.")
    
def sort_list_alphabetically(data_list):    
    data_list.sort(key=str.lower)
    return data_list

def write_to_file(path,content):
    try:
        with open(path, 'w', encoding='utf-8') as file:
            for i in range(len(content)):
                if i != 0:
                    file.write("\n" + content[i])
                else:
                    file.write(content[i])
            print("Archivo nuevo creado.")
    except FileNotFoundError as err:
        print(f"No se encontro el archivo {path}")

def main():
    print("---- EJERCICIOS DE ARCHIVOS - 1")
    sorted_list = sort_list_alphabetically(read_file_by_lines('song_names.txt'))
    write_to_file('sorted_song_names.txt', sorted_list)

if __name__ == '__main__':
    main()