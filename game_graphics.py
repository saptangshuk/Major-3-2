import pygame
import math

# Define color constants
WHITE = (255, 255, 255)
LIGHT_BLUE = (173, 216, 230)
BROWN = (139, 69, 19)
GRAY = (100, 100, 100)
BLACK = (0, 0, 0)

# Radius for the nodes
NODE_RADIUS = 30

# Constants for the exit button dimensions and position
EXIT_BUTTON_WIDTH = 200
EXIT_BUTTON_HEIGHT = 70
EXIT_BUTTON_X = 20
EXIT_BUTTON_Y = 20

def game_graphics_loop(screen, graph, cat, mouse, node_positions):
    """The main loop responsible for updating graphics for the game."""
    clock = pygame.time.Clock()

    # Fill screen with white background
    screen.fill(WHITE)
    
    # Draw graph edges and nodes
    draw_edges(screen, graph, node_positions)
    draw_nodes(screen, graph, node_positions, cat, mouse)

    # Draw exit button
    exit_button = pygame.Rect(EXIT_BUTTON_X, EXIT_BUTTON_Y, EXIT_BUTTON_WIDTH, EXIT_BUTTON_HEIGHT)
    pygame.draw.rect(screen, LIGHT_BLUE, exit_button)
    font = pygame.font.Font(None, 74)
    text = font.render('Exit', True, BLACK)
    screen.blit(text, (exit_button.x + exit_button.width // 4, exit_button.y + exit_button.height // 4))

    # Refresh screen
    pygame.display.flip()
    
    # Limit frames per second
    clock.tick(60)

def draw_game(screen, graph, cat=None, mouse=None):
    """Function to draw the entire game screen, including the graph, nodes, cat, and mouse."""
    screen_width, screen_height = screen.get_size()
    
    # Distribute nodes evenly on the screen
    node_positions = {}
    angle = 2 * math.pi / len(graph)
    center_x, center_y = screen_width // 2, screen_height // 2
    radius = min(screen_width, screen_height) * 0.4
    for i, node in enumerate(graph):
        x = center_x + radius * math.cos(i * angle)
        y = center_y + radius * math.sin(i * angle)
        node_positions[node] = (x, y)

    game_graphics_loop(screen, graph, cat, mouse, node_positions)

    return node_positions

def draw_edges(screen, graph, node_positions):
    """Draws the edges between nodes based on the graph structure."""
    for node, neighbors in graph.items():
        for neighbor in neighbors:
            pygame.draw.line(screen, GRAY, node_positions[node], node_positions[neighbor], 2)

def draw_nodes(screen, graph, node_positions, cat=None, mouse=None):
    """Draws nodes, cat, and mouse on the screen."""
    for node in graph:
        if node == cat:
            pygame.draw.circle(screen, LIGHT_BLUE, (int(node_positions[node][0]), int(node_positions[node][1])), NODE_RADIUS)
        elif node == mouse:
            pygame.draw.circle(screen, BROWN, (int(node_positions[node][0]), int(node_positions[node][1])), NODE_RADIUS)
        else:
            pygame.draw.circle(screen, GRAY, (int(node_positions[node][0]), int(node_positions[node][1])), NODE_RADIUS)
            
        # Draw node numbers on top of the nodes for easier identification
        font = pygame.font.Font(None, 36)
        text = font.render(str(node), True, BLACK)
        screen.blit(text, (node_positions[node][0] - text.get_width() // 2, node_positions[node][1] - text.get_height() // 2))

def get_clicked_node(pos, node_positions):
    """Returns the node clicked on or None if no node was clicked."""
    for node, position in node_positions.items():
        distance = math.sqrt((position[0] - pos[0]) ** 2 + (position[1] - pos[1]) ** 2)
        if distance <= NODE_RADIUS:
            return node
    return None
