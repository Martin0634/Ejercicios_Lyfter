import csv
from actions import enter_hold
from constants import PATH
from classes import Student

#read CSV file
def read_student_data_file():
    try:
        with open(PATH, 'r', encoding='utf-8') as file:
            student_data = csv.DictReader(file)
            for student in student_data:
                new_student = Student(
                    student[student_data.fieldnames[0]],
                    student[student_data.fieldnames[1]],
                    student[student_data.fieldnames[2]],
                    student[student_data.fieldnames[3]],
                    student[student_data.fieldnames[4]],
                    student[student_data.fieldnames[5]]
                    )
                new_student.add_verified_student()
        return Student.students_data_list
    except FileNotFoundError as err:
        print(f"File '{PATH}' not found")
        enter_hold()

#writes data list to CSV file
def write_data_list_to_csv():
    try:
        with open(PATH,'w',encoding="utf-8", newline="") as file:
            dict_data_list = Student.to_dict()
            headers = list(dict_data_list[0].keys())
            writer = csv.DictWriter(file, fieldnames=headers)
            writer.writeheader()
            writer.writerows(dict_data_list)
            print("Data exported to CSV file.")
    except FileNotFoundError as err:
        print(f"File '{PATH}' not found.")