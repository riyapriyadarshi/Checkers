import pygame
from .constants import SQUARE_SIZE, CROWN_COLOR, BLACK

PADDING   = 15
OUTLINE   = 4
CROWN_R   = 12   # radius of the crown circle indicator


class Piece:
    def __init__(self, row, col, color):
        self.row   = row
        self.col   = col
        self.color = color
        self.king  = False
        self.x = 0
        self.y = 0
        self.calc_pos()
        
    def calc_pos(self):
        self.x = SQUARE_SIZE * self.col + SQUARE_SIZE // 2
        self.y = SQUARE_SIZE * self.row + SQUARE_SIZE // 2

    def make_king(self):
        self.king = True

    def draw(self, win):
        radius = SQUARE_SIZE // 2 - PADDING

        # Shadow
        pygame.draw.circle(win, BLACK,
                           (self.x + 3, self.y + 3), radius + OUTLINE)
        # Outline ring
        pygame.draw.circle(win, BLACK, (self.x, self.y), radius + OUTLINE)
        # Body
        pygame.draw.circle(win, self.color, (self.x, self.y), radius)

        # King indicator – golden crown circle
        if self.king:
            pygame.draw.circle(win, CROWN_COLOR, (self.x, self.y), CROWN_R)
            pygame.draw.circle(win, BLACK,       (self.x, self.y), CROWN_R, 2)

    def move(self, row, col):
        self.row = row
        self.col = col
        self.calc_pos()
        
    def __repr__(self):
        return f"Piece({self.row},{self.col}, {'K' if self.king else 'P'}, {self.color})"
