import pytest
import pygame
from selection import SelectNumber

@pytest.fixture
def setup():
    pygame.init()
    screen = pygame.display.set_mode((1200, 600))
    font = pygame.font.SysFont('Comic Sans MS', 50)
    return pygame, screen, font

def test_button_click(setup):
    pygame, screen, font = setup
    selector = SelectNumber(pygame, font)
    selector.button_click(960, 60)  # Click on the first button
    assert selector.selcected_number == 1

    selector.button_click(960, 260)
    assert selector.selcected_number == 5

    selector.button_click(850, 40)
    assert selector.selcected_number == 5

def test_button_hover(setup, monkeypatch):
    pygame, screen, font = setup
    selector = SelectNumber(pygame, font)

    monkeypatch.setattr(pygame.mouse, 'get_pos', lambda: (960, 60))  # Hover over the first button
    assert selector.button_hover(selector.btn_positions[0]) == True

    monkeypatch.setattr(pygame.mouse, 'get_pos', lambda: (1050, 500))  # Hover over the fifth button
    assert selector.button_hover(selector.btn_positions[0]) == None

def test_draw_button(setup):
    pygame, screen, font = setup
    selector = SelectNumber(pygame, font)
    surface = pygame.Surface((1200, 900))

    selector.selcected_number = 2
    selector.draw_button(pygame, surface)

    selected_button_pos = selector.btn_positions[1]
    pixel_inside_selected = (
        selected_button_pos[0] + selector.btn_w // 2,
        selected_button_pos[1] + selector.btn_h // 2
    )
    surface_color = surface.get_at(pixel_inside_selected)[:3]
    assert surface_color == selector.color_normal # fix laterlater

    unselected_button_pos = selector.btn_positions[0]
    pixel_inside_unselected = (
        unselected_button_pos[0] + selector.btn_w // 2,
        unselected_button_pos[1] + selector.btn_h // 2
    )
    surface_color_unselected = surface.get_at(pixel_inside_unselected)[:3]
    assert surface_color_unselected == selector.color_normal


def test_on_button(setup):
    pygame, screen, font = setup
    selector = SelectNumber(pygame, font)
    assert selector.on_button(960, 60, selector.btn_positions[0]) == True
    assert selector.on_button(850, 40, selector.btn_positions[0]) == False
