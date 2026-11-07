def my_function ():
    function_variable = 10
    #total = 0 # Si previamente decalro la variable local, solo tiene ese valor dentro de la funcion
    total = total + function_variable #Intentar acceder a una variable local desde una funcion. UnboundLocalError
    print(f"Variable local es: {function_variable}")
    global global_variable
    global_variable += function_variable

print("---- EJERCICIOS DE FUNCIONES - 2")

global_variable = 5
global_variable_2 = 7
total = 0
#total = total + function_variable intentar acceder a una variable local. variable no esta definida.

print(f"Valor antes de la funcion: {global_variable}")
my_function()
print(f"Ahora le sumo el valor de una variable global. Valor despues de la funcion: {global_variable}")
print(f"Esta variable global tiene este valor: {global_variable_2}")
print(f"Ahora intento sumarle el valor de una variable local de una funcion y no se puede ")
print(total)