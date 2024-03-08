class Car:
    def __init__(self, brand, model, color):
        self.brand = brand
        self.model = model
        self.color = color
        self.speed = 0  # Set initial speed to 0 for safety
        self.distance_travelled = 0  # Track distance

    def speedUp(self, speed_increase):
        if speed_increase < 0:
            print("Speed increase must be a positive value.")
            return
        self.speed += speed_increase
        if self.speed > 200:  # Assuming 200 km/h as max speed
            self.speed = 200
            print("Max speed reached.")
        print(f"Speed increased. New speed: {self.speed} km/h")

    def slowDown(self, speed_decrease):
        if speed_decrease < 0:
            print("Speed decrease must be a positive value.")
            return
        self.speed -= speed_decrease
        if self.speed < 0:
            self.speed = 0
            print("Car has stopped.")
        print(f"Speed decreased. New speed: {self.speed} km/h")

    def stop(self):
        self.speed = 0
        print("Car stopped.")

    def showInfo(self):
        print(f"Brand: {self.brand}")
        print(f"Model: {self.model}")
        print(f"Color: {self.color}")
        print(f"Speed: {self.speed} km/h")
        print(f"Distance Travelled: {self.distance_travelled} km\n")

    def drive(self, time_in_hours):
        """Simulate driving for a certain period at the current speed, updating the distance travelled."""
        distance = self.speed * time_in_hours
        self.distance_travelled += distance
        print(f"Drove for {time_in_hours} hours at {self.speed} km/h, covering {distance} km. Total distance: {self.distance_travelled} km.")


# Inherit from Car to create a specialized version of Car, such as a SportsCar
class SportsCar(Car):
    def __init__(self, brand, model, color):
        super().__init__(brand, model, color)
        self.speed = 0  # Even though it's already set in Car, setting it here shows you can modify base class attributes if needed.

    def speedUp(self, speed_increase):
        super().speedUp(speed_increase * 2)  # Sports cars accelerate faster, hence *2

    def slowDown(self, speed_decrease):
        super().slowDown(speed_decrease * 2)  # Sports cars decelerate faster, hence *2


# Main program flow
print("--------------Base Mode--------------")
car1 = Car("Toyota", "Corolla", "White")
car1.showInfo()

print("--------------Drive Mode--------------")
car1.speedUp(50)
car1.slowDown(20)
car1.drive(2)  # Drive for 2 hours at current speed
car1.showInfo()

print("--------------Stop Mode--------------")
car1.stop()
car1.showInfo()

print("----------SportsCar Mode-------------")
sports_car = SportsCar("Ferrari", "488", "Red")
sports_car.showInfo()
sports_car.speedUp(50)  # Notice how this increases the speed more due to the override
sports_car.drive(1)  # Drive for 1 hour
sports_car.showInfo()
