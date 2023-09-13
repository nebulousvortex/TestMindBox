# Unit tests
from AreaCalculator import *
import unittest


class TestShapes(unittest.TestCase):
    # Тестирование вычисления площади круга
    def test_circle_area(self):
        circle = Circle(5)
        self.assertAlmostEqual(circle.calculate_area(), 78.53981633974483, places=6)

    # Тестирование вычисления площади треугольника
    def test_triangle_area(self):
        triangle = Triangle(3, 4, 5)
        self.assertAlmostEqual(triangle.calculate_area(), 6.0, places=6)

    # Тестирование создание и вычисления площади без знания заранее, какая это фигура
    def test_create_figure(self):
        unknown_figure_1 = AreaCalculator.create_fig("circle", 5)
        self.assertIsInstance(unknown_figure_1, Circle)
        self.assertAlmostEqual(unknown_figure_1.calculate_area(), 78.53981633974483, places=6)

        unknown_figure_2 = AreaCalculator.create_fig("triangle", 3, 4, 5)
        self.assertIsInstance(unknown_figure_2, Triangle)
        self.assertAlmostEqual(unknown_figure_2.calculate_area(), 6.0, places=6)

    # Тестирование вычисления прямого угла
    def test_is_right_triangle(self):
        triangle1 = Triangle(3, 4, 5)
        self.assertTrue(triangle1.is_right_triangle())

        triangle2 = Triangle(5, 12, 13)
        self.assertTrue(triangle2.is_right_triangle())

        triangle3 = Triangle(4, 7, 9)
        self.assertFalse(triangle3.is_right_triangle())


if __name__ == "__main__":
    unittest.main()
