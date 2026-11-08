from data import add_student_data_to_csv_file, read_student_data_file, print_students_data, grade_avg_data, student_exists, delete_student_data, enter_hold
from constants import HEADERS

def validate_new_student_qty(students_data_qty):
    if students_data_qty <= 0:
        return 0
    if students_data_qty > 30:
        return 'too much'
    else:
        if students_data_qty == 1:
            print(f"{students_data_qty} student will be added.")
        else:
            print(f"{students_data_qty} students will be added one by one.\n")
        return students_data_qty

def receiving_student_data():
    new_student = {}
    flag = True
    while flag:
        try:
            student_name = input("Full Name: ")
            if len(student_name) == 0:
                raise ValueError("Full Name can not be empty.")
            else:
                count_digits = 0
                for i in student_name:
                    if i.isdigit():
                        count_digits += 1
                if count_digits > 0:
                    raise ValueError("Full name can not contain numbers.")
            new_student[HEADERS[0]] = student_name
            flag = False
        except ValueError as err:
            print(err)
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
                new_student[HEADERS[1]] = student_section.upper()
                flag_section = False
        except ValueError as err:
            print(err)    

    for i in range(2,len(HEADERS)):
        flag_grades = True
        while flag_grades:
            try:
                student_grade = int(input(f"{HEADERS[i]}: "))
                if student_grade > 100 or student_grade < 0:
                    raise ValueError("Grades must be a number between 0-100.")
                else:
                    new_student[HEADERS[i]] = student_grade
                    flag_grades = False
            except ValueError as err:
                print(err)
    return new_student

def add_student_info():
    #asking a number of students to add
    flag = True
    while flag:
        try:
            students_data_qty = int(input("How many students do you want to add?: "))
            #validate user input
            validate_qty = validate_new_student_qty(students_data_qty)
            if validate_qty == 0:
                raise ValueError("Please enter a number higher than zero.")
            elif validate_qty == 'too much':
                raise ValueError("You can add up to 30 students at a time.")
            else:
                flag = False
        except ValueError as err:
            print(err)
    
    #receiving student data
    new_student_data = []
    for i in range(students_data_qty):
        new_student_data.append(receiving_student_data())
    
    #validating existing students
    new_student_data_verified = []
    students_data_qty = 0
    students_data = read_student_data_file()
    for i in range(len(new_student_data)):
        if student_exists(students_data, new_student_data[i][HEADERS[0]], new_student_data[i][HEADERS[1]]):
            print(f"\nStudent name {new_student_data[i][HEADERS[0]]} in section {new_student_data[i][HEADERS[1]]} already registered.")
        else:
            new_student_data_verified.append(new_student_data[i])
            students_data_qty += 1
    
    #writing new student to CSV file
    if students_data_qty > 0:
        add_student_data_to_csv_file(new_student_data_verified)
        if students_data_qty == 1:
            print(f"\n{students_data_qty} student added")
        else:
            print(f"\n{students_data_qty} students added")
    else:
        print("\nNo students added")
    enter_hold()

def show_all_students_data():
    students_data = read_student_data_file()
    if students_data is not None:
        print_students_data(students_data)

def show_all_students_grade_avg(flag):
    students_data = read_student_data_file()
    if students_data is not None:
        if flag == 'top3':
            grade_avg_data(students_data, 3)
        else:
            grade_avg_data(students_data, 0)

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
            return 2

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

def delete_student():
    students_data = read_student_data_file()
    if students_data is not None:
        print("Enter student's name and section to delete.")
        flag = True
        while flag:
            try:
                delete_student_name = input("Name: ")
                name_validation = is_valid_name(delete_student_name)
                if name_validation == 0:
                    raise ValueError("Name can not be empty.")
                elif name_validation == 1:
                    raise ValueError("Name can not contain a number.")
                else:
                    flag = False
            except ValueError as err:
                print(err)
        flag = True
        while flag:
            try:
                delete_student_section = input("Section: ")
                if is_valid_section(delete_student_section) == 0:
                    raise ValueError("Enter a valid section format. Ex: 10A")
                elif is_valid_section(delete_student_section) == 1:
                    raise ValueError("Section first digit must be a number.")
                elif is_valid_section(delete_student_section) == 2:
                    raise ValueError("Section second digit must be a number.")
                elif is_valid_section(delete_student_section) == 3:
                    raise ValueError("Section third digit must be a letter.")
                elif is_valid_section(delete_student_section) == 4:
                    flag = False
            except ValueError as err:
                print(err)
        flag_student_exists = student_exists(students_data,delete_student_name,delete_student_section)
        if  flag_student_exists:
            flag_confirmation = True
            while flag_confirmation:
                try:
                    user_confirmation = input("Student found. Are you sure you want to continue? (y/n): ")
                    if user_confirmation != 'y' and user_confirmation != 'n' and user_confirmation != 'Y' and user_confirmation != 'N':
                        raise ValueError("Chose only Yes or No (y/n)")
                    elif user_confirmation == 'y' or user_confirmation == 'Y':
                        delete_student_data(students_data, delete_student_name, delete_student_section)
                        flag_confirmation = False
                    else:
                        break
                except ValueError as err:
                    print(err)
        else:
            print("Student's name and section combination not found.")
            enter_hold()

def select_failed_students():
    students_data = read_student_data_file()
    failed_students_list = []
    failed_flag = False
    for i in range(1,len(students_data)):
        for grades in range(2,len(HEADERS)):
            if int(students_data[i][grades]) < 60:
                failed_flag = True
        if failed_flag:
            failed_students_list.append(students_data[i])
    if len(failed_students_list) == 0:
        print("No failed students.")
        enter_hold()
    else:
        print_failed_students(failed_students_list)

def print_failed_students(data_list):
    print("\nFAILED STUDENTS")
    print("---------------\n")
    for i in range(len(data_list)):
        print(f"{HEADERS[0]}: {data_list[i][0]}")
        print(f"{HEADERS[1]}: {data_list[i][1]}")
        print("Failed subjects:")
        for grades in range(2,len(data_list)):
            if int(data_list[i][grades]) < 60:
                print(f"{HEADERS[grades]}: {data_list[i][grades]}")
        print("")
    enter_hold()