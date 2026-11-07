print("---- EJERCICIO DE SINTAXIS - 2")

first_name = input("Ingrese su nombre: ")
last_name = input("Ingrese su apellido: ")
age = int(input("ingrese su edad: "))

if age < 2:
    message = "bebe"
elif age < 8:
    message = "niño"
elif age < 13:
    message = "preadolescente"
elif age < 18:
    message = "adolescente"
elif age < 35:
    message = "adulto joven"
elif age < 65:
    message = "adulto"
else:
    message = "adulto mayor"

print(f"{first_name} {last_name}, usted tiene {age} años. Es un {message}")