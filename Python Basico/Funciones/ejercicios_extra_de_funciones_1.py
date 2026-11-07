def count_char_in_word (string, char):
    count_char = 0
    string = string.lower()
    char = char.lower()
    for i in string:
        if i == char:
            count_char += 1
    return count_char

print("---- EJERCICIOS DE EXTRA DE FUNCIONES - 1")

user_word = input("Escriba una palabra: ");
user_char = input("Escriba una letra a contar: ")
print(f"La letra '{user_char}' aparece {count_char_in_word(user_word,user_char)} veces en {user_word}")