class Point:
    """Create a point object with x and y coordinates"""

    def __init__(self, x_coord, y_coord):
        self._x_coord = x_coord
        self._y_coord = y_coord

    def get_x_coord(self):
        return self._x_coord

    def get_y_coord(self):
        return self._y_coord

    def distance_to(self, point):
        """return the distance from the first point to the second point"""
        x_block = (self._x_coord - point._x_coord) ** 2
        y_block = (self._y_coord - point._y_coord) ** 2
        total = x_block + y_block
        return total**0.5

    def get_slope(self, point):
        """return the slope of a line from the first point to the second point"""
        if self._x_coord - point._x_coord == 0:
            return "Undefined"
        return (self._y_coord - point._y_coord) / (self._x_coord - point._x_coord)


class LineSegment:
    """Create a linesegegment object with tow points"""

    def __init__(self, endpoint_1, endpoint_2):
        self._endpoint_1 = endpoint_1
        self._endpoint_2 = endpoint_2

    def get_endpoint_1(self):
        return self._endpoint_1

    def get_endpoint_2(self):
        return self._endpoint_2

    def length(self):
        """returns the length of the line segment"""
        return self._endpoint_1.distance_to(self._endpoint_2)

    def slope(self):
        """returns the slope of the line segement"""
        return self._endpoint_1.get_slope(self._endpoint_2)

    def is_parallel_to(self, line_segment):
        """returns boolean comparing the slope of the first line segment and the second"""
        slope1 = self.slope()
        slope2 = line_segment.slope()
        if slope1 == "Undefined" and slope2 == "Undefined":
            return True
        if slope1 == "Undefined" or slope2 == "Undefined":
            return False
        if abs(slope1 - slope2) < 0.000001:
            return True
        else:
            return False


# Create two new points
point_1 = Point(1, 4)
point_2 = Point(2, 8)
print(point_1.distance_to(point_2))

# create line segement
line_seg_1 = LineSegment(point_1, point_2)
print(line_seg_1.length())
print(line_seg_1.slope())

# create two moer points
point_3 = Point(2, 5)
point_4 = Point(3, 9)

# create second line segment
line_seg_2 = LineSegment(point_3, point_4)
print(line_seg_1.is_parallel_to(line_seg_2))
