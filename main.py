class Ellipse:
    def __init__(self, x1=None, y1=None, x2=None, y2=None):
        if x1 is not None and y1 is not None and x2 is not None and y2:
            self.x1 = x1
            self.y1 = y1
            self.x2 = x2
            self.y2 = y2
        else:
            return

    def __bool__(self):
        return all(map(lambda x: x in self.__dict__, ('x1', 'y1', 'x2', 'y2')))

    def get_coords(self):
        if not self.__bool__():
            raise AttributeError('нет координат для извлечения')
        return (self.x1, self.y1, self.x2, self.y2)

lst_geom = [Ellipse(), Ellipse(), Ellipse(1, 1, 2, 2), Ellipse(1, 1, 3, 3)]

for geom in lst_geom:
    if bool(geom):
        geom.get_coords()