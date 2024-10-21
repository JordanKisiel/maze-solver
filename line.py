class Line():
    def __init__(self, point1, point2):
        self.point1 = point1
        self.point2 = point2 

    def draw(self, canvas, fill_color):
        canvas.create_line(
            self.point1.x_coord,
            self.point1.y_coord,
            self.point2.x_coord,
            self.point2.y_coord,
            fill=fill_color,
            width=2
        )