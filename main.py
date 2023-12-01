import pygame
from game_mechanics import generate_random_graph, spawn_cat_mouse, cat_strategy
from game_graphics import draw_game, get_clicked_node

# Initialize the pygame environment
pygame.init()

# Define constants for the graph's structure
N_NODES = 10
EDGE_PROB = 0.4

# Generate a random graph and spawn cat & mouse
graph = generate_random_graph(N_NODES, EDGE_PROB)
cat, mouse = spawn_cat_mouse(graph)

# Set up a fullscreen display
screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN | pygame.DOUBLEBUF)

# Define coordinates and dimensions for the exit button
EXIT_BUTTON_X = 20
EXIT_BUTTON_Y = 20
EXIT_BUTTON_WIDTH = 200
EXIT_BUTTON_HEIGHT = 70
exit_button = pygame.Rect(EXIT_BUTTON_X, EXIT_BUTTON_Y, EXIT_BUTTON_WIDTH, EXIT_BUTTON_HEIGHT)

def start_screen():
    """Displays the starting screen of the game."""
    running = True
    while running:
        # Fill the screen with a white background
        screen.fill((255, 255, 255))

        # Display game title
        font = pygame.font.Font(None, 74)
        text = font.render('Cat and Mouse Game', True, (0, 0, 0))
        screen.blit(text, (screen.get_width() // 2 - text.get_width() // 2, screen.get_height() // 3))
        
        # Draw the start button
        pygame.draw.rect(screen, (0, 128, 0), exit_button)
        text = font.render('Start', True, (255, 255, 255))
        screen.blit(text, (exit_button.x + exit_button.width // 4, exit_button.y + exit_button.height // 4))

        # Update the display
        pygame.display.flip()

        # Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if exit_button.collidepoint(event.pos):
                    return True

def end_screen():
    """Displays the ending screen of the game when the cat catches the mouse."""
    running = True
    while running:
        # Fill the screen with a white background
        screen.fill((255, 255, 255))

        # Display end message
        font = pygame.font.Font(None, 74)
        text = font.render('Cat Wins!', True, (255, 0, 0))
        screen.blit(text, (screen.get_width() // 2 - text.get_width() // 2, screen.get_height() // 3))
        
        # Draw the exit button
        pygame.draw.rect(screen, (0, 128, 0), exit_button)
        text = font.render('Exit', True, (255, 255, 255))
        screen.blit(text, (exit_button.x + exit_button.width // 4, exit_button.y + exit_button.height // 4))
        
        # Update the display
        pygame.display.flip()

        # Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if exit_button.collidepoint(event.pos):
                    return

# If player starts the game from the start screen
if start_screen():
    # Draw the initial game state
    node_positions = draw_game(screen, graph)

    # Main game loop
    game_running = True
    while game_running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if exit_button.collidepoint(event.pos):
                    game_running = False
                else:
                    # Determine if a node was clicked
                    clicked_node = get_clicked_node(event.pos, node_positions)
                    if clicked_node is not None and clicked_node != cat and clicked_node in graph[mouse]:
                        # Move mouse and then cat
                        mouse = clicked_node
                        cat = cat_strategy(cat, mouse, graph)
                        if cat == mouse:
                            # Cat caught the mouse
                            print("Cat caught the Mouse!")
                            game_running = False
        
        # Redraw game state
        draw_game(screen, graph, cat, mouse)

    # Show the ending screen
    end_screen()

# Clean up and close the game
pygame.quit()
