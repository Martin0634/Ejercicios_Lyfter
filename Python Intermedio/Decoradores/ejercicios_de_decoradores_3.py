from datetime import datetime

class User:
    def __init__(self, date_of_birth):
        self.date_of_birth = date_of_birth
    
    def age(self):
        current_year = datetime.now().year
        current_month = datetime.now().month
        current_day = datetime.now().day
        user_yob = f"{self.date_of_birth[len(self.date_of_birth)-4]}{self.date_of_birth[len(self.date_of_birth)-3]}{self.date_of_birth[len(self.date_of_birth)-2]}{self.date_of_birth[len(self.date_of_birth)-1]}"
        user_dob = f"{self.date_of_birth[len(self.date_of_birth)-7]}{self.date_of_birth[len(self.date_of_birth)-6]}"
        user_mob = f"{self.date_of_birth[len(self.date_of_birth)-10]}{self.date_of_birth[len(self.date_of_birth)-9]}"
        user_age = int(current_year) - int(user_yob)
        if int(current_month) < int(user_mob):
            user_age -= 1
            return (user_age)
        elif int(current_day) < int(user_dob):
            user_age -= 1
            return (user_age)
        else:
            return (user_age)
    
    def validate_user_age(func):
        def wrapper(self, *args):
            try:
                if (self.age()) < 18:
                    raise Exception("You can't access Adults Only games category. You must be 18 years old or older. ")
                else:
                    print("The Adults Only games category is displayed.")
                func(self, *args)
            except Exception as err:
                print(err)
        return wrapper
    
    @validate_user_age
    def show_ao_games(self):
        print("Showing Adults Only video games category.")

def main():
    user_1 = User('01/12/1982')
    user_1.show_ao_games()
    user_2 = User('01/12/2010')
    user_2.show_ao_games()

if __name__ == '__main__':
    main()