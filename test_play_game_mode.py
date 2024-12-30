import pytest
import pygame
from play_game_mode import select_level, play_game_mode


@pytest.fixture
def pygame_setup():
    pygame.init()
    surface = pygame.display.set_mode((1200, 800))
    font = pygame.font.SysFont('Comic Sans MS', 30)
    yield pygame, surface, font
    pygame.quit()


def test_select_level_quit(pygame_setup, monkeypatch):
    pygame, surface, font = pygame_setup

    monkeypatch.setattr('pygame.event.get',
                        lambda: [pygame.event.Event(pygame.QUIT)])
    assert select_level(pygame, surface, font) is None


def test_select_level_easy(pygame_setup, monkeypatch):
    pygame, surface, font = pygame_setup

    def mock_get():
        return [pygame.event.Event(pygame.MOUSEBUTTONDOWN,
                                   {'button': 1, 'pos': (550, 320)})]

    monkeypatch.setattr('pygame.event.get', mock_get)
    monkeypatch.setattr('pygame.mouse.get_pressed', lambda: (1, 0, 0))
    monkeypatch.setattr('pygame.mouse.get_pos', lambda: (550, 320))

    assert select_level(pygame, surface, font) == 'Easy'


def test_select_level_medium(pygame_setup, monkeypatch):
    pygame, surface, font = pygame_setup

    def mock_get():
        return [pygame.event.Event(pygame.MOUSEBUTTONDOWN,
                                   {'button': 1, 'pos': (550, 420)})]

    monkeypatch.setattr('pygame.event.get', mock_get)
    monkeypatch.setattr('pygame.mouse.get_pressed', lambda: (1, 0, 0))
    monkeypatch.setattr('pygame.mouse.get_pos', lambda: (550, 420))

    assert select_level(pygame, surface, font) == 'Medium'


def test_select_level_hard(pygame_setup, monkeypatch):
    pygame, surface, font = pygame_setup

    def mock_get():
        return [pygame.event.Event(pygame.MOUSEBUTTONDOWN,
                                   {'button': 1, 'pos': (550, 520)})]

    monkeypatch.setattr('pygame.event.get', mock_get)
    monkeypatch.setattr('pygame.mouse.get_pressed', lambda: (1, 0, 0))
    monkeypatch.setattr('pygame.mouse.get_pos', lambda: (550, 520))

    assert select_level(pygame, surface, font) == 'Hard'


def test_play_game_mode_quit(pygame_setup, monkeypatch):
    pygame, surface, font = pygame_setup

    def mock_select_level(*args):
        return 'Easy'

    monkeypatch.setattr('play_game_mode.select_level', mock_select_level)
    monkeypatch.setattr('pygame.event.get',
                        lambda: [pygame.event.Event(pygame.QUIT)])

    play_game_mode(pygame, surface, font)
    assert True  # If no exceptions, the test passes
