import random
from typing import Tuple
from ..othello.gamestate import GameState
from ..othello.board import Board
from .minimax import minimax_move

# Continuamos usando a máscara para dar valor aos tiles
EVAL_TEMPLATE = [
    [100, -30, 6, 2, 2, 6, -30, 100],
    [-30, -50, 1, 1, 1, 1, -50, -30],
    [  6,   1, 1, 1, 1, 1,   1,   6],
    [  2,   1, 1, 3, 3, 1,   1,   2],
    [  2,   1, 1, 3, 3, 1,   1,   2],
    [  6,   1, 1, 1, 1, 1,   1,   6],
    [-30, -50, 1, 1, 1, 1, -50, -30],
    [100, -30, 6, 2, 2, 6, -30, 100]
]

# Mapeamento dos corners e das extremidades
CORNERS = {(0,0), (0,7), (7,0), (7,7)}
EDGES = {(0,i) for i in range(8)} | {(7,i) for i in range(8)} | \
        {(i,0) for i in range(8)} | {(i,7) for i in range(8)}



def make_move(state) -> Tuple[int, int]:
    """
    Returns a move for the given game state
    :param state: state to make the move
    :return: (int, int) tuple with x, y coordinates of the move (remember: 0 is the first row/column)
    """

    # o codigo abaixo apenas retorna um movimento aleatorio valido para
    # a primeira jogada 
    # Remova-o e coloque uma chamada para o minimax_move (que vc implementara' no modulo minimax).
    # A chamada a minimax_move deve receber sua funcao evaluate como parametro.

    return minimax_move(state, max_depth=3, eval_func=evaluate_custom)


def evaluate_custom(state: GameState, player:str) -> float:
    """
    A heuristica que combina mobilidade, pesos posicionais e posições conringa
    """
    board = state.get_board()
    adv = 'B' if player == 'W' else 'W'

    # --- 1. Mobilidade
    player_moves = len(state.legal_moves()) if state.player == player else \
                   len(board.legal_moves(player))
    adv_moves = len(board.legal_moves(adv))

    mobility_score = 0
    if player_moves + adv_moves != 0:
        mobility_score = 100 * (player_moves - adv_moves) / (player_moves + adv_moves)

    # --- 2. Mask (usada previamente)
    positional_score = 0
    for r in range(8):
        for c in range(8):
            v = board.tiles[r][c]
            if v == player:
                positional_score += EVAL_TEMPLATE[r][c]
            elif v == adv:
                positional_score -= EVAL_TEMPLATE[r][c]

    # --- 3. Corner + edge
    corner_score = 0

    for (r, c) in CORNERS:
        v = board.tiles[r][c]
        if v == player:
            corner_score += 200
        elif v == adv:
            corner_score -= 200

    edge_score = 0
    for (r, c) in EDGES:
        v = board.tiles[r][c]
        if v == player:
            edge_score += 10
        elif v == adv:
            edge_score -= 10

    # --- Weighted combination ----------------------------------
    # Tuned weights for a depth-10 minimax:
    # Mobility:           40%
    # Positional mask:    40%
    # Corners/edges:      20%
    total = (
        0.4 * mobility_score +
        0.4 * positional_score +
        0.2 * (corner_score + edge_score)
    )

    return total