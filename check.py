from utils import create_grid, create_line_coordinates, remove_numbers, SUB_GRID_SIZE
from selection import SelectNumber
from copy import deepcopy




class Grid():
    def __init__(self, pygame, font):
        self.cell_size = 100
        self.num_x_offset = 35
        self.num_y_offset = 35
        self.line_coordinates = create_line_coordinates(self.cell_size)
        self.win = False
        self.game_font = font

        self.grid = create_grid(SUB_GRID_SIZE)
        self.__test_grid = deepcopy(self.grid) # create a copy of the grid before removing numbers
        remove_numbers(self.grid)
        self.occupied_cell_coordinates = self.pre_occupied_cells()

        self.selection = SelectNumber(pygame, self.game_font)

    def restart(self) -> None:
        self.grid = create_grid(SUB_GRID_SIZE)
        self.__test_grid = deepcopy(self.grid)
        remove_numbers(self.grid)
        self.occupied_cell_coordinates = self.pre_occupied_cells()
        self.win = False

    def check_grids(self):
        # Check if all the cells are filled correctly
        for y in range(len(self.grid)):
            for x in range(len(self.grid[y])):
                if self.grid[y][x] != self.__test_grid[y][x]:
                    return False
        return True


    def is_cell_preoccupied(self, x:int, y:int) -> bool:
        # Check if a cell is preoccupied/initialized
        for cell in self.occupied_cell_coordinates:
            if x == cell[1] and y == cell[0]:
                return True
        return False

    def get_mouse_click(self, x: int, y: int) -> None:
        # Sets an empty cell to the selected number
        if x <= 900:
            grid_x, grid_y = x // 100, y // 100
            # print(grid_x, grid_y)
            if not self.is_cell_preoccupied(grid_x, grid_y):
                self.set_cell(grid_x, grid_y, self.selection.selcected_number)
        self.selection.button_click(x,y)
        if self.check_grids():
            self.win = True

    def pre_occupied_cells(self) -> list[tuple]:
        # Gather the y, x coordinates for all preoccupied/initialized cells.
        occupied_cell_coordinates = []
        for y in range(len(self.grid)):
            for x in range(len(self.grid[y])):
                if self.get_cell(x, y) != 0:
                    occupied_cell_coordinates.append((y,x)) # first the row, then the column: y, x
        return occupied_cell_coordinates


    def __draw_lines(self, pg, surface) -> None:
        for index, point in enumerate(self.line_coordinates):
            if index == 2 or index == 5 or index == 10 or index == 13:
                pg.draw.line(surface, (0, 0, 255), point[0], point[1])
            else:
                pg.draw.line(surface, (173, 216, 230), point[0], point[1])

    def __draw_numbers(self, surface) -> None:
        # draw the grid numbers
        for y in range(len(self.grid)):
            for x in range(len(self.grid[y])):
                if self.get_cell(x, y) != 0:
                    if (y, x) in self.occupied_cell_coordinates:
                        text_surface = self.game_font.render(str(self.get_cell(x, y)), False, (10, 10, 10))
                    else:
                        text_surface = self.game_font.render(str(self.get_cell(x, y)), False, (0, 255, 0))

                    if self.get_cell(x, y) != self.__test_grid[y][x]:
                        text_surface = self.game_font.render(str(self.get_cell(x, y)), False, (255, 0, 0))

                    surface.blit(text_surface,
                                (x * self.cell_size + self.num_x_offset, y * self.cell_size + self.num_y_offset))

    def draw_all(self, pg, surface):
        self.__draw_lines(pg, surface)
        self.__draw_numbers(surface)
        self.selection.draw_button(pg, surface)
    def get_cell(self, x: int, y:int) -> int:
        # Get a cell value at y, x coordinate
        return self.grid[y][x]

    def set_cell(self, x:int, y: int, value: int) -> None:
        self.grid[y][x] = value

# import pygame
# import os
# from grid import Grid
# import time

# os.environ['SOL_VIDEO_WINDOW_POS'] = '%d,%d' % (400, 100)

# def main():
#     pygame.init()
#     surface = pygame.display.set_mode((1200, 900))
#     pygame.display.set_caption("Sudoku")

#     game_font = pygame.font.SysFont('Comic Sans MS', 50)
#     game_font2 = pygame.font.SysFont('Comic Sans MS', 25)

#     grid = Grid(pygame, game_font)
#     running = True

#     start_time = time.time()
#     elapsed_time = 0
#     game_in_progress = True
#     while running:

#         # Counting time playing
#         if game_in_progress and not grid.win:
#             elapsed_time = (time.time() - start_time)
#         minutes = int(elapsed_time // 60)
#         seconds = int(elapsed_time % 60)

#         for event in pygame.event.get():
#             if event.type == pygame.QUIT:
#                 running = False
#             if event.type == pygame.MOUSEBUTTONDOWN and not grid.win:
#                 if pygame.mouse.get_pressed()[0]: # check for the left mouse button
#                     pos = pygame.mouse.get_pos()
#                     grid.get_mouse_click(pos[0], pos[1])
#                     grid.selection.button_click(pos[0], pos[1])

#             if event.type == pygame.KEYDOWN:
#                 if event.key == pygame.K_SPACE and grid.win:
#                     grid.restart()
#                     start_time = time.time()
#                     elapsed_time = 0
#                     game_in_progress = True

#         # clearthe window surface to white
#         surface.fill((245, 255, 247))

#         # draw the grid here
#         grid.draw_all(pygame, surface)

#         # draw time playing
#         time_surface = game_font.render(f" {minutes:02d} : {seconds:02d}", False, (0, 0, 0))
#         surface.blit(time_surface, (980, 600))

#         if grid.win:
#             won_surface = game_font.render("You Won!", False, (0, 255, 0))
#             surface.blit(won_surface, (970, 700))

#             press_space_surf = game_font2.render("Press Space to play again", False, (0, 255, 200))
#             surface.blit(press_space_surf, (950, 750))

#             game_in_progress = False

#     #update the window surface
#         pygame.display.flip()



# if __name__ == '__main__':
#     main()
