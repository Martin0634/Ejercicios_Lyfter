import csv
from actions import enter_hold
from constants import PATH, HEADERS
from classes import Student, RegisteredStudent

#read CSV file
#def read_student_data_file():
#    try:
#        with open(PATH, 'r', encoding="utf-8") as file:
#            student_data = csv.DictReader(file)
#            students_data_list = []
#            for i in student_data:
#                students_data_list.append(i)
#        return students_data_list
#    except FileNotFoundError as err:
#        print(f"File '{PATH}' not found.")
#        enter_hold()

#read CSV file
def read_student_data_file():
    try:
        with open(PATH, 'r', encoding='utf-8') as file:
            student_data = csv.DictReader(file)
            students_data_list = []
            for i in student_data:
                new_student = RegisteredStudent(Student(i[HEADERS[0]], i[HEADERS[1]], i[HEADERS[2]], i[HEADERS[3]], i[HEADERS[4]], i[HEADERS[5]] ))
                new_student.add_verified_student()
        return RegisteredStudent.students_data_list
    except FileNotFoundError as err:
        print(f"File '{PATH}' not found")
        enter_hold()

#writes data list to CSV file
def write_data_list_to_csv(data_list):
    try:
        with open(PATH,'w',encoding="utf-8", newline="") as file:
            dict_data_list = []
            for i in data_list:
                index = 0
                dict_data = {}
                for values in i.__dict__.values():
                    dict_data[HEADERS[index]] = values
                    index += 1
                dict_data_list.append(dict_data)
            writer = csv.DictWriter(file, fieldnames=HEADERS)
            writer.writeheader()
            writer.writerows(dict_data_list)
            print("Data exported to CSV file.")
    except FileNotFoundError as err:
        print(f"File '{PATH}' not found.")