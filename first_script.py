print('Hello World')

class Car:
    speed = 0
    started = False
    
    def start(self):
        self.started = True
        print("Car started.")

    def accelerate(self, delta):
        if self.started:
            self.speed = self.speed + delta
            print('Vroooom')
        else:
            print('Start the car first.')

    def stop(self):
        self.speed = 0
        print("Car stopped.")

    def turn_off(self):
        self.started = False
        print('Car turned off')


my_first_car = Car()

type(my_first_car)


my_first_car.start()
my_first_car.accelerate(10)
my_first_car.stop()
my_first_car.turn_off()

my_first_car.speed

my_first_car.started
