# Checkers — Minimax AI (Pygame)

A graphical Checkers game with an AI opponent powered by the **Minimax algorithm with Alpha-Beta pruning**.

---

## Project Structure

```
checkers_game/
├── main.py                  # Entry point – game loop & window
├── requirements.txt
├── assets/                  # (optional) images / sounds
├── checkers/
│   ├── __init__.py
│   ├── constants.py         # Colors, dimensions, player IDs
│   ├── piece.py             # Piece class (draw, move, king)
│   ├── board.py             # Board class (draw, moves, eval, copy)
│   └── game.py              # Game class (select, AI move, turn)
└── minimax/
    ├── __init__.py
    └── algorithm.py         # Minimax + Alpha-Beta pruning
```

---


## How to Play

| Action          | Control                        |
|-----------------|--------------------------------|
| Select piece    | Left-click on your piece (RED) |
| Move piece      | Left-click on a green dot      |
| Restart game    | Press **R**                    |
| Quit            | Press **Q** or close window    |

- You play as **RED** (bottom), AI plays as **WHITE** (top).
- Pieces become **Kings** (gold center) when they reach the opposite end.
- Kings can move both forward and backward.

---

## AI Difficulty

Edit `AI_DEPTH` in `main.py`:

```python
AI_DEPTH = 4   # 3 = easy, 4 = medium, 5 = hard (slower)
```

---

## Key Concepts Demonstrated

- **Object-Oriented Programming** — `Piece`, `Board`, `Game` classes
- **Game State Management** — full board copy for look-ahead search
- **Pygame GUI** — wooden board, highlighted moves, winner overlay
- **Minimax + Alpha-Beta Pruning** — optimal AI decision-making
