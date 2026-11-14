import csv
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
        print(f"File {PATH} not found.")

#checks if file exists but has no data
def data_list_validation(data_list):
    if len(data_list) < 2:
        print("No data imported. Add a student.")
    else:
        print("Data imported from file.")
    enter_hold()
    return True

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
        print(f"File {PATH} not found.")

#adds new students to data list
def add_new_students_to_data_list(data_list, new_students_list):
    for i in new_students_list:
        data_list.append(i)
    return data_list

#print students data
def print_students_data(data_list):
    print("LIST OF ALL STUDENTS")
    print("--------------------\n\n")
    for i in range(len(data_list)):
        print(f"Student {i+1}:\n")
        for headers in HEADERS:
            print (f"{headers}: {data_list[i][headers]}")
        print("\n")
    enter_hold()

#print students average grades
def grade_avg_data(data_list, flag):
    grade_avg_data_list = []
    if len(data_list) > 1:
        all_student_grades = 0
        for i in range(len(data_list)):
            total_grades = 0
            for j in range(2,6):
                total_grades += int(data_list[i][HEADERS[j]])
            grade_avg = total_grades / 4
            all_student_grades += total_grades
            grade_avg_data_list.append([grade_avg, data_list[i][HEADERS[0]]])
            grade_avg_data_list_sorted = sorted(grade_avg_data_list, key=lambda x: x[0], reverse=True)
        all_student_grade_avg = all_student_grades / (len(data_list)*4)
        if flag == 0:
            print("\nSTUDENT'S AVERAGE GRADE")
            print("-----------------------\n")
            print(f"General Average Grade: {round(all_student_grade_avg,2)}\n")
            print("Individual student average grade: \n")
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

#checks duplicate students
def student_exists(data_list,name,section):
    student_found = False
    for i in range(len(data_list)):
        if data_list[i][HEADERS[0]].lower() == name.lower() and data_list[i][HEADERS[1]].lower() == section.lower():
            student_found = True
    return student_found

#removes student data from data list
def delete_student_data(data_list,name,section):
    for i in range(1,len(data_list)):
        if data_list[i][HEADERS[0]].lower() == name.lower() and data_list[i][HEADERS[1]].lower() == section.lower():
            data_list.pop(i)
            flag_deletion = True
            break
        else:
            flag_deletion = False
    if flag_deletion:
        print("Data successfully deleted.\n")
    else:
        print("Data could not be deleted.\n")
    enter_hold()

#waits for the user to hit ENTER key
def enter_hold():
    input("PRESS 'ENTER' TO CONTINUE")