import pygame
from .constants import (BLACK, WHITE, RED, SQUARE_SIZE, ROWS, COLS,
                        LIGHT_BROWN, DARK_BROWN, BOARD_BORDER,
                        MOVE_DOT, PLAYER_COLOR, AI_COLOR)
from .piece import Piece


class Board:
    def __init__(self):
        self.board = []
        self.red_left = self.white_left = 12
        self.red_kings = self.white_kings = 0
        self._create_board()

    def draw_squares(self, win):
        win.fill(BOARD_BORDER)
        for row in range(ROWS):
            for col in range(COLS):
                color = LIGHT_BROWN if (row + col) % 2 == 0 else DARK_BROWN
                pygame.draw.rect(win, color,
                                 (col * SQUARE_SIZE, row * SQUARE_SIZE,
                                  SQUARE_SIZE, SQUARE_SIZE))

    def draw(self, win, valid_moves=None):
        self.draw_squares(win)
        if valid_moves:
            self._draw_valid_moves(win, valid_moves)
        for row in range(ROWS):
            for col in range(COLS):
                piece = self.board[row][col]
                if piece:
                    piece.draw(win)

    def _draw_valid_moves(self, win, moves):
        for move in moves:
            row, col = move
            cx = col * SQUARE_SIZE + SQUARE_SIZE // 2
            cy = row * SQUARE_SIZE + SQUARE_SIZE // 2
            pygame.draw.circle(win, MOVE_DOT, (cx, cy), 15)
    def _create_board(self):
        for row in range(ROWS):
            self.board.append([])
            for col in range(COLS):
                if col % 2 == ((row + 1) % 2):
                    if row < 3:
                        self.board[row].append(Piece(row, col, AI_COLOR))
                    elif row > 4:
                        self.board[row].append(Piece(row, col, PLAYER_COLOR))
                    else:
                        self.board[row].append(0)
                else:
                    self.board[row].append(0)

    def get_piece(self, row, col):
        return self.board[row][col]

    def get_all_pieces(self, color):
        pieces = []
        for row in self.board:
            for piece in row:
                if piece and piece.color == color:
                    pieces.append(piece)
        return pieces

    def move(self, piece, row, col):
        self.board[piece.row][piece.col], self.board[row][col] = \
            self.board[row][col], self.board[piece.row][piece.col]
        piece.move(row, col)

        # Promotion to king
        if row == ROWS - 1 and piece.color == AI_COLOR:
            piece.make_king()
            self.white_kings += 1
        if row == 0 and piece.color == PLAYER_COLOR:
            piece.make_king()
            self.red_kings += 1

    def remove(self, pieces):
        for piece in pieces:
            self.board[piece.row][piece.col] = 0
            if piece.color == PLAYER_COLOR:
                self.red_left -= 1
            else:
                self.white_left -= 1

    def get_valid_moves(self, piece):
        moves = {}
        left  = piece.col - 1
        right = piece.col + 1
        row   = piece.row

        if piece.color == PLAYER_COLOR or piece.king:
            moves.update(self._traverse_left (row - 1, max(row - 3, -1), -1, piece.color, left))
            moves.update(self._traverse_right(row - 1, max(row - 3, -1), -1, piece.color, right))
        if piece.color == AI_COLOR or piece.king:
            moves.update(self._traverse_left (row + 1, min(row + 3, ROWS), 1, piece.color, left))
            moves.update(self._traverse_right(row + 1, min(row + 3, ROWS), 1, piece.color, right))
        return moves

    def _traverse_left(self, start, stop, step, color, left, skipped=[]):
        moves = {}
        last  = []
        for r in range(start, stop, step):
            if left < 0:
                break
            current = self.board[r][left]
            if current == 0:
                if skipped and not last:
                    break
                elif skipped:
                    moves[(r, left)] = last + skipped
                else:
                    moves[(r, left)] = last
                if last:
                    row = max(r - 3, -1) if step == -1 else min(r + 3, ROWS)
                    moves.update(self._traverse_left (r + step, row, step, color, left  - 1, skipped=last + skipped))
                    moves.update(self._traverse_right(r + step, row, step, color, left  + 1, skipped=last + skipped))
                break
            elif current.color == color:
                break
            else:
                last = [current]
            left -= 1
        return moves

    def _traverse_right(self, start, stop, step, color, right, skipped=[]):
        moves = {}
        last  = []
        for r in range(start, stop, step):
            if right >= COLS:
                break
            current = self.board[r][right]
            if current == 0:
                if skipped and not last:
                    break
                elif skipped:
                    moves[(r, right)] = last + skipped
                else:
                    moves[(r, right)] = last
                if last:
                    row = max(r - 3, -1) if step == -1 else min(r + 3, ROWS)
                    moves.update(self._traverse_left (r + step, row, step, color, right - 1, skipped=last + skipped))
                    moves.update(self._traverse_right(r + step, row, step, color, right + 1, skipped=last + skipped))
                break
            elif current.color == color:
                break
            else:
                last = [current]
            right += 1
        return moves

    def evaluate(self):
        return (self.white_left - self.red_left +
                (self.white_kings * 0.5 - self.red_kings * 0.5))

    def copy(self):
        new_board = Board()
        new_board.board = []
        for row in self.board:
            new_row = []
            for piece in row:
                if piece:
                    new_piece = Piece(piece.row, piece.col, piece.color)
                    new_piece.king = piece.king
                    new_row.append(new_piece)
                else:
                    new_row.append(0)
            new_board.board.append(new_row)
        new_board.red_left    = self.red_left
        new_board.white_left  = self.white_left
        new_board.red_kings   = self.red_kings
        new_board.white_kings = self.white_kings
        return new_board
    def winner(self):
        if self.red_left   <= 0:
            return "WHITE"
        if self.white_left <= 0:
            return "RED"
        return None
