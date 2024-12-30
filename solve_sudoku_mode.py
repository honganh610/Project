from grid_draw import GridDraw
from solver_sudoku import SolveSudoku
from utils import create_line_coordinates


def solve_sudoku_mode(pygame, surface, font):
    grid_draw = GridDraw(
        game_font=font,
        cell_size=100,
        num_x_offset=35,
        num_y_offset=35,
        line_coordinates=create_line_coordinates(100)
    )
    solver = SolveSudoku()

    grid = [[0 for _ in range(9)] for _ in range(9)]
    input_mode = True
    running = True
    selected_cell = None
    message = ""
    solved_grid = None

    while running:
        surface.fill((245, 255, 247))
        grid_draw.draw_lines(pygame, surface)

        for row in range(9):
            for col in range(9):
                value = grid[row][col]
                if value != 0:
                    if solved_grid and \
                       solved_grid[row][col] != 0 and \
                       solved_grid[row][col] != grid[row][col]:
                        color = (0, 255, 0)
                    else:
                        color = (10, 10, 10)
                    text_surface = font.render(str(value), True, color)
                    surface.blit(
                        text_surface,
                        (col * 100 + 35, row * 100 + 35)
                    )

        if not input_mode:
            msg_surface = font.render(message, True, (0, 255, 0))
            surface.blit(msg_surface, (920, 470))

        if selected_cell:
            x, y = selected_cell
            pygame.draw.rect(
                surface, (100, 173, 216),
                (x * 100, y * 100, 100, 100),
                width=5
            )

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if input_mode:
                if event.type == pygame.MOUSEBUTTONDOWN:
                    pos = pygame.mouse.get_pos()
                    x, y = pos[0] // 100, pos[1] // 100
                    if 0 <= x < 9 and 0 <= y < 9:
                        selected_cell = (x, y)

                if event.type == pygame.KEYDOWN:
                    if selected_cell:
                        x, y = selected_cell
                        if event.key == pygame.K_BACKSPACE or \
                           event.key == pygame.K_DELETE:
                            grid[y][x] = 0
                        elif pygame.K_1 <= event.key <= pygame.K_9:
                            grid[y][x] = event.key - pygame.K_0

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_s:  # Solve
                    input_mode = False
                    solver.grid = grid
                    if not solver.is_valid_grid():
                        message = "Invalid board logic"
                    elif solver.solve():
                        grid = solver.grid
                        message = "Solved!"
                    else:
                        message = "Cannot solve!"
                if event.key == pygame.K_r:  # Reset
                    grid = [[0] * 9 for _ in range(9)]
                    input_mode = True
                    message = ""

        pygame.display.flip()
