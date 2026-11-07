def options_menu():
    user_option = 0
    current_number = 0
    menu_operations = ['Suma', 'Resta', 'Multiplicacion', 'Division', 'Borrar Resultado', 'Salir']
    while user_option != 6:
        print("---- MENU DE OPCIONES ----")
        for index,options in enumerate(menu_operations):
            print (index+1,options)
        print(f"Numero actual: {round(current_number,2)}")
        
        user_option = validate_user_option()
    
        if user_option == 1:
            current_number = addition_operation(current_number)
    
        if user_option == 2:
            current_number = subtraction_operation(current_number)
    
        if user_option == 3:
            current_number = multiplication_operation(current_number)
    
        if user_option == 4:
            current_number = division_operation(current_number)
    
        if user_option == 5:
            current_number = clear_current_number()
        
        if user_option == 6:
            end_calculator()

def validate_user_option():
    try:
        user_option = int(input("Elija una opcion: "))
        if user_option < 1 or user_option > 6:
            raise ValueError("Debe elegir una opcion del menu")
    except ValueError as err:
            user_option = 0
            print("Opcion invalida. Debe elegir una opcion del menu.")
    return user_option

def addition_operation(current_number):
    flag = True
    while flag:
        try:
            new_number = int(input("Digite el numero para sumar: "))
            current_number += new_number
            flag = False
        except ValueError as err:
            print("Mensaje del sistema: Debe digitar un numero.")
            flag = True
    return current_number

def subtraction_operation(current_number):
    flag = True
    while flag:
        try:
            new_number = int(input("Digite el numero para restar: "))
            current_number -= new_number
            flag = False
        except ValueError as err:
            print("Mensaje del sistema: Debe digitar un numero.")
            flag = True
    return current_number

def multiplication_operation(current_number):
    flag = True
    while flag:
        try:
            new_number = int(input("Digite el numero para multiplicar: "))
            current_number *= new_number
            flag = False
        except ValueError as err:
            print("Mensaje del sistema: Debe digitar un numero.")
            flag = True
    return current_number

def division_operation(current_number):
    flag = True
    while flag:
        try:
            new_number = int(input("Digite el numero para dividir: "))
            current_number /= new_number
            flag = False
        except ValueError as err:
            print("Mensaje del sistema: Debe digitar un numero.")
            flag = True
        except ZeroDivisionError as err:
            print("Mensaje del sistema: No se puede dividir por 0.")
            flag = True
    return current_number

def clear_current_number():
    current_number = 0
    return current_number

def end_calculator():
    print("Hasta pronto!")

def main():
    options_menu()

main ()