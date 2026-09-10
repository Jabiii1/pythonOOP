class car:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year
        self.isrunning = False
        self.milage = 0

    def start_engine(self):
        if self.isrunning:
            print(f"the {self.brand} is already running!")
        else:
            self.isrunning = True
            print(f"the {self.brand}'s engine is now running!")

    def stop_engine(self):
        if not self.isrunning:
            print(f"the {self.brand} is already off!")
        else:
            self.isrunning = False
            print(f"the {self.brand}'s engine has stopped!")

    def drive(self, distance):
        if not self.isrunning:
            print(f"Cannot drive! Start the {self.brand} engine first!")
        else:
            self.milage += distance
            print(f"Drove {distance}km. Total milage: {self.milage} km")


car1 = car('Toyota', "Corolla", 2022)
car2 = car('Tesla', "Model 3", 2024)

car1.start_engine()
car1.drive(50)


    

