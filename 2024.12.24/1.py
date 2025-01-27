class Point:
    """
    Класс, который описывает двумерную точку.
    """
    def __init__(self, x: float, y: float):
        self.__x = x
        self.__y = y
        
    @property    
    def x(self) -> float:
        return self.__x
    @x.setter
    def x(self, value):
        raise TypeError("'Point' object does not support coordinate assignment") 
    @property    
    def y(self) -> float:
        return self.__y
    @y.setter
    def y(self, value):
        raise TypeError("'Point' object does not support coordinate assignment")
    
    def __eq__(self, other) -> bool: # специальный метод, вызываемый для операторов == и !=
        return isinstance(other, Point) and self.__x == other.x and self.__y == other.y                
    
    def __repr__(self):
        return f'({self.__x}, {self.__y})'
    def __str__(self):
        return self.__repr__()

class Line:
    """
    Класс, который описывает двумерный отрезок.
    """
    def __init__(self, start: Point, end: Point):
        self.__start = start
        self.__end = end
        self.__length = self.length_calc(self.__start, self.__end)
        
    @staticmethod    
    def length_calc(point1: Point, point2: Point) -> float:
        """
        Функция, которая находит длинну отрезка по заданным точкам.
        """
        return ((point1.x - point2.x)**2 + (point1.y- point2.y)**2)**0.5 
        
    @property
    def start(self):
        return self.__start
    @start.setter
    def start(self, new_point: Point):
        if not isinstance(new_point, Point): # проверят соответсвие экземпляра заданному классом
            raise TypeError("'start' attribute of 'Line' object supports only 'Point' object assignment")
        self.__start = new_point
        self.__length = self.length_calc(new_point, self.__end)
    @property
    def end(self):
        return self.__end
    @end.setter
    def end(self, new_point: Point):
        if not isinstance(new_point, Point): # проверят соответсвие экземпляра заданному классом
            raise TypeError("'end' attribute of 'Line' object supports only 'Point' object assignment")
        self.__end = new_point
        self.__length = self.length_calc(new_point, self.__start)
    @property
    def length(self):
        return self.__length
    @length.setter
    def length(self, value):
        raise TypeError("'Line' object does not support length assignment")
    
    def __repr__(self):
        return f'{self.__start}---{self.__end}'
    def __str__(self):
        return self.__repr__() 

class Polygon(list):
    """
    Класс, который описывает двумерный многоугольник.
    Количество отрезков должно быть не меньше трёх.
    Элементами списка Polygon являются экземпляры Line.
    """
    def __init__(self, *sides: Line):
        if len(sides) < 3:
            raise ValueError("A polygon must have at least three sides.")
        if not all(isinstance(side, Line) for side in sides):
            raise TypeError("All sides must be 'Line' objects.")
        self.sides = sides
    
    @property
    def perimeter(self) -> float:
        """
        Функция, которая находит периметр многоугольника.
        Если многоугольник незамкнутый, то выбрасывается исключение.
        """
        self.is_closed()
        return sum(side.length for side in self.sides) # сумма длин отрезков

    def is_closed(self) -> None:
        """
        Приватный метод, который проверяет многоугольник на замкнутость.
        Конец каждой стороны многоугольника должен совпадать с началом следующей стороны.
        """
        for i in range(len(self.sides)):
            current_end = self.sides[i].end # исходный отрезок
            next_start = self.sides[(i + 1) % len(self.sides)].start # отрезок, следующий за исходным 
            if current_end != next_start:
                 raise ValueError("line items doesn't form a closed polygon") 

# >>> p1 = Point(0, 3)
# >>> p2 = Point(4, 0)
# >>> p3 = Point(8, 3)
# >>> p1
# (0, 3)
# >>> repr(p1) == str(p1)
# True
# >>> p1 == Point(0, 3)
# True
# >>> p1.x, p1.y
# (0, 3)
# >>> p2.y = 5

# TypeError: 'Point' object does not support coordinate assignment
# >>> l1 = Line(p1, p2)
# >>> l2 = Line(p2, p3)
# >>> l3 = Line(p3, p1)
# >>> l1
# (0, 3)---(4, 0)
# >>> repr(l1) == str(l1)
# True
# >>> l1.length
# 5.0
# >>> l1.length = 10

# TypeError: 'Line' object does not support length assignment
# >>> l3.start = 12

# TypeError: 'start' attribute of 'Line' object supports only 'Point' object assignment
# >>> pol1 = Polygon(l1, l2, l3)
# >>> pol1.perimeter
# 18.0
# >>> pol1.perimeter = 20

# AttributeError: property 'perimeter' of 'Polygon' object has no setter
# >>> l3.end = Point(-10, -10)
# >>> pol1.perimeter

# ValueError: line items doesn't form a closed polygon                 
                        