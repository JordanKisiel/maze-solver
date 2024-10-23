from cell import Cell
import time
import random

class Maze():
    def __init__(self, 
                 x1,
                 y1,
                 num_rows,
                 num_cols,
                 cell_size_x,
                 cell_size_y,
                 window=None,
                 seed=None):

        self.x1 = x1 
        self.y1 = y1 
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.cell_size_x = cell_size_x
        self.cell_size_y = cell_size_y
        self.window = window
        self._cells = []
        
        if seed != None:
            self.seed = random.seed(seed)

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

    def _break_entrance_and_exit(self):
        self._cells[0][0].has_top = False
        self._cells[self.num_cols- 1][self.num_rows - 1].has_bottom = False
        self._draw_cell(0, 0)
        self._draw_cell(self.num_cols - 1, self.num_rows - 1)

    def _break_walls_r(self, i, j):
        self._cells[i][j].visited = True
        while True:
            to_visit = []
            # must check bounds before adding neighbors
            # must check visited before adding to make sure
            # we don't move in loop
            possible_neighbors = [(i, j + 1), (i + 1, j), (i, j - 1), (i - 1, j)]
            for neighbor in possible_neighbors:
                in_bounds_i = neighbor[0] < self.num_cols and neighbor[0] >= 0
                in_bounds_y = neighbor[1] < self.num_rows and neighbor[1] >= 0

                if in_bounds_i and in_bounds_y:
                    if not self._cells[neighbor[0]][neighbor[1]].visited:
                        to_visit.append(neighbor)

            if len(to_visit) == 0:
                self._draw_cell(i, j)
                return
        
            random_idx = random.randrange(0, len(to_visit))
            random_neighbor = to_visit[random_idx]
            to_right= random_neighbor[0] > i
            to_left = random_neighbor[0] < i
            to_up = random_neighbor[1] < j 
            to_down = random_neighbor[1] > j

            if to_right:
                self._cells[i][j].has_right = False
                self._cells[i + 1][j].has_left = False
            elif to_left:
                self._cells[i][j].has_left = False
                self._cells[i - 1][j].has_right = False
            elif to_up:
                self._cells[i][j].has_top = False
                self._cells[i][j - 1].has_bottom = False
            elif to_down:
                self._cells[i][j].has_bottom = False
                self._cells[i][j + 1].has_top = False

            self._break_walls_r(random_neighbor[0], random_neighbor[1])
            
    def _reset_cells_visited(self):
        def reset(cell):
            cell.visited = False
        self.map_maze(reset) 

    def print_maze(self):
        def print_state(cell):
            print(cell.visited)
        self.map_maze(print_state)

    def map_maze(self, fn):
        for i in range(self.num_cols):
            for j in range(self.num_rows):
                fn(self._cells[i][j])