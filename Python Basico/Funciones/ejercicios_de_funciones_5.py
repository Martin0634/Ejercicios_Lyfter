def count_uppercase_lowercase(string):
    count_uppercase = 0
    count_lowercase = 0
    count_special = 0
    for char in range(len(string)):
        if not string[char].isspace():
            if string[char].isupper():
                count_uppercase += 1
            elif string[char].islower():
                count_lowercase += 1
            else:
                count_special +=1
    if count_special == 0:
        print(f"La frase tiene {count_uppercase} mayusculas y {count_lowercase} minusculas. ")
    else:
        print(f"La frase tiene {count_uppercase} mayusculas, {count_lowercase} minusculas y {count_special} caracteres espciales. ")

print("---- EJERCICIOS DE FUNCIONES - 5")

user_string = input("Escriba una frase: ")
count_uppercase_lowercase(user_string)