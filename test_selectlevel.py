import pytest
import pygame

from selectlevel import SelectLevel

@pytest.fixture
def setup():
    pygame.init()
    font = pygame.font.SysFont('Arial', 20)
    return pygame, font

def test_draw(setup):
    pygame, font = setup
    surface = pygame.Surface((1200, 900))
    selector = SelectLevel(pygame, font)

    # Kiểm tra vẽ các nút
    selector.selected_level = 'Medium'
    selector.draw(surface)

    # Kiểm tra màu nút được chọn
    medium_button_pos = selector.btn_positions[1]
    pixel_inside = (medium_button_pos[0] + 10, medium_button_pos[1] + 10)
    assert surface.get_at(pixel_inside)[:3] == selector.color_selected, (
        f"Expected {selector.color_selected} for selected button, but got {surface.get_at(pixel_inside)[:3]}"
    )

    # Kiểm tra màu nút không được chọn
    easy_button_pos = selector.btn_positions[0]
    pixel_inside = (easy_button_pos[0] + 10, easy_button_pos[1] + 10)
    assert surface.get_at(pixel_inside)[:3] == selector.color_normal, (
        f"Expected {selector.color_normal} for unselected button, but got {surface.get_at(pixel_inside)[:3]}"
    )

def test_handle_click(setup):
    pygame, font = setup
    selector = SelectLevel(pygame, font)

    # Giả lập nhấp chuột vào nút "Hard"
    hard_button_pos = selector.btn_positions[2]
    selector.handle_click(hard_button_pos[0] + 1, hard_button_pos[1] + 1)

    assert selector.selected_level == 'Hard', (
        f"Expected selected level to be 'Hard', but got {selector.selected_level}"
    )

    # Giả lập nhấp chuột vào nút "Easy"
    easy_button_pos = selector.btn_positions[0]
    selector.handle_click(easy_button_pos[0] + 1, easy_button_pos[1] + 1)

    assert selector.selected_level == 'Easy', (
        f"Expected selected level to be 'Easy', but got {selector.selected_level}"
    )

def test_on_button(setup):
    pygame, font = setup
    selector = SelectLevel(pygame, font)

    # Kiểm tra khi chuột nằm trên nút
    button_pos = selector.btn_positions[1]  # Nút "Medium"
    assert selector.on_button(button_pos[0] + 1, button_pos[1] + 1, button_pos), (
        "Expected on_button to return True for mouse position inside the button"
    )

    # Kiểm tra khi chuột nằm ngoài nút
    assert not selector.on_button(button_pos[0] - 10, button_pos[1] - 10, button_pos), (
        "Expected on_button to return False for mouse position outside the button"
    )
