class Car:
    def __init__(self, brand, model, color):
        self.brand = brand
        self.model = model
        self.color = color
        self.speed = 100

    def speedUp(self, speed_increase):
        self.speed += speed_increase
        print(f"Speed increased. New speed: {self.speed} km/h")

    def slowDown(self, speed_decrease):
        self.speed -= speed_decrease
        print(f"Speed decreased. New speed: {self.speed} km/h")

    def stop(self):
        self.speed = 0
        print("Car stopped.")

    def showInfo(self):
        print(f"Brand: {self.brand}")
        print(f"Model: {self.model}")
        print(f"Color: {self.color}")
        print(f"Speed: {self.speed} km/h\n")


# Main program flow
print("--------------Base Mode--------------")
car1 = Car("Toyota", "Corolla", "White")
car1.showInfo()

print("--------------Drive Mode--------------")
car1.speedUp(50)
car1.slowDown(20)
car1.showInfo()

print("--------------Stop Mode--------------")
car1.stop()
car1.showInfo()
