import math


# Если под легкостью добавления других фигур имелось в виду создание новой фигуры с помощью наследования, то я
# создал родительский класс.
class Figure:
    def calculate_area(self):
        pass


class Circle(Figure):
    def __init__(self, radius):
        self.radius = radius

    # Вычисление площади круга по радиусу
    def calculate_area(self):
        return math.pi * (self.radius ** 2)


class Triangle(Figure):
    def __init__(self, side1, side2, side3):
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3

    # Вычисление площади треугольника по трем сторонам
    def calculate_area(self):
        semiperimeter = (self.side1 + self.side2 + self.side3) / 2
        return math.sqrt(
            semiperimeter * (semiperimeter - self.side1) * (semiperimeter - self.side2) * (semiperimeter - self.side3))

    # Проверка теоремы Пифагора
    def is_right_triangle(self):
        sides = [self.side1, self.side2, self.side3]
        # Если треугольник с прямым углом, то у него есть гипотенуза. После сортировки ее индекс будет 2
        sides.sort()
        return sides[0] ** 2 + sides[1] ** 2 == sides[2] ** 2


class AreaCalculator:
    @staticmethod
    def create_fig(figure_type, *args):
        if figure_type == "circle":
            return Circle(*args)
        elif figure_type == "triangle":
            return Triangle(*args)
        else:
            raise ValueError("Неверный тип фигуры")
