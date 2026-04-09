import pygame

# Window
WIDTH, HEIGHT = 800, 800
ROWS, COLS = 8, 8
SQUARE_SIZE = WIDTH // COLS

# Colors
RED         = (200, 50,  50)
WHITE       = (240, 235, 220)
BLACK       = (30,  20,  10)
BLUE        = (50,  120, 200)
GREY        = (150, 150, 150)

# Board colors (wooden style)
LIGHT_BROWN = (240, 200, 140)
DARK_BROWN  = (100,  60,  20)
BOARD_BORDER= ( 60,  30,   5)

# Crown (king) marker color
CROWN_COLOR = (255, 215,   0)   # gold

# Highlight / selection
HIGHLIGHT   = ( 50, 205,  50, 160)   # semi-transparent green
MOVE_DOT    = ( 50, 205,  50)

# Player identifiers
PLAYER_COLOR = RED
AI_COLOR     = WHITE
