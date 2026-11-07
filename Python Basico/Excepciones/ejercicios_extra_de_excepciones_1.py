def get_user_info():
    name_status_ok = False
    while not name_status_ok:
        try:
            user_name = input("Escriba su nombre: ")
            name_status_ok = True
            #validate name is not a number
            if user_name.isdigit():
                name_status_ok = False
                raise ValueError ("El nombre no puede ser un numero. Intente nuevamente.")
            #validate name's length
            if len(user_name) < 3:
                name_status_ok = False
                raise ValueError ("Nombre muy corto. Intente nuevamente.")
        except ValueError as err:
            name_status_ok = False
            print(err)
    
    age_status_ok = False
    while not age_status_ok:
        try:
            user_age = int(input("Digite su edad: "))
            age_status_ok = True
        except ValueError as err:
            age_status_ok = False
            print("Dato no valido. Intente nuevamente.")
    
    user_info_list = [user_name,user_age]
    return user_info_list

print("---- EJERCICIOS EXTRA DE EXCEPCIONES - 1 ----")
user_data = get_user_info()
print(f"Hola {user_data[0]}, usted tiene {user_data[1]} años")    