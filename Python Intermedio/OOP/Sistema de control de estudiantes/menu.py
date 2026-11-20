from actions import add_student_info, show_all_students_data, show_all_students_grade_avg, delete_student, select_failed_students, enter_hold, data_list_validation
from data import read_student_data_file, write_data_list_to_csv
from constants import HEADERS
from classes import Student

def main_menu():
    #data list while the program runs
    students_data_list = []
    #checks if data list was imported
    data_list_flag = False
    #checks data list when no data was imported
    unimported_data_list_flag = False
    #checks if changes were made to data list
    flag_export_data = False
    #main menu
    flag = True
    while flag:
        print("\n-------------------")
        print("---- MAIN MENU ----\n")
        print("1. Import data from file")
        print("2. Add students")
        print("3. View all students")
        print("4. View top-3 grade average students")
        print("5. View student average grade")
        print("6. Delete student")
        print("7. Failed students")
        print("8. Export data to file")
        print("9. Number of Students")
        print("0. Exit\n")
        
        try:
            user_input_option = input("Choose your option: ")
            if int(user_input_option) > 9 or int(user_input_option) < 0:
                raise ValueError
        except ValueError as err:
                print("Invalid option.")
        
        if user_input_option == '0':
            if students_data_list:
                if flag_export_data:
                    flag_confirmation = True
                    while flag_confirmation:
                        user_confirmation = input("There are changes in data not exported yet. All changes will be lost. Do you wish to continue? (y/n): ")
                        if user_confirmation != 'y' and user_confirmation != 'n' and user_confirmation != 'Y' and user_confirmation != 'N':
                            print("Chose only Yes or No (y/n)")
                        if user_confirmation == 'n' or user_confirmation == 'N':
                            flag_confirmation = False
                        else:
                            print("\nThank you for using Martin Zeta Systems.")
                            print("Have a nice day.")
                            flag_confirmation = False
                            flag = False
                else:
                    print("\nThank you for using Martin Zeta Systems.")
                    print("Have a nice day.")
                    flag = False
            else:
                print("\nThank you for using Martin Zeta Systems.")
                print("Have a nice day.")
                flag = False
        
        elif user_input_option == '1':
            if data_list_flag:
                print("Data was already imported.")
                enter_hold()
            elif unimported_data_list_flag and students_data_list is None:
                flag_data = True
                while flag_data:
                    user_confirmation = input("There is data in data list. If you continue, data list will be lost. Continue? (y/n): ")
                    if user_confirmation != 'y' and user_confirmation != 'n' and user_confirmation != 'Y' and user_confirmation != 'N':
                        print("Chose only Yes or No (y/n)")
                    if user_confirmation == 'n' or user_confirmation == 'N':
                        flag_data = False
                    else:
                        students_data_list = read_student_data_file()
                        data_list_flag = data_list_validation(students_data_list)
                        flag_data = False
            else:
                students_data_list = read_student_data_file()
                data_list_flag = data_list_validation(students_data_list)
        
        elif user_input_option == '2':
            students_data_list = add_student_info(students_data_list)
            for data in students_data_list:
                print(f"{HEADERS[0]}: {data.full_name}")
            flag_export_data = True
            if not data_list_flag:
                unimported_data_list_flag = True
            
        elif user_input_option == '3':
            show_all_students_data(students_data_list)
        
        elif user_input_option == '4':
            show_all_students_grade_avg(students_data_list, 'top3')
        
        elif user_input_option == '5':
            show_all_students_grade_avg(students_data_list, 'all')
        
        elif user_input_option == '6':
            delete_student(students_data_list)
            flag_export_data = True
        
        elif user_input_option == '7':
            select_failed_students(students_data_list)
        
        elif user_input_option == '8':
            if not students_data_list:
                print("No data to export.")
                enter_hold()
            else:
                write_data_list_to_csv(students_data_list)
                flag_export_data = False
        
        elif user_input_option == '9':
            print(f"\nStudents registered: {Student.count_students}")
            enter_hold()
        
        else:
            print(f"\nInvalid Option")
            enter_hold()