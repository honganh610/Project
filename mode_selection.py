class ModeSelection:
    def __init__(self, pygame, font):
        self.pygame = pygame
        self.font = font
        self.modes = ['Play Game', 'Solve Sudoku']
        self.selected_mode = None
        self.btn_positions = [(500, 400), (500, 500)]
        self.btn_size = (250, 50)
        self.color_selected = (0, 255, 0)
        self.color_normal = (0, 0, 0)

    def draw(self, surface):
        for idx, mode in enumerate(self.modes):
            pos = self.btn_positions[idx]
            color = self.color_selected \
                if mode == self.selected_mode \
                else self.color_normal
            self.pygame.draw.rect(
                surface,
                color,
                (*pos, *self.btn_size),
                width=3,
                border_radius=10
            )
            text_surface = self.font.render(mode, True, (0, 0, 0))
            surface.blit(text_surface, (pos[0] + 10, pos[1] + 10))

    def handle_click(self, mouse_x, mouse_y):
        for idx, pos in enumerate(self.btn_positions):
            if self.on_button(mouse_x, mouse_y, pos):
                self.selected_mode = self.modes[idx]

    def on_button(self, mouse_x, mouse_y, pos):
        return pos[0] < mouse_x < pos[0] + self.btn_size[0] and \
               pos[1] < mouse_y < pos[1] + self.btn_size[1]
