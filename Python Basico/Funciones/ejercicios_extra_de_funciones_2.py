def words_new_list(list,user_number):
    n_digit_word_list = []
    for i in range(len(list)):
        if len(list[i]) >= int(user_number):
            n_digit_word_list.append(list[i])
    if not n_digit_word_list:
        return 'No se encontraron elementos'
    else:
        return n_digit_word_list

print("---- EJERCICIOS DE EXTRA DE FUNCIONES - 2")

my_list = ['cielo', 'sol', 'maravilloso', 'dia']
char_number = input("Digite el numero de letras: ")
print(words_new_list(my_list,char_number))