class Student:
    students_data_list = []
    
    def __init__(self, full_name, section, spanish_grade, english_grade, social_grade, science_grade):
        self.full_name = full_name
        self.section = section
        self.spanish_grade = spanish_grade
        self.english_grade = english_grade
        self.social_grade = social_grade
        self.science_grade = science_grade
    
    def add_verified_student(student):
            Student.students_data_list.append(student)
    
    def to_dict():
        dict_data_list = []
        dict_data ={}
        for student in Student.students_data_list:
            dict_data = {
                "Name": student.full_name,
                "Section": student.section,
                "Spanish Grade": student.spanish_grade,
                "English Grade": student.english_grade,
                "Social Studies Grade": student.social_grade,
                "Science Grade": student.science_grade
            }
            dict_data_list.append(dict_data)
        return dict_data_list