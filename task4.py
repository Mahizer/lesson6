# Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты: speed, color, name, is_police (булево).
# А также методы: go, stop, turn(direction), кот. должны сообщать, что машина поехала, остановилась, повернула (куда).
# Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar. Добавьте в базовый класс метод show_speed,
# который должен показывать текущую скорость автомобиля. Для классов TownCar и WorkCar переопределите метод show_speed.
# При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
# Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам, выведите результат.
# Выполните вызов методов и также покажите результат.


def stop():
    return 'Машина остановилась'


class Car:

    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def stop(self):
        print('Машина остановилась')

    def go(self):
        print('Машина поехала')

    def turn(self, direction):
        print(f'Машина повернула {direction}')

    def show_speed(self):
        return self.speed


class TownCar(Car):
    def show_speed(self):
        if self.speed > 60:
            print('Вы превышаете скорость!')
        else:
            print(self.speed)


class SportCar(Car):
    pass


class WorkCar(Car):
    def show_speed(self):
        if self.speed > 40:
            print('Вы превышаете скорость!')
        else:
            print(self.speed)


class PoliceCar(Car):
    def police(self):
        if self.is_police == True:
            print('Полицейская машина')


my_car = TownCar(50, 'blue', 'audi', False)
my_car.show_speed()
my_car.turn('налево')


first_car = PoliceCar(70, 'red', 'lada', True)
first_car.police()
print(f'Скорость автомобиля {first_car.name} = {first_car.show_speed()}')

