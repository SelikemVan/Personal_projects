import pygame
import sys

# Initialize Pygame and Pygame mixer
pygame.init()
pygame.mixer.init()

# Define constants
WIDTH, HEIGHT = 800, 600
FPS = 60

# Set up the game window
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Adventure Game")

# Define colors
WHITE = (255, 255, 255)

# Load introduction music
pygame.mixer.music.load("intro_music.mp3")
pygame.mixer.music.set_volume(0.5)  # Adjust the volume (0.0 to 1.0)
pygame.mixer.music.play(-1)  # -1 makes the music loop indefinitely

# Create the player character
player_size = 50
player_x = WIDTH // 2 - player_size // 2
player_y = HEIGHT - player_size - 10

# Set up clock for controlling the frame rate
clock = pygame.time.Clock()

# Introduction loop
intro_running = True
while intro_running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            intro_running = False

    # Draw introduction screen
    screen.fill(WHITE)

    # Add a customized welcome message with Times New Roman font
    font_path = "path/to/times_new_roman.ttf"  # Replace with the actual path to your Times New Roman font file
    font_large = pygame.font.Font(font_path, 48)
    font_small = pygame.font.Font(font_path, 36)

    welcome_text = font_large.render("Welcome", True, (0, 0, 0))
    game_name_text = font_large.render("(Name of Game)", True, (0, 0, 0))
    to_text = font_small.render("To", True, (0, 0, 0))

    welcome_rect = welcome_text.get_rect(center=(WIDTH // 2, HEIGHT // 2 - 50))
    game_name_rect = game_name_text.get_rect(center=(WIDTH // 2, HEIGHT // 2))
    to_rect = to_text.get_rect(center=(WIDTH // 2, HEIGHT // 2 + 50))

    screen.blit(welcome_text, welcome_rect)
    screen.blit(game_name_text, game_name_rect)
    screen.blit(to_text, to_rect)

    # Update display
    pygame.display.flip()

    # Cap the frame rate
    clock.tick(FPS)

    # Check for a key press or any other event to proceed to the game
    keys = pygame.key.get_pressed()
    if any(keys):
        intro_running = False

# Stop the introduction music
pygame.mixer.music.stop()

# Game loop (similar to the one in the previous example)
game_running = True
while game_running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_running = False

    # Update game state

    # Draw background
    screen.fill(WHITE)

    # Draw player character
    pygame.draw.rect(screen, (0, 128, 255), (player_x, player_y, player_size, player_size))

    # Update display
    pygame.display.flip()

    # Cap the frame rate
    clock.tick(FPS)

# Quit Pygame
pygame.quit()
sys.exit()
