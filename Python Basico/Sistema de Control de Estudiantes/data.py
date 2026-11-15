import csv
from actions import enter_hold
from constants import PATH, HEADERS

#read CSV file
def read_student_data_file():
    try:
        with open(PATH, 'r', encoding="utf-8") as file:
            student_data = csv.DictReader(file)
            students_data_list = []
            for i in student_data:
                students_data_list.append(i)
        return students_data_list
    except FileNotFoundError as err:
        print(f"File '{PATH}' not found.")
        enter_hold()

#writes data list to CSV file
def write_data_list_to_csv(data_list):
    try:
        with open(PATH,'w',encoding="utf-8", newline="") as file:
            writer = csv.DictWriter(file, fieldnames=HEADERS)
            writer.writeheader()
            writer.writerows(data_list)
            print("Data exported to CSV file.")
            enter_hold()
    except FileNotFoundError as err:
        print(f"File '{PATH}' not found.")
        enter_hold()