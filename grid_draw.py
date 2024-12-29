class GridDraw:
    def __init__(self, game_font, cell_size, num_x_offset,
                 num_y_offset, line_coordinates):
        self.game_font = game_font
        self.cell_size = cell_size
        self.num_x_offset = num_x_offset
        self.num_y_offset = num_y_offset
        self.line_coordinates = line_coordinates

    def draw_lines(self, pg, surface) -> None:
        for index, point in enumerate(self.line_coordinates):
            if index in {2, 5, 10, 13}:
                pg.draw.line(surface, (0, 0, 255), point[0], point[1])
            else:
                pg.draw.line(surface, (173, 216, 230), point[0], point[1])

    def draw_numbers(self, surface, grid, test_grid, occupied_cells) -> None:
        for y in range(len(grid)):
            for x in range(len(grid[y])):
                if grid[y][x] != 0:
                    if (y, x) in occupied_cells:
                        text_color = (10, 10, 10)
                    elif grid[y][x] != test_grid[y][x]:
                        text_color = (255, 0, 0)
                    else:
                        text_color = (0, 255, 0)

                    text_surface = self.game_font.render(str(grid[y][x]),
                                                         False, text_color)
                    surface.blit(text_surface,
                                 (x * self.cell_size + self.num_x_offset,
                                  y * self.cell_size + self.num_y_offset))
