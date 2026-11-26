def repeat_twice(func):
    def wrapper(*args):
        func(*args)
        func(*args)
    return wrapper

@repeat_twice
def print_hello(name):
    print(f"Hello {name}")

print_hello('Martin')