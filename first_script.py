class Vehicle:
    def __init__(self, started = False, speed = 0):
        self.started = started
        self.speed = speed
    
    def start(self):
        self.started = True
        print("Vehicle on")
    
    def increase_speed(self, delta):
        if self.started:
            self.speed = self.speed + delta
            print("Vroom")
        else:
            print("Turn the vehicle on")


class Car(Vehicle):
    trunk_open = False

    def open_trunk(self):
        self.trunk_open = True

    def close_trunk(self):
        self.trunk_open = False

class Bike(Vehicle):
    def __init__(self, center_stand_out = False):
        self.center_stand_out = center_stand_out
        super().__init__()
    def start(self):
        print("Sorry, out of fuel!")

my_bike = Bike()

my_bike.speed

my_bike.increase_speed(10)
my_bike.start()

my_car = Car()

my_car.trunk_open
