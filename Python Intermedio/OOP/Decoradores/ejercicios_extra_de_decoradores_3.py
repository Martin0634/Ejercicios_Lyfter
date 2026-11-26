from datetime import datetime

def log_call(func):
    def wrapper(a, b):
        print(f"Function name: {func.__name__}")
        print(f"Function arguments: {a}, {b}")
        print(f"Date: {datetime.now()}")
        result = func(a,b)
        print(f"Function returns: {result}")
        return result
    return wrapper

def validate_numbers(func):
    def wrapper(a, b):
        try:
            if isinstance(float(a), (int, float)) and isinstance(float(b), (int, float)):
                print("Parameters are numbers. Function can run.")
                return func(float(a), float(b))
            else:
                raise ValueError
        except ValueError as err:
            print("One of the parameters is not a number.\nFunction can't run.")
    return wrapper

@validate_numbers
@log_call 
def multiply(a,b):
    return (a * b)

def main():
    multiply(3, '5')
    multiply(3, 'Cinco')
    multiply(3, 4)

if __name__ == '__main__':
    main()