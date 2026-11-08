from actions import add_student_info, show_all_students_data, show_all_students_grade_avg, delete_student, select_failed_students
from data import read_student_data_file

def main_menu():
    flag = True
    while flag:
        print("\n-------------------")
        print("---- MAIN MENU ----\n")
        print("1. Add students")
        print("2. View all students")
        print("3. View top-3 grade average students")
        print("4. View student average grade")
        print("5. Delete student")
        print("6. Failed students")
        print("0. Exit\n")
        
        file_exists = read_student_data_file()
        if file_exists is None:
            print("System Message: Data file doesn't exists yet. Add a student to create data file.\n")
        
        try:
            user_input_option = input("Choose your option: ")
            if int(user_input_option) > 6 or int(user_input_option) < 0:
                raise ValueError
        except ValueError as err:
                print("Invalid option.")
        
        if user_input_option == '0':
            print("\nThank you for using Martin Zeta Systems.")
            print("Have a nice day.")
            flag = False
        
        if user_input_option == '1':
            add_student_info()
            
        if user_input_option == '2':
            show_all_students_data()
        
        if user_input_option == '3':
            show_all_students_grade_avg('top3')
        
        if user_input_option == '4':
            show_all_students_grade_avg('all')
        
        if user_input_option == '5':
            delete_student()
        
        if user_input_option == '6':
            select_failed_students()