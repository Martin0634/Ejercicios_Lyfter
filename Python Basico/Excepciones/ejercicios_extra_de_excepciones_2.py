def list_to_integer(user_list):
    print("RESULTADO")
    for i in range(len(user_list)):
        try:
            print(f"{user_list[i]} convertido a {int(user_list[i])}")
        except ValueError as err:
            print(f"No su pudo convertir el elemento: {user_list[i]}")
    return user_list

print("---- EJERCICIOS EXTRA DE EXCEPCIONES - 2 ----")
my_list = ['4','hola','10','5.2']
list_to_integer(my_list)
