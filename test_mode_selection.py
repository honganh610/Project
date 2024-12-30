import pytest
from mode_selection import ModeSelection
import pygame


@pytest.fixture
def mode_selection():
    pygame.init()
    font = pygame.font.Font(None, 36)
    return ModeSelection(pygame, font)


def test_initial_modes(mode_selection):
    assert mode_selection.modes == ['Play Game', 'Solve Sudoku']


def test_initial_selected_mode(mode_selection):
    assert mode_selection.selected_mode is None


def test_initial_button_positions(mode_selection):
    assert mode_selection.btn_positions == [(500, 400), (500, 500)]


def test_initial_button_size(mode_selection):
    assert mode_selection.btn_size == (250, 50)


def test_initial_colors(mode_selection):
    assert mode_selection.color_selected == (0, 255, 0)
    assert mode_selection.color_normal == (0, 0, 0)


def test_handle_click_selects_mode(mode_selection):
    mode_selection.handle_click(510, 410)
    assert mode_selection.selected_mode == 'Play Game'
    mode_selection.handle_click(510, 510)
    assert mode_selection.selected_mode == 'Solve Sudoku'


def test_handle_click_outside_buttons(mode_selection):
    mode_selection.handle_click(100, 100)
    assert mode_selection.selected_mode is None


def test_on_button_true(mode_selection):
    assert mode_selection.on_button(510, 410, (500, 400)) is True


def test_on_button_false(mode_selection):
    assert mode_selection.on_button(100, 100, (500, 400)) is False


def test_draw(mode_selection):
    surface = pygame.Surface((800, 600))
    mode_selection.draw(surface)
    # This test is basic and does not verify the actual drawing
    assert True
