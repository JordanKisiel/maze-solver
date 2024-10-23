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
                in_bounds_j = neighbor[1] < self.num_rows and neighbor[1] >= 0

                if in_bounds_i and in_bounds_j:
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
    
    def solve(self):
        return self._solve_r(0, 0)

    def _solve_r(self, i, j):
        self._animate()

        curr_cell = self._cells[i][j]

        curr_cell.visited = True

        at_end_cell = i == self.num_cols - 1 and j == self.num_rows - 1 

        if at_end_cell:
            return True

        cell_top = j - 1 >= 0
        cell_bottom = j + 1 < self.num_rows
        cell_left = i - 1 >= 0
        cell_right = i + 1 < self.num_cols

        # up 
        if cell_top:
            next_cell = self._cells[i][j - 1]
            if not self._is_blocked(curr_cell, next_cell, "up") and not next_cell.visited:
                curr_cell.draw_move(next_cell)
                result = self._solve_r(i, j - 1)
                if result:
                    return True
                curr_cell.draw_move(next_cell, True)
        # down 
        if cell_bottom:
            next_cell = self._cells[i][j + 1]
            if not self._is_blocked(curr_cell, next_cell, "down") and not next_cell.visited:
                curr_cell.draw_move(next_cell)
                result = self._solve_r(i, j + 1)
                if result:
                    return True
                curr_cell.draw_move(next_cell, True)
        # left 
        if cell_left:
            next_cell = self._cells[i - 1][j]
            if not self._is_blocked(curr_cell, next_cell, "left") and not next_cell.visited:
                curr_cell.draw_move(next_cell)
                result = self._solve_r(i - 1, j)
                if result:
                    return True
                curr_cell.draw_move(next_cell, True)

        # right 
        if cell_right:
            next_cell = self._cells[i + 1][j]
            if not self._is_blocked(curr_cell, next_cell, "right") and not next_cell.visited:
                curr_cell.draw_move(next_cell)
                result = self._solve_r(i + 1, j)
                if result:
                    return True
                curr_cell.draw_move(next_cell, True)

        return False

    def _is_blocked(self, cell, other_cell, direction):
        if direction == "up":
            if not cell.has_top and not other_cell.has_bottom:
                return False 
        elif direction == "down":
            if not cell.has_bottom and not other_cell.has_top:
                return False 
        elif direction == "left":
            if not cell.has_left and not other_cell.has_right:
                return False 
        elif direction == "right":
            if not cell.has_right and not other_cell.has_left:
                return False 
        return True 
         