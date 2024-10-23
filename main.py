from window import Window
from line import Line
from point import Point
from cell import Cell
from maze import Maze

def main():
    win = Window(800, 600)
    
    # draw here
    maze = Maze(50, 50, 10, 14, 50, 50, win) 

    maze._break_entrance_and_exit()

    maze._break_walls_r(0, 0)

    maze._reset_cells_visited()

    maze.solve()     
    
    win.wait_for_close()



main()