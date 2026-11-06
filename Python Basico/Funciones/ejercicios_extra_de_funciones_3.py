def count_vowel(string):
    count = 0
    for char in string.lower():
        if char == 'a' or char == 'e' or char == 'i' or char == 'o' or char == 'u':
            count += 1
    return count

print("---- EJERCICIOS DE EXTRA DE FUNCIONES - 3")

user_string = input("Escriba una palabra o frase: ")
print(f"La frase '{user_string}' tiene {count_vowel(user_string)} vocales.")