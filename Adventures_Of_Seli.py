import pygame
import sys

# Initialize Pygame and Pygame mixer
pygame.init()
pygame.mixer.init()

# Define constants
WIDTH, HEIGHT = 1100, 800
FPS = 60

# Set up the game window
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Adventure Game")

# Define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Load introduction music
pygame.mixer.music.load("intro_music.mp3")
pygame.mixer.music.set_volume(0.5)  # Adjust the volume (0.0 to 1.0)
pygame.mixer.music.play(-1)  # -1 makes the music loop indefinitely

# Load the image
image = pygame.image.load("background_image.png")  # Replace with the actual image file path
image = pygame.transform.scale(image, (WIDTH, HEIGHT))  # Resize the image to fit the screen

# Create the player character
player_size = 50
player_x = WIDTH // 2 - player_size // 2
player_y = HEIGHT - player_size - 10

# Set up clock for controlling the frame rate
clock = pygame.time.Clock()

# Introduction variables
intro_running = True
text_x = -WIDTH  # Initial x-coordinate for the text (off-screen to the left)
text_speed = 5  # Adjust the speed of the text movement
intro_start_time = pygame.time.get_ticks()  # Record the start time of the intro

# Menu variables
menu_font = pygame.font.Font("fonts/Gothic Bozo.ttf", 36)  # Use Gothic Bozo font for the menu text
menu_text_color = WHITE
menu_running = False

# Times New Roman font for the New Game buttons and progress text
times_new_roman_font = pygame.font.Font("fonts/Typography Times Regular.ttf", 20)

# Cut scene variables
cut_scene_images = [
    pygame.image.load("cut_scene_image_1.webp"),
    pygame.image.load("cut_scene_image_2.webp"),
    pygame.image.load("cut_scene_image_3.webp"),
    pygame.image.load("cut_scene_image_4.webp")
]  # Add your cut scene images to this list
cut_scene_text = [
    "In the mystical land of Eldoria, a brave adventurer named Seli embarks on a journey.",
    "He discovers an ancient prophecy that foretells of a hidden artifact deep within the Old Forest.",
    "Facing perilous challenges, Seli uncovers the artifact's secrets and gains newfound powers.",
    "As the journey continues, Seli must confront the dark forces threatening Eldoria's balance."
]
cut_scene_duration = 3000  # Time in milliseconds for each cut scene image
cut_scene_index = 0
cut_scene_timer = pygame.time.get_ticks()
cut_scene_running = False

# Game loop (similar to the one in the previous example)
game_running = True
while game_running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_running = False

        # Check for mouse clicks
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            mouse_x, mouse_y = pygame.mouse.get_pos()

            # Check if the mouse click is within the New Game buttons
            for i in range(3):
                button_rect = pygame.Rect(50, HEIGHT // 2 - 75 + (75 * i), 200, 50)
                if button_rect.collidepoint(mouse_x, mouse_y):
                    intro_running = False
                    menu_running = True
                    cut_scene_running = True

    if intro_running and pygame.time.get_ticks() - intro_start_time >= 5000:
        intro_running = False
        menu_running = True

    if menu_running:
        # Draw menu background
        screen.fill(BLACK)

        # Add text at the middle top of the window with Gothic Bozo font
        menu_text = menu_font.render("Start a new adventure", True, menu_text_color)
        menu_text_rect = menu_text.get_rect(center=(WIDTH // 2, HEIGHT // 4))
        screen.blit(menu_text, menu_text_rect)

        if not cut_scene_running:  # Only draw buttons if the cut scene is not running
            # Add buttons
            button_height = 50
            button_spacing = 20
            button_y = HEIGHT // 2 - (button_height * 3 + button_spacing * 2) // 2

            for i in range(3):
                button_rect = pygame.Rect(50, button_y + (button_height + button_spacing) * i, 200, button_height)
                pygame.draw.rect(screen, WHITE, button_rect)

                button_text = times_new_roman_font.render(f"New Game {i + 1}", True, BLACK)
                button_text_rect = button_text.get_rect(center=button_rect.center)
                screen.blit(button_text, button_text_rect)

                progress_text = times_new_roman_font.render("Progress: 0%", True, WHITE)
                progress_text_rect = progress_text.get_rect(midleft=(button_rect.right + 10, button_rect.centery))
                screen.blit(progress_text, progress_text_rect)

    else:
        # Draw introduction screen with the image
        screen.blit(image, (0, 0))

        # Add a customized welcome message with Gothic Bozo font
        font_path = "fonts/Gothic Bozo.ttf"  # Replace with the actual path to your Gothic Bozo font file
        font_large = pygame.font.Font(font_path, 50)
        font_small = pygame.font.Font(font_path, 40)

        welcome_text = font_large.render("Welcome", True, WHITE)
        to_text = font_small.render("To", True, WHITE)
        game_name_text = font_large.render("The Adventures of Seli!", True, WHITE)

        welcome_rect = welcome_text.get_rect(center=(text_x + WIDTH // 2, HEIGHT // 2 - 50))
        to_rect = to_text.get_rect(center=(text_x + WIDTH // 2, HEIGHT // 2))
        game_name_rect = game_name_text.get_rect(center=(text_x + WIDTH // 2, HEIGHT // 2 + 50))

        screen.blit(welcome_text, welcome_rect)
        screen.blit(to_text, to_rect)
        screen.blit(game_name_text, game_name_rect)

        # Update text position
        text_x += text_speed

        # If the text reaches the middle, stop moving
        if text_x >= WIDTH // 2 - game_name_rect.width // 2:
            text_x = WIDTH // 2 - game_name_rect.width // 2

    # Cut scene logic
    if cut_scene_running:
        current_time = pygame.time.get_ticks()
        if current_time - cut_scene_timer >= cut_scene_duration:
            cut_scene_index = (cut_scene_index + 1) % len(cut_scene_images)
            cut_scene_timer = current_time

        # Draw the scene
        if cut_scene_running:
            # Draw cut scene
            screen.blit(cut_scene_images[cut_scene_index], (0, 0))

            # Add text at the bottom of the window with Times New Roman font
            cut_scene_text_surface = times_new_roman_font.render(cut_scene_text[cut_scene_index], True, WHITE)
            cut_scene_text_rect = cut_scene_text_surface.get_rect(center=(WIDTH // 2, HEIGHT - 20))
            screen.blit(cut_scene_text_surface, cut_scene_text_rect)

    # Update display
    pygame.display.flip()

    # Cap the frame rate
    clock.tick(FPS)

# Stop the introduction music
pygame.mixer.music.stop()

# Quit Pygame
pygame.quit()
sys.exit()
