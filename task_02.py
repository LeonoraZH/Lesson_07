"""
Задание 2.

Реализовать класс Road (дорога), в котором определить защищенные атрибуты:
length (длина в метрах), width (ширина в метрах).

Значения данных атрибутов должны передаваться при создании экземпляра класса.

Реализовать публичный метод расчета массы асфальта, необходимого для покрытия
всего дорожного полотна.

Использовать формулу: длина * ширина * масса асфальта для покрытия одного кв
метра дороги асфальтом, толщиной в 1 см * число м толщины полотна.
Массу и толщину сделать публичными атрибутами.
Проверить работу метода.

Например: 20м*5000м*25кг*0.05м = 125000 кг = 125 т
"""

class Road:
    def __init__(self, length, width):
        self._length = length
        self._width = width
        self.mass_per_sq_meter = 25
        self.thickness = 0.05
        
    def asphalt_mass_calculation(self):
        total_area = self._length * self._width
        asphalt_mass = total_area * self.mass_per_sq_meter * self.thickness
        return asphalt_mass

road = Road(20, 5000)
print(road.asphalt_mass_calculation())