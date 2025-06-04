class Car:
    def __init__(self):
        self.__max_speed = 0

    @property
    def max_speed(self):
        return self.__max_speed

    @max_speed.setter
    def max_speed(self, value):
        self.__max_speed = value

    @max_speed.deleter
    def max_speed(self):
        del self.__max_speed

new_car = Car()
new_car.max_speed = 10000
print(f'Max Speed: {new_car.max_speed}')
