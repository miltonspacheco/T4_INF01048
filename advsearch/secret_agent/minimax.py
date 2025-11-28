import random
from typing import Tuple, Callable


def _alphabeta(state, max_depth: int, depth: int, alpha: float, beta: float, 
               eval_func: Callable, root_player: str) -> Tuple[float, Tuple[int, int]]:
    """
    Função auxiliar recursiva que implementa minimax com poda alfa-beta
    """
    if state.is_terminal() or (max_depth != -1 and depth >= max_depth):
        value = eval_func(state, root_player)
        return value, None

    legal_moves = list(state.legal_moves())
    
    if not legal_moves:
        value = eval_func(state, root_player)
        return value, None
    
    is_maximizing = (state.player == root_player)    
    best_move = None
    best_value = float('-inf') if is_maximizing else float('inf')
    
    for move in legal_moves:
        next_state = state.next_state(move)
        value, _ = _alphabeta(next_state, max_depth, depth + 1, alpha, beta, eval_func, root_player)
        if is_maximizing:
            if value > best_value:
                best_value = value
                best_move = move
            alpha = max(alpha, best_value)
            if beta <= alpha:
                break
        else:
            if value < best_value:
                best_value = value
                best_move = move
            beta = min(beta, best_value)
            # Para para fazer poda alfa-beta
            if beta <= alpha:
                break

    if depth == 0:
        return best_value, best_move
    else:
        return best_value, None


def minimax_move(state, max_depth:int, eval_func:Callable) -> Tuple[int, int]:
    """
    Returns a move computed by the minimax algorithm with alpha-beta pruning for the given game state.
    :param state: state to make the move (instance of GameState)
    :param max_depth: maximum depth of search (-1 = unlimited)
    :param eval_func: the function to evaluate a terminal or leaf state (when search is interrupted at max_depth)
                    This function should take a GameState object and a string identifying the player,
                    and should return a float value representing the utility of the state for the player.
    :return: (int, int) tuple with x, y coordinates of the move (remember: 0 is the first row/column)
    """
    root_player = state.player
    _, best_move = _alphabeta(state, max_depth, 0, float('-inf'), float('inf'), 
                              eval_func, root_player)
    return best_move
