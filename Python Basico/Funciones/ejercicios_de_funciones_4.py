def upside_down_string (string_variable):
    new_string = ''
    for char in range(len(string_variable)-1,-1,-1):
        new_string += string_variable[char]
    return new_string

print("---- EJERCICIOS DE FUNCIONES - 4")

user_char = input("Escriba una palabra o frase: ")
print(upside_down_string(user_char))