import pygame
from .board import Board
from .constants import (PLAYER_COLOR, AI_COLOR, SQUARE_SIZE,
                        LIGHT_BROWN, BLACK, HIGHLIGHT)

class Game:
    def __init__(self, win):
        self.win    = win
        self._init()

    def _init(self):
        self.selected     = None
        self.board        = Board()
        self.turn         = PLAYER_COLOR
        self.valid_moves  = {}

    def reset(self):
        self._init()
    def update(self):
        self.board.draw(self.win, self.valid_moves)
        self._draw_selected_highlight()
        pygame.display.update()

    def _draw_selected_highlight(self):
        if self.selected:
            row, col = self.selected.row, self.selected.col
            surf = pygame.Surface((SQUARE_SIZE, SQUARE_SIZE), pygame.SRCALPHA)
            surf.fill((50, 205, 50, 80))
            self.win.blit(surf, (col * SQUARE_SIZE, row * SQUARE_SIZE))

    def select(self, row, col):
        if self.selected:
            result = self._move(row, col)
            if not result:
                self.selected = None
                self.select(row, col)

        piece = self.board.get_piece(row, col)
        if piece and piece.color == self.turn:
            self.selected    = piece
            self.valid_moves = self.board.get_valid_moves(piece)
            return True
        return False
    
    def _move(self, row, col):
        piece = self.board.get_piece(row, col)
        if self.selected and (row, col) in self.valid_moves:
            self.board.move(self.selected, row, col)
            skipped = self.valid_moves[(row, col)]
            if skipped:
                self.board.remove(skipped)
            self.change_turn()
            return True
        return False

    def ai_move(self, board):
        self.board = board
        self.change_turn()

    def change_turn(self):
        self.valid_moves = {}
        self.selected    = None
        self.turn = AI_COLOR if self.turn == PLAYER_COLOR else PLAYER_COLOR

    def get_board(self):
        return self.board

    def winner(self):
        return self.board.winner()
