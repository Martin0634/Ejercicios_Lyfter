from actions import add_student_info, show_all_students_data, show_all_students_grade_avg, delete_student, select_failed_students, enter_hold
from data import read_student_data_file, data_list_validation, write_data_list_to_csv

def main_menu():
    #data list while the program runs
    students_data_list = []
    #checks if data list was imported
    data_list_flag = False
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
        print("0. Exit\n")
        
        try:
            user_input_option = input("Choose your option: ")
            if int(user_input_option) > 8 or int(user_input_option) < 0:
                raise ValueError
        except ValueError as err:
                print("Invalid option.")
        
        if user_input_option == '0':
            if flag_export_data:
                print("You need to export data file first. Use menu option 8")
                enter_hold()
            else:
                print("\nThank you for using Martin Zeta Systems.")
                print("Have a nice day.")
                flag = False
        
        if user_input_option == '1':
            if data_list_flag:
                print("Data was already imported.")
                enter_hold()
            else:
                students_data_list = read_student_data_file()
                if students_data_list is not None:
                    data_list_flag = data_list_validation(students_data_list)
        
        if user_input_option == '2':
            if data_list_flag:
                students_data_list = add_student_info(students_data_list)
                flag_export_data = True
            else:
                print("No data imported. Import data from file first")
            
        if user_input_option == '3':
            if not data_list_flag:
                print("No data imported. Import data from file first")
            else:
                show_all_students_data(students_data_list)
        
        if user_input_option == '4':
            if not data_list_flag:
                print("No data imported. Import data from file first")
            else:
                show_all_students_grade_avg(students_data_list, 'top3')
        
        if user_input_option == '5':
            if not data_list_flag:
                print("No data imported. Import data from file first")
            else:
                show_all_students_grade_avg(students_data_list, 'all')
        
        if user_input_option == '6':
            if not data_list_flag:
                print("No data imported. Import data from file first")
            else:
                delete_student(students_data_list)
                flag_export_data = True
        
        if user_input_option == '7':
            if not data_list_flag:
                print("No data imported. Import data from file first")
            else:
                select_failed_students(students_data_list)
        
        if user_input_option == '8':
            if not data_list_flag:
                print("No data imported. Import data from file first")
            else:
                write_data_list_to_csv(students_data_list)
                flag_export_data = False