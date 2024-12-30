import pygame
import time
from grid import Grid


def select_level(pygame, surface, font):
    surface.fill((245, 255, 247))
    title_surface = font.render("Select Level", False, (0, 0, 0))
    surface.blit(title_surface, (500, 200))

    levels = ['Easy', 'Medium', 'Hard']
    level_positions = [(500, 300), (500, 400), (500, 500)]

    for idx, pos in enumerate(level_positions):
        pygame.draw.rect(surface, (0, 0, 0), (*pos, 200, 50), width=3, border_radius=10)
        text_surface = font.render(levels[idx], False, (0, 0, 0))
        surface.blit(text_surface, (pos[0] + 50, pos[1] + 10))

    pygame.display.flip()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return None
            if event.type == pygame.MOUSEBUTTONDOWN:
                if pygame.mouse.get_pressed()[0]:
                    mouse_pos = pygame.mouse.get_pos()
                    for idx, pos in enumerate(level_positions):
                        if pos[0] < mouse_pos[0] < pos[0] + 200 and \
                           pos[1] < mouse_pos[1] < pos[1] + 50:
                            return levels[idx]


def play_game_mode(pygame, surface, font):
    game_font2 = pygame.font.SysFont('Comic Sans MS', 25)

    difficulty = select_level(pygame, surface, font)
    if not difficulty:
        return

    grid = Grid(pygame, font, difficulty)
    start_time = time.time()
    elapsed_time = 0
    running = True

    while running:
        if not grid.win:
            elapsed_time = time.time() - start_time

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN and not grid.win:
                if pygame.mouse.get_pressed()[0]:
                    pos = pygame.mouse.get_pos()
                    grid.get_mouse_click(pos[0], pos[1])
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and grid.win:
                    grid.restart()
                    start_time = time.time()
                    elapsed_time = 0

        surface.fill((245, 255, 247))
        grid.draw_all(pygame, surface)

        minutes = int(elapsed_time // 60)
        seconds = int(elapsed_time % 60)
        time_surface = font.render(f" {minutes:02d} : {seconds:02d}",
                                   False, (0, 0, 0))
        surface.blit(time_surface, (980, 600))

        if grid.win:
            won_surface = font.render("You Won!", False, (0, 255, 0))
            surface.blit(won_surface, (970, 700))
            press_space_surf = game_font2.render("Press Space to play again",
                                                 False, (0, 255, 200))
            surface.blit(press_space_surf, (950, 750))

        pygame.display.flip()
