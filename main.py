import pygame
import os
from mode_selection import ModeSelection
from play_game_mode import play_game_mode
from solve_sudoku_mode import solve_sudoku_mode


os.environ['SOL_VIDEO_WINDOW_POS'] = '%d,%d' % (400, 100)


def main():
    pygame.init()
    surface = pygame.display.set_mode((1200, 900))
    pygame.display.set_caption("Sudoku")
    font = pygame.font.SysFont('Comic Sans MS', 50)
    mode_selection = ModeSelection(pygame, font)

    running = True
    selected_mode = None

    while running:
        surface.fill((255, 255, 255))
        mode_selection.draw(surface)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                mode_selection.handle_click(pos[0], pos[1])
                selected_mode = mode_selection.selected_mode

        pygame.display.flip()

        if selected_mode == 'Play Game':
            play_game_mode(pygame, surface, font)
            selected_mode = None
        elif selected_mode == 'Solve Sudoku':
            solve_sudoku_mode(pygame, surface, font)
            selected_mode = None


if __name__ == '__main__':
    main()
