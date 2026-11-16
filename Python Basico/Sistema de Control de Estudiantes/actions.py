from constants import HEADERS
import re

#checks if file exists but has no data
def data_list_validation(data_list):
    if not data_list:
        print("Data file not exported. Add students and export file.")
    else:
        if len(data_list) < 2:
            print("No data on file. Add a student.")
        else:
            print("Data imported from file.")
    enter_hold()
    return True

#validates the number of new students to be added
def validate_new_student_qty(students_data_qty):
    if students_data_qty <= 0:
        return students_data_qty
    if students_data_qty > 30:
        return students_data_qty
    else:
        if students_data_qty == 1:
            print(f"{students_data_qty} student will be added.")
        else:
            print(f"{students_data_qty} students will be added one by one.\n")
        return students_data_qty

#user inputs name
def get_name():
    flag = True
    while flag:
        try:
            student_name = is_valid_name(input("Full Name: "))
            if student_name == 0:
                raise ValueError("Full Name can not be empty.")
            elif student_name == 1:
                raise ValueError("Full name can not contain numbers.")
            else:
                flag = False
            return student_name
        except ValueError as err:
            print(err)

#user inputs section
def get_section():
    flag_section = True
    while flag_section:
        try:
            student_section = input("Section: ")
            if len(student_section) != 3:
                raise ValueError("Enter a valid section format. Ex: 10A")
            elif not student_section[0].isdigit():
                raise ValueError("Section first digit must be a number. Ex: 10A")
            elif not student_section[1].isdigit():
                raise ValueError("Section second digit must be a number. Ex: 10A")
            elif not student_section[2].isalpha():
                raise ValueError("Section third digit must be a letter. Ex: 10A")
            else:
                flag_section = False
                return student_section.upper()
        except ValueError as err:
            print(err) 

#user inputs grades
def get_grades(index):
    flag_grades = True
    while flag_grades:
        try:
            student_grade = int(input(f"{HEADERS[index]}: "))
            if student_grade > 100 or student_grade < 0:
                raise ValueError("Grades must be a number between 0-100.")
            else:
                flag_grades = False
                return student_grade
        except ValueError as err:
            print(err)

#collects student data and returns as Dict
def receiving_student_data():
    new_student = {}
    new_student[HEADERS[0]] = get_name()
    new_student[HEADERS[1]] = get_section()
    for i in range(2,len(HEADERS)):
        new_student[HEADERS[i]] = get_grades(i)
    return new_student

#add new students data to data list
def add_student_info(data_list):
    #asking a number of students to add
    flag = True
    while flag:
        try:
            students_data_qty = int(input("How many students do you want to add?: "))
            #validate user input
            validate_qty = validate_new_student_qty(students_data_qty)
            if validate_qty == 0:
                raise ValueError("Please enter a number greater than zero.")
            elif validate_qty > 30:
                raise ValueError("You can add up to 30 students at a time.")
            else:
                flag = False
        except ValueError as err:
            print(err)
    
    #receiving student data
    new_student_data = []
    for i in range(students_data_qty):
        new_student = receiving_student_data()
        if not new_student_data:
            new_student_data.append(new_student)
        else:
            #validating duplicate student entered
            if student_exists(new_student_data, new_student[HEADERS[0]], new_student[HEADERS[1]]):
                print(f"\nStudent name: {new_student[HEADERS[0]]} in section {new_student[HEADERS[1]]} already entered.")
            else:
                new_student_data.append(new_student)
    
    #validating existing students registered
    new_student_data_verified = []
    students_data_qty = 0
    for i in range(len(new_student_data)):
        if data_list:
            if student_exists(data_list, new_student_data[i][HEADERS[0]], new_student_data[i][HEADERS[1]]):
                print(f"\nStudent name {new_student_data[i][HEADERS[0]]} in section {new_student_data[i][HEADERS[1]]} already registered.")
            else:
                new_student_data_verified.append(new_student_data[i])
                students_data_qty += 1
    
    #adding new student to Data List
    if students_data_qty > 0:
        new_data_list = add_new_students_to_data_list(data_list, new_student_data_verified)
        if students_data_qty == 1:
            print(f"\n{students_data_qty} student added")
        else:
            print(f"\n{students_data_qty} students added")
    else:
        print("\nNo students added")
        new_data_list = data_list
    enter_hold()
    return new_data_list

#adds new students to data list
def add_new_students_to_data_list(data_list, new_students_list):
    if not data_list:
        data_list = []
    for i in new_students_list:
        data_list.append(i)
    return data_list

#checks duplicate students
def student_exists(data_list,name,section):
    student_found = False
    for i in range(len(data_list)):
        if data_list[i][HEADERS[0]].lower() == name.lower() and data_list[i][HEADERS[1]].lower() == section.lower():
            student_found = True
    return student_found

#print all students data
def show_all_students_data(data_list):
    #students_data = read_student_data_file()
    if data_list:
        print_students_data(data_list)
    else:
        print("No data to print.")
        enter_hold()

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
def show_all_students_grade_avg(data_list, flag):
    if data_list:
        #print top-3 students average grades
        if flag == 'top3':
            grade_avg_data(data_list, 3)
        else:
            #print all students average grades
            grade_avg_data(data_list, 0)
    else:
        print("No data to print.")
        enter_hold()

#print students average grades
def grade_avg_data(data_list, flag):
    grade_avg_data_list = []
    if len(data_list) >= 1:
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

#validates name
def is_valid_name(name):
    if len(name) == 0:
        return 0
    else:
        count_digits = 0
        for i in name:
            if i.isdigit():
                count_digits += 1
        if count_digits > 0:
            return 1
        else:
            return name

#validates section
def is_valid_section(section):
    if len(section) != 3:
        return 0
    elif not section[0].isdigit():
        return 1
    elif not section[1].isdigit():
        return 2
    elif not section[2].isalpha():
        return 3
    else:
        return 4

#removes student data from data list
def delete_student(data_list):
    if data_list:
        print("Enter student's name and section to delete.")
        delete_student_name = get_name()
        delete_student_section = get_section()
        flag_student_exists = student_exists(data_list,delete_student_name,delete_student_section)
        if  flag_student_exists:
            flag_confirmation = True
            while flag_confirmation:
                try:
                    user_confirmation = input("Student found. Are you sure you want to continue? (y/n): ")
                    if user_confirmation != 'y' and user_confirmation != 'n' and user_confirmation != 'Y' and user_confirmation != 'N':
                        raise ValueError("Chose only Yes or No (y/n)")
                    elif user_confirmation == 'y' or user_confirmation == 'Y':
                        delete_student_data(data_list, delete_student_name, delete_student_section)
                        flag_confirmation = False
                    else:
                        break
                except ValueError as err:
                    print(err)
        else:
            print("Student's name and section combination not found.")
            enter_hold()
    else:
        print("Empty data list.")
        enter_hold()

#removes student data from data list
def delete_student_data(data_list,name,section):
    for i in range(len(data_list)):
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

#selects failed students
def select_failed_students(data_list):
    if data_list:
        failed_students_list = []
        for i in range(len(data_list)):
            failed_flag = False
            for grades in range(2,len(HEADERS)):
                if int(data_list[i][HEADERS[grades]]) < 60:
                    failed_flag = True
            if failed_flag:
                failed_students_list.append(data_list[i])
        if len(failed_students_list) == 0:
            print("No failed students.")
            enter_hold()
        else:
            print_failed_students(failed_students_list)
    else:
        print("No data to print.")
        enter_hold()

#prints failed students
def print_failed_students(data_list):
    print("\nFAILED STUDENTS")
    print("---------------\n")
    for i in range(len(data_list)):
        print(f"{HEADERS[0]}: {data_list[i][HEADERS[0]]}")
        print(f"{HEADERS[1]}: {data_list[i][HEADERS[1]]}")
        print("Failed subjects:")
        for grades in range(2,len(HEADERS)):
            if int(data_list[i][HEADERS[grades]]) < 60:
                print(f"{HEADERS[grades]}: {data_list[i][HEADERS[grades]]}")
        print("")
    enter_hold()
    
#waits for the user to hit ENTER key
def enter_hold():
    input("PRESS 'ENTER' TO CONTINUE")