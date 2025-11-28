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
    # Mobilidade é quantas jogadas disponiveis temos se fossemos jogar nesse
    player_moves = len(board.legal_moves(player))
    adv_moves    = len(board.legal_moves(adv))

    mobility_score = 0
    if player_moves + adv_moves != 0:
        # Multiplica por 100 para se comparar com o positional_score
        # score de mobilidade: diferença/total de movimentos
        mobility_score = 100 * (player_moves - adv_moves) / (player_moves + adv_moves)

    # --- 2. Mask (usada previamente)
    positional_score = 0
    for r, row in enumerate(board.tiles):
        for c, tile in enumerate(row):
            if tile == player:
                positional_score+=EVAL_TEMPLATE[r][c]
            if tile == adv:
                positional_score-=EVAL_TEMPLATE[r][c]
        

    # --- Combinação dos dois scores
    total = mobility_score+positional_score
    return total