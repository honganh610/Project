from grid_logic import GridLogic
from grid_draw import GridDraw
from selection import SelectNumber
from utils import create_line_coordinates


class Grid:
    def __init__(self, pygame, font, difficulty='Easy'):
        self.difficulty = difficulty
        self.logic = GridLogic(difficulty)
        self.selection = SelectNumber(pygame, font)
        self.draw_helper = GridDraw(
            font,
            cell_size=100,
            num_x_offset=35,
            num_y_offset=35,
            line_coordinates=create_line_coordinates(100)
        )
        self.win = False

    def restart(self) -> None:
        self.logic.restart(self.difficulty)
        self.win = False

    def get_mouse_click(self, x: int, y: int) -> None:
        if self.selection.is_hint_button_clicked(x, y):
            if self.logic.provide_hint():
                if self.logic.check_grids():
                    self.win = True
        else:
            if x <= 900 and not self.win:
                grid_x, grid_y = x // 100, y // 100
                if not self.logic.is_cell_preoccupied(grid_x, grid_y):
                    self.logic.set_cell(grid_x, grid_y,
                                        self.selection.selected_number)
                    if self.logic.check_grids():
                        self.win = True
            self.selection.button_click(x, y)

    def draw_all(self, pg, surface):
        self.draw_helper.draw_lines(pg, surface)
        self.draw_helper.draw_numbers(
            surface,
            self.logic.grid,
            self.logic._GridLogic__test_grid,
            self.logic.occupied_cell_coordinates
        )
        self.selection.draw_button(pg, surface)
