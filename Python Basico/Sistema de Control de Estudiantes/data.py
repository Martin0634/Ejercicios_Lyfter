import csv
from constants import PATH, HEADERS

#read CSV file
def read_student_data_file():
    try:
        with open(PATH, 'r', encoding="utf-8") as file:
            student_data = csv.reader(file)
            students_data_list = []
            for i in student_data:
                students_data_list.append(i)
        if len(students_data_list) < 2:
            print("The data file is empty. Add a student.\n")
        if len(students_data_list) == 0:
            with open(PATH, 'w', encoding="utf-8", newline="") as file:
                writer = csv.DictWriter(file, fieldnames=HEADERS)
                writer.writeheader()
        return students_data_list
    except FileNotFoundError as err:
        print(f"File {PATH} not found.")

#write data to CSV file
def add_student_data_to_csv_file(data_list):
    try:
        with open(PATH, 'x', encoding="utf-8", newline="") as file:
            writer = csv.DictWriter(file, fieldnames=HEADERS)
            writer.writeheader()
            writer.writerows(data_list)
            print("New file created.")
    except FileExistsError as err:
            with open(PATH, 'a', encoding='utf-8', newline='') as file:
                writer = csv.DictWriter(file, fieldnames=HEADERS)
                writer.writerows(data_list)
                print("Data on file updated.")

#writes new data list after deletion
def write_data_list_to_csv(data_list):
    try:
        with open(PATH,'w',encoding="utf-8", newline="") as file:
            writer = csv.writer(file)
            writer.writerows(data_list)
    except FileNotFoundError as err:
        print(f"File {PATH} not found.")

#print students data
def print_students_data(data_list):
    print("LIST OF ALL STUDENTS")
    print("--------------------\n\n")
    for i in range(1,len(data_list)):
        print(f"Student {i}:\n")
        for headers in range(len(HEADERS)):
            print (f"{data_list[0][headers]}: {data_list[i][headers]}")
        print("\n")
    enter_hold()

def grade_avg_data(data_list, flag):
    grade_avg_data_list = []
    if len(data_list) > 1:
        for i in range(1,len(data_list)):
            total_grades = 0
            for j in range(2,6):
                total_grades += int(data_list[i][j])
            grade_avg = total_grades / 4
            grade_avg_data_list.append([grade_avg, data_list[i][0]])
            grade_avg_data_list_sorted = sorted(grade_avg_data_list, key=lambda x: x[0], reverse=True)
        if flag == 0:
            print("\nSTUDENT'S AVERAGE GRADE")
            print("-----------------------\n")
            print("Name: Avg. Grade")
            for k in range(len(grade_avg_data_list)):
                print (f"{grade_avg_data_list[k][1]}: {grade_avg_data_list[k][0]}")
            print("")
            enter_hold()
        if flag == 3:
            print("\nTOP-3 AVERAGE GRADES")
            print("--------------------\n")
            print("Name: Avg. Grade")
            if len(grade_avg_data_list_sorted) == 1:
                length = -2
            elif len(grade_avg_data_list_sorted) == 2:
                length = -3
            elif len(grade_avg_data_list_sorted) >= 3:
                length = -4
            for k in range(-1,length,-1):
                print (f"{k*(-1)}. {sorted(grade_avg_data_list_sorted)[k][1]}: {sorted(grade_avg_data_list_sorted)[k][0]}")
            print("")
            enter_hold()

def student_exists(data_list,name,section):
    student_found = False
    for i in range(1,len(data_list)):
        if data_list[i][0].lower() == name.lower() and data_list[i][1].lower() == section.lower():
            student_found = True
    return student_found
        

def delete_student_data(data_list,name,section):
    for i in range(1,len(data_list)):
        if data_list[i][0].lower() == name.lower() and data_list[i][1].lower() == section.lower():
            data_list.pop(i)
            flag_deletion = True
            break
        else:
            flag_deletion = False
    if flag_deletion:
        write_data_list_to_csv(data_list)
        print("Data successfully deleted.\n")
        enter_hold()
    else:
        print("Data could not be deleted.\n")
        enter_hold()

def enter_hold():
    input("PRESS 'ENTER' TO CONTINUE")