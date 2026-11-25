user_logged_in = True

def requires_login(func):
    def wrapper(*args):
        try:
            if not user_logged_in:
                raise Exception("User not logged in. Please log in first.")
            else:
                func(*args)
        except Exception as err:
            print(err)
    return wrapper

@requires_login
def view_profile():
    print("Showing user profile.")

def main():
    view_profile()

if __name__ == '__main__':
    main()