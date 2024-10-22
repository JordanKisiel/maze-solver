from cell import Cell
import time

class Maze():
    def __init__(self, 
                 x1,
                 y1,
                 num_rows,
                 num_cols,
                 cell_size_x,
                 cell_size_y,
                 window=None):

        self.x1 = x1 
        self.y1 = y1 
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.cell_size_x = cell_size_x
        self.cell_size_y = cell_size_y
        self.window = window
        self._cells = []

        self._create_cells()

    def _create_cells(self):
        # create matrix
        for i in range(self.num_cols):
            row = []
            for j in range(self.num_rows):
                row.append(Cell(self.window))
            self._cells.append(row)
        
        for i in range(self.num_cols):
            for j in range(self.num_rows):
                self._draw_cell(i, j)

    def _draw_cell(self, i, j):
        if self.window == None:
            return
        
        x_pos1 = self.x1 + (i * self.cell_size_x)
        y_pos1 = self.y1 + (j * self.cell_size_y)
        x_pos2 = x_pos1 + self.cell_size_x
        y_pos2 = y_pos1 + self.cell_size_y

        self._cells[i][j].draw(x_pos1, 
                               y_pos1, 
                               x_pos2, 
                               y_pos2)
        
        self._animate()

    def _animate(self):
        self.window.redraw()
        time.sleep(0.05)