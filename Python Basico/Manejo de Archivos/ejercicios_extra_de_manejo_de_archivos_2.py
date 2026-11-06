def count_words_on_file(path):
    count = 1
    try:
        with open(path, 'r') as file:
            content = file.read()
        for i in content:
            if i == " " or i == "\n":
                count += 1
        return count
    except FileNotFoundError as err:
        print("No se encontro el archivo")

def main():
    print("---- EJERCICIOS EXTRA DE ARCHIVOS - 2")
    result_word_count = count_words_on_file('random_text_file_.txt')
    if result_word_count != None:
        print(f"El archivo tiene {result_word_count} palabras.")

if __name__ == '__main__' :
    main()