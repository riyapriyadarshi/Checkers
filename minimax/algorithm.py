from checkers.constants import AI_COLOR, PLAYER_COLOR


def minimax(board, depth, alpha, beta, maximizing_player):
    """
    Alpha-beta pruned Minimax.

    Returns (score, best_board_state)
    """
    if depth == 0 or board.winner() is not None:
        return board.evaluate(), board

    if maximizing_player:
        max_eval = float('-inf')
        best_move = None
        for move in _get_all_moves(board, AI_COLOR):
            evaluation, _ = minimax(move, depth - 1, alpha, beta, False)
            if evaluation > max_eval:
                max_eval  = evaluation
                best_move = move
            alpha = max(alpha, evaluation)
            if beta <= alpha:
                break
        return max_eval, best_move
    else:
        min_eval = float('inf')
        best_move = None
        for move in _get_all_moves(board, PLAYER_COLOR):
            evaluation, _ = minimax(move, depth - 1, alpha, beta, True)
            if evaluation < min_eval:
                min_eval  = evaluation
                best_move = move
            beta = min(beta, evaluation)
            if beta <= alpha:
                break
        return min_eval, best_move

def _get_all_moves(board, color):
    moves = []
    for piece in board.get_all_pieces(color):
        valid_moves = board.get_valid_moves(piece)
        for move, skip in valid_moves.items():
            temp_board = board.copy()
            temp_piece = temp_board.get_piece(piece.row, piece.col)
            new_board  = _simulate_move(temp_piece, move, temp_board, skip)
            moves.append(new_board)
    return moves

def _simulate_move(piece, move, board, skip):
    board.move(piece, move[0], move[1])
    if skip:
        board.remove(skip)
    return board
