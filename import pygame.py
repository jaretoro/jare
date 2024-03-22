import pygame
# Define the colors we will use
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
# Define the tetris pieces
PIECES = [
    [
        [0, 0, 0, 0],
        [1, 1, 1, 1],
        [0, 0, 0, 0],
        [0, 0, 0, 0],
    ],
    [
        [0, 0, 0, 0],
        [0, 1, 1, 0],
        [0, 1, 1, 0],
        [0, 0, 0, 0],
    ],
    [
        [0, 0, 0, 0],
        [1, 1, 0, 0],
        [1, 0, 0, 0],
        [1, 0, 0, 0],
    ],
    [
        [0, 0, 0, 0],
        [1, 1, 1, 0],
        [0, 0, 1, 0],
        [0, 0, 0, 0],
    ],
    [
        [0, 0, 0, 0],
        [0, 1, 1, 1],
        [0, 0, 1, 0],
        [0, 0, 0, 0],
    ],
]
# Set up the pygame window
WIDTH = 640
HEIGHT = 480
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
# Create a clock to keep track of the game time
clock = pygame.time.Clock()
# Create a list to store the tetris pieces
pieces = []
# Create a random piece and add it to the list
piece = random.choice(PIECES)
pieces.append(piece)
# Create a variable to keep track of the current score
score = 0
# Start the main loop
while True:
    # Get the current time
    current_time = pygame.time.get_ticks()
    # Check for events
    for event in pygame.event.get():
        # If the user quits the game, exit
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        # If the user presses the space bar, drop the current piece
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            drop_piece(piece)
    # Update the game state
    update_piece(piece, current_time)
    # Check if the piece has collided with anything
    if check_collision(piece):
        # If the piece has collided, remove it from the list and create a new one
        pieces.remove(piece)
        piece = random.choice(PIECES)
        pieces.append(piece)
    # Check if any lines have been cleared
    if check_lines():
        # If any lines have been cleared, increase the score
        score += 1
    # Draw the game to the screen
    draw_grid()
    draw_pieces(pieces)
    pygame.display.update()
    # Slow down the game loop
    clock.tick(60)