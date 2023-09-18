class Taxicab:
    def __init__(self, x_coord, y_coord):
        self._x_coord = x_coord
        self._y_coord = y_coord
        self._odometer = 0

    def _change_odometer(self, num):
        if num < 0:
            self._odometer -= num
        else:
            self._odometer += num

    def get_x_coord(self):
        return self._x_coord

    def get_y_coord(self):
        return self._y_coord

    def get_odometer(self):
        return self._odometer

    def move_x(self, num):
        self._x_coord += num
        self._change_odometer(num)

    def move_y(self, num):
        self._y_coord += num
        self._change_odometer(num)


taxi = Taxicab(5, -8)
taxi.move_x(3)
taxi.move_y(-4)
taxi.move_x(-1)
print(taxi.get_odometer())
print(taxi.get_x_coord())
print(taxi.get_y_coord())
