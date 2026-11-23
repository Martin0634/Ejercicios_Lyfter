class Animal:
    def __init__(self, name):
        self.name = name
    
    def speak(self):
        return "Makes sound"

class Dog(Animal):
    def speak(self):
        return "Woof"

class Cat(Animal):
    def speak(self):
        return "Meow"

def main():
    dog_1 = Dog('Firulais')
    print(f"{dog_1.name} is speaking '{dog_1.speak()}'")
    cat_1 = Cat('Don Gato')
    print(f"{cat_1.name} is speaking '{cat_1.speak()}'")

if __name__ == '__main__':
    main()