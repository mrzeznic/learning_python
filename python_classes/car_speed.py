from time import gmtime
from time import strftime

# values for topSpeed and currentSpeed in m/s, for acc in m/s^2, time in seconds
class Car():
    def __init__(self, topSpeed, acc):
        self.topSpeed = topSpeed
        self.acceleration = acc

    def calcTime(self, currentSpeed):
        t = (self.topSpeed - currentSpeed) / self.acceleration
        return t


car = Car(75, 3.5)
time = car.calcTime(30)

result = strftime("%H:%M:%S", gmtime(time))

print(result)
