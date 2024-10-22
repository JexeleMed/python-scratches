class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def info(self):
        print(f"Car: {self.make} {self.model} {self.year}")

mycar = Car("Ford", "Focus", "2015")


mycar.info()

