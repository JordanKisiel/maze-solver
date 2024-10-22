from window import Window
from line import Line
from point import Point
from cell import Cell

def main():
    win = Window(800, 600)
    
    # draw here
    default_cell = Cell()
    default_cell.draw(win, 300, 200, 400, 400)

    missing_top = Cell(True, True, False, True)
    missing_top.draw(win, 50, 50, 200, 200)

    missing_bottom = Cell(True, True, True, False)
    missing_bottom.draw(win, 100, 120, 450, 230)

    missing_left= Cell(False, True, True, True)
    missing_left.draw(win, 500, 500, 550, 550)

    missing_right = Cell(True, False, True, True)
    missing_right.draw(win, 560, 560, 590, 590)
    
    win.wait_for_close()



main()