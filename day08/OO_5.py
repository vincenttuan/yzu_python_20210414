class Engine:
    power = 0

class Wheel:
    count = 0

class Car(Engine, Wheel):
    def __init__(self, power, count, price):
        self.power = power
        self.count = count
        self.price = price

    def __str__(self):
        print("power:", self.power, " count:", self.count, " prce:", self.price)
        return ""

if __name__ == '__main__':
    car = Car(100000, 150, 2)
    print(car)