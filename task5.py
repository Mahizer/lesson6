# Реализовать класс Stationery (канцелярская принадлежность).
# Определить в нем атрибут title (название) и метод draw (отрисовка). Метод выводит сообщение “Запуск отрисовки.”
# Создать три дочерних класса Pen (ручка), Pencil (карандаш), Handle (маркер).
# В каждом из классов реализовать переопределение метода draw.
# Для каждого из классов методы должен выводить уникальное сообщение.
# Создать экземпляры классов и проверить, что выведет описанный метод для каждого экземпляра.


class Stationery:
    def __init__(self, title):
        self.title = title

    def draw(self):
        print('Запуск отрисовки.')


class Pen(Stationery):
    def draw(self):
        print('Рисование ручкой')


class Pencil(Stationery):
    def draw(self):
        print('Рисование карандашом')


class Handle(Stationery):
    def draw(self):
        print('Рисование маркером')


pen = Pen('ручка')
pen.draw()
print(pen.title)

pencil = Pencil('карандаш')
pencil.draw()
print(pencil.title)

handle = Handle('маркер')
handle.draw()
print(handle.title)
