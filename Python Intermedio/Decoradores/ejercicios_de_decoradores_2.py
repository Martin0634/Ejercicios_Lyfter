class StudentGrades:
    def __init__(self, math_grade, spanish_grade, english_grade, science_grade):
        self.math_grade = math_grade
        self.spanish_grade = spanish_grade
        self.english_grade = english_grade
        self.science_grade = science_grade
        
    def show_grades(self):
        print(f"Math grade: {self.math_grade}")
        print(f"Spanish grade: {self.spanish_grade}")
        print(f"English grade: {self.english_grade}")
        print(f"Science grade: {self.science_grade}")
    
    def value_numbers(func):
        def wrapper(self, new_math_grade, new_spanish_grade, new_english_grade, new_science_grade, *args):
            print("Validating parameter values are actually numbers.")
            try:
                if not float(new_math_grade) and not float(new_spanish_grade) and not float(new_english_grade) and not float(new_science_grade):
                    raise ValueError("Not all parameters are numbers. Please check.")
                else:
                    func(self, new_math_grade, new_spanish_grade, new_english_grade, new_science_grade, *args)
                    print("All data updated.")
            except ValueError as err:
                print("Not all parameters are numbers. Please check.")
        return wrapper
    
    @value_numbers
    def update_grades(self, new_math_grade, new_spanish_grade, new_english_grade, new_science_grade):
        self.math_grade = new_math_grade
        self.spanish_grade = new_spanish_grade
        self.english_grade = new_english_grade
        self.science_grade = new_science_grade

def main():
    student = StudentGrades(
        math_grade = 72,
        spanish_grade = 79,
        english_grade = 83,
        science_grade = 91
    )
    
    
    student.show_grades()
    student.update_grades('Noventa', 50, 72, 63)
    student.show_grades()
    student.update_grades('90', 50, 72, 63)
    student.show_grades()

if __name__ == '__main__':
    main()