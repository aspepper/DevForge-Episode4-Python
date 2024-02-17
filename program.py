class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greather(self):
        return f"Hello, my name is {self.name} and I am {self.age} years old."

person = Person("Alex Pimenta", 51)
print(person.greather())
