from line import Line
from point import Point

class Cell():
    def __init__(self,
                 has_left=True,
                 has_right=True,
                 has_top=True,
                 has_bottom=True):
        self.has_left = has_left
        self.has_right = has_right
        self.has_top = has_top
        self.has_bottom = has_bottom
        self._x1 = 0
        self._y1 = 0
        self._x2 = 0
        self._y2 = 0
        self._window = None

    def draw(self, window, x1, y1, x2, y2):
        if x1 >= x2 or y1 >= y2:
            raise Exception("Invalid coordinates for cell")
            
        self._window = window
        self._x1 = x1 
        self._y1 = y1 
        self._x2 = x2 
        self._y2 = y2 

        upper_left = Point(x1, y1)
        lower_left = Point(x1, y2)
        upper_right = Point(x2, y1)
        lower_right = Point(x2, y2)

        top_line = Line(upper_left, upper_right)
        right_line = Line(upper_right, lower_right)
        bottom_line = Line(lower_left, lower_right)
        left_line = Line(upper_left, lower_left)

        if self.has_left:
            self._window.draw_line(left_line, "black")
        if self.has_top:
            self._window.draw_line(top_line, "black")
        if self.has_right:
            self._window.draw_line(right_line, "black")
        if self.has_bottom:
            self._window.draw_line(bottom_line, "black")

    def draw_move(self, window, to_cell, undo=False):
        color = "red" if not undo else "gray"
        self._window = window

        center1 = self.get_center()
        center2 = to_cell.get_center()
        line = Line(center1, center2)

        self._window.draw_line(line, color)

    def get_center(self):
        x_center = (self._x2 - self._x1) / 2 + self._x1
        y_center = (self._y2 - self._y1) / 2 + self._y1

        return Point(x_center, y_center) 
