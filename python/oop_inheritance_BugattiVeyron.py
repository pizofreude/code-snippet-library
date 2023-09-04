# Python OOP Inheritance - Bugatti Veyron
# Bugatti Veyron is a car with a top speed of 431 km/h.

class Vehicle:
    def __init__(self, name, color):
        self.name = name
        self.color = color
        self.speed = 0

    def move(self, speed):
        self.speed = speed
        print(f"The {self.name} is moving at {self.speed} km/h.")

    def stop(self):
        self.speed = 0
        print(f"The {self.name} has stopped.")

class BugattiVeyron(Vehicle):
    def __init__(self, name, color, top_speed):
        super().__init__(name, color)
        self.top_speed = top_speed

    def accelerate(self):
        self.speed += 100
        print(f"The {self.name} is accelerating at {self.speed} km/h.")

    def drift(self):
        self.speed += 100
        print(f"The {self.name} is drifting at {self.speed} km/h.")

    def brake(self):
        self.speed -= 150
        print(f"The {self.name} is braking and slowing down at {self.speed} km/h.")

bugatti_veyron = BugattiVeyron("Bugatti Veyron", "Acquited Blue", 431)
bugatti_veyron.move(150)
bugatti_veyron.drift()
bugatti_veyron.accelerate()
bugatti_veyron.move(431)
bugatti_veyron.brake()
bugatti_veyron.stop()
