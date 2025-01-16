class Animal:
    def sound(self):
        print("Some sound")

class Dog(Animal):
    def sound(self):
        print("Woof!")

animal = Animal()
dog = Dog()

animal.sound()
dog.sound()
