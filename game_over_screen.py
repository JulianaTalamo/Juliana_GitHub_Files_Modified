import pygame
import sys

# Working menu screen

pygame.init()

# Screen dimensions and window setup
screen_width, screen_height = 750, 750
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Sudoku Game")

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GRAY = (200, 200, 200)
BLUE = (55, 118, 171)


def draw_button(screen, text, x, y, width, height, color):
    # To work with text in pygame, we create a font, render the image, and then blit the image to the screen.
    button_font = pygame.font.SysFont('comicsansms', 20)
    pygame.draw.rect(screen, color, (x, y, width, height))
    text_surf = button_font.render(text, True, BLACK)
    text_rect = text_surf.get_rect(center=(x + (width / 2), y + (height / 2)))
    screen.blit(text_surf, text_rect)


def game_over_screen():
    game_menu = True
    while game_menu:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit_game()
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_x, mouse_y = event.pos
                if 350 < mouse_x < 450 and 350 < mouse_y < 400:
                    restart()

        screen.fill(GRAY)  # Fill the background

        # Draw the "Welcome to Sudoku" message
        welcome_font = pygame.font.SysFont('comicsansms', 60)
        welcome_text = welcome_font.render("Game Over :(", True, BLACK)
        welcome_rect = welcome_text.get_rect(center=(screen_width / 2, screen_height / 4))
        screen.blit(welcome_text, welcome_rect)

        draw_button(screen, "Restart", 325, 350, 100, 50, BLUE)

        pygame.display.update()


def restart():
    print("Restart")


def exit_game():
    """Exits the game."""
    pygame.quit()
    sys.exit()


if __name__ == "__main__":
    game_over_screen()
