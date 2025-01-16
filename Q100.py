class Flyable:
    def fly(self):
        print("Flying")

class Swimmable:
    def swim(self):
        print("Swimming")

class Amphibian(Flyable, Swimmable):
    pass

amphibian = Amphibian()
amphibian.fly()
amphibian.swim()
