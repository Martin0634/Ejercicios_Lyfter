def read_file_by_line(path):
    try:
        with open(path, 'r', encoding="utf-8") as file:
            content = file.readlines()
        for i in range(len(content)):
            content[i] = content[i].strip()
        return content
    except FileNotFoundError as err:
        print(f"Archivo {path} no encontrado.")

def to_uppercase(list):
    for i in range(len(list)):
        list[i] = list[i].upper()
    return list

def write_file(path,content):
    try:
        with open(path, 'x', encoding='utf-8') as file:
            for i in range(len(content)):
                if i == len(content)-1:
                    file.write(content[i])
                else:
                    file.write(content[i] + "\n")
        print("Archivo nuevo creado.")
    except FileExistsError as err:
        with open(path, 'w', encoding="utf-8") as file:
            for i in range(len(content)):
                if i == len(content)-1:
                    file.write(content[i])
                else:
                    file.write(content[i] + "\n")
        print("Archivo sobreescito.")

def main():
    print("---- EJERCICIOS EXTRA DE ARCHIVOS - 3")
    file_content = read_file_by_line('multiline_lower.txt')
    if file_content != None:
        file_content_uppercase = to_uppercase(file_content)
        write_file('multiline_upper.txt',file_content_uppercase)

if __name__ == '__main__':
    main()