from window import Window
from line import Line
from point import Point

def main():
    win = Window(800, 600)
    
    # draw here
    test_pt_1 = Point(800, 0)
    test_pt_2 = Point(500, 500)

    test_line = Line(test_pt_1, test_pt_2)
    win.draw_line(test_line, "red")
    
    win.wait_for_close()



main()