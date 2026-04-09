import pygame
import sys
from checkers.constants import WIDTH, HEIGHT, SQUARE_SIZE, AI_COLOR
from checkers.game       import Game
from minimax.algorithm   import minimax

FPS         = 60
AI_DEPTH    = 4          
FONT_NAME   = "freesansbold.ttf"

def get_row_col_from_mouse(pos):
    x, y = pos
    row = y // SQUARE_SIZE
    col = x // SQUARE_SIZE
    return row, col


def draw_winner_screen(win, winner):
    overlay = pygame.Surface((WIDTH, HEIGHT), pygame.SRCALPHA)
    overlay.fill((0, 0, 0, 160))
    win.blit(overlay, (0, 0))

    font_big   = pygame.font.SysFont("freesansbold.ttf", 72)
    font_small = pygame.font.SysFont("freesansbold.ttf", 36)

    if winner == "RED":
        msg   = "YOU WIN!"
        color = (220, 80, 80)
    else:
        msg   = "AI WINS!"
        color = (220, 220, 180)

    text      = font_big.render(msg,    True, color)
    sub_text  = font_small.render("Press R to restart or Q to quit", True, (200, 200, 200))

    win.blit(text,     (WIDTH // 2 - text.get_width()     // 2, HEIGHT // 2 - 60))
    win.blit(sub_text, (WIDTH // 2 - sub_text.get_width() // 2, HEIGHT // 2 + 30))
    pygame.display.update()


def draw_hud(win, turn_label):
    font  = pygame.font.SysFont("freesansbold.ttf", 22)
    label = font.render(f"Turn: {turn_label}", True, (255, 230, 150))
    win.blit(label, (10, 10))

def main():
    pygame.init()
    win   = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Checkers — Minimax AI")
    clock = pygame.time.Clock()
    game  = Game(win)

    game_over    = False
    winner_label = None

    while True:
        clock.tick(FPS)

        if game.turn == AI_COLOR and not game_over:
            pygame.display.set_caption("Checkers — AI Thinking…")
            _, new_board = minimax(game.get_board(), AI_DEPTH,
                                   float('-inf'), float('inf'), True)
            if new_board:
                game.ai_move(new_board)
            pygame.display.set_caption("Checkers — Minimax AI")

        if game.winner() and not game_over:
            winner_label = game.winner()
            game_over    = True

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    game.reset()
                    game_over    = False
                    winner_label = None
                if event.key == pygame.K_q:
                    pygame.quit()
                    sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN and not game_over:
                pos = pygame.mouse.get_pos()
                row, col = get_row_col_from_mouse(pos)
                game.select(row, col)

        game.update()

        if game_over:
            draw_winner_screen(win, winner_label)


if __name__ == "__main__":
    main()
