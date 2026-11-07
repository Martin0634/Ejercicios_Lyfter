first_name = "Martin"
last_name = "Zeta"
age = 44
yob = 1982
height = 1.74
weight = 85.5
logged = True
active = False
sports = ["futbol", "basquet", "voley"]
social = ["Facebook", "X", "Instagram"]

#Prueba de sumas entre diferentes tipos de datos
#string + string -> MartinZeta
print(first_name + last_name)

#string + int -> TypeError: can only concatenate str (not "int") to str
#print(first_name + age)

#int + string -> TypeError: unsupported operand type(s) for +: 'int' and 'str'
#print(yob + last_name)

#list + list -> ['futbol', 'basquet', 'voley', 'Facebook', 'X', 'Instagram']
print(sports + social)

#string + list -> TypeError: can only concatenate str (not "list") to str
#print(first_name + sports)

#float + int -> 45.74
print(height + age)

#bool + bool -> 1
print(logged + active)
