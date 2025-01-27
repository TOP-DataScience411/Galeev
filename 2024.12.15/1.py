class Tetrahedron:
    """
    Класс, который описывает правильный тетраэдр.
    """
    def __init__(self, edge: float):
        self.edge = float(edge)
        
    def surface(self):
        """
        Функция, которая вычисляет площадь поверхности.
        """
        return self.edge**2 * 3**0.5
        
    def volume(self):
        """
        Функция, которая вычисляет объём.
        """
        return self.edge**3 / 12 * 2**0.5
 
# >>> t1 = Tetrahedron(5)
# >>> t1.surface()
# 43.30127018922193
# >>> t1.volume()
# 14.73139127471974
# >>> t1.edge = 6
# >>> t1.surface()
# 62.35382907247958 