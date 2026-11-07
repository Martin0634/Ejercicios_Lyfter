print("---- EJERCICIO DE SINTAXIS - 5")

name = input("Nombre del estudiante: ")
grades = int(input("Cuántas materias registradas?: "))
passed = 0
failed = 0
total_passed = 0
total_failed = 0
avg_passed = 0
avg_failed = 0
total = 0

for grade in range(1,grades+1):
    grade = int(input(f"Ingrese la nota {grade}: "))
    total += grade
    if grade > 70:
        passed += 1
        total_passed += grade
    else:
        failed += 1
        total_failed += grade

print(f"{name} tomó {grades} materias con un promedio de: {round(total / grades,2)}")
if total_passed != 0:
    avg_passed = round(total_passed / passed,2)
    print(f"{name} aprobó {passed} materias con un promedio de: {avg_passed}")
else:
    print(f"{name} no tiene materias aprobadas")
if total_failed != 0:
    avg_failed = round(total_failed / failed,2)
    print(f"{name} reprobó {failed} materias con un promedio de: {avg_failed}")
else:
    print(f"{name} no tiene materias reprobadas")



