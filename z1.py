#Ерженин Александр ДПИ23-1с
#Задание 1


#Класс point, который имеет два атрибута x и y
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"Точка ({self.x}, {self.y})"


#Класс rect, который имеет два атрибута (верхний левый и нижний правый углы)
#А также методы init(), str(), sides() и perim()
class Rect:
    def __init__(self, top_left: Point, bottom_right: Point):
        self.top_left = top_left
        self.bottom_right = bottom_right

    def __str__(self):
        return f"Прямоугольник (Верхний левый угол: {self.top_left}, Нижний правый угол: {self.bottom_right})"

    def sides(self):
        width = self.bottom_right.x - self.top_left.x
        height = self.top_left.y - self.bottom_right.y
        return width, height

    def perim(self):
        width, height = self.sides()
        return 2 * (width + height)



if __name__ == "__main__":
    # Создаем точки
    p1 = Point(1, 4)
    p2 = Point(5, 1)

    # Создаем прямоугольник
    rectangle = Rect(p1, p2)

    # Выводим информацию о прямоугольнике
    print(rectangle)

    # Вычисляем длины сторон
    width, height = rectangle.sides()
    print(f"Ширина: {width}, Высота: {height}")

    # Вычисляем периметр
    perimeter = rectangle.perim()
    print(f"Периметр: {perimeter}")
