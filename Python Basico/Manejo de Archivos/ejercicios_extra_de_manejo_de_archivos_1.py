def read_file_lines(path):
    try:
        with open(path, 'r', encoding="utf-8") as file:
            content = file.read().splitlines()
        return content
    except FileNotFoundError as err:
        print(f"No se encontro el archivo '{path}'")

def list_to_string(data_list):
    new_string = data_list[0]
    for i in range(1,len(data_list)):
        new_string += " " + data_list[i]
    return new_string

def write_string_to_file(path,string_text):
    try:
        with open(path, 'x', encoding="utf-8") as file:
            file.write(string_text)
        print("Archivo nuevo creado.")
    except:
        with open(path, 'w', encoding="utf-8") as file:
            file.write(string_text)
        print("Archivo sobreescrito.")

def main():
    print("---- EJERCICIOS EXTRA DE ARCHIVOS - 1")
    file_content = read_file_lines('multiline_text_file.txt')
    if file_content != None:
        write_string_to_file('single_line_file.txt',list_to_string(file_content))

if __name__ == '__main__':
    main()