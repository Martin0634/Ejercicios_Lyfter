print("---- EJERCICIOS EXTRA DE DICCIONARIOS - 2")

employees = [
    {"name": "Carlos", "email": "carlos@empresa.com", "department": "ventas"},
    {"name": "Ana", "email": "ana@empresa.com", "department": "TI"},
    {"name": "Luis", "email": "luis@empresa.com", "department": "ventas"},
    {"name": "Sofia", "email": "sofia@empresa.com", "department": "RRHH"},
]

employees_by_department = {}

for i in range(len(employees)):
    if employees[i].get('department') not in employees_by_department:
        employees_by_department[employees[i].get('department')] = []
    employees_by_department[employees[i].get('department')].append(employees[i])

for i,j in employees_by_department.items():
    print(f"{i} - {j}")
    