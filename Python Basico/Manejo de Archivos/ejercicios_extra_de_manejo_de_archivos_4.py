def write_user_string_to_file(path, user_string):
    try:
        with open(path, 'x') as file:
            file.write(user_string)
        print("Archivo creado y linea agregada.")
    except:
        with open(path, 'a') as file:
                file.write("\n" + user_string)
        print("Linea agregada al archivo.")

def user_input_string():
    flag = True
    while flag:
        try:
            user_string = input("Escriba una frase: ")
            if len(user_string) < 5:
                raise ValueError
            flag = False
            return user_string
        except ValueError as err:
            print("Frase muy corta.")
            flag = True

def main():
    print("---- EJERCICIOS EXTRA DE ARCHIVOS - 3")
    user_phrase = user_input_string()
    write_user_string_to_file('user_strings.txt',user_phrase)

if __name__ == '__main__':
    main()