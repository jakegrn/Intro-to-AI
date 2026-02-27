"""Alpha-Beta Pruning 

Implement alpha-beta pruning for Tic-Tac-Toe.

Requirements:
  - Implement a recursive search that returns an evaluation score.
  - Use alpha and beta bounds to prune branches.
  - Provide a function to select the best move from a given game state.

"""

from __future__ import annotations
from typing import Optional, Tuple
from tictactoe import TicTacToe, Move, Player

# You may import the Game/Board types used in the provided support code.

class AlphaBetaAI:
    """Alpha-Beta Pruning AI for Tic‑Tac‑Toe."""

    def __init__(self, ai_player: Player = "X") -> None:
        self.ai_player = ai_player

    def alphabeta_value(self, state: TicTacToe, player: Player, alpha: int, beta: int, depth: int = 0) -> int:
        """Return the minimax value of `state` for `player` using alpha-beta pruning.

    
        - Handle terminal states (win/lose/draw).
        - Generate legal moves and recurse.
        - Update alpha/beta and prune when possible.
        """
        
        # Return the minimax value of state for player using Alpha-Beta pruning

        # Safety check to check for infinite recursion. Game should never reach this depth in reality

        if depth > 10:
            raise RuntimeError("Maximum recursion depth exceeded.") 
        
        if state.is_terminal():
            return state.outcome_value()
            
        next_player = state.next_player

        if next_player == player:  # maximiser (AI player)
            value = -2
            for move in state.legal_moves():
                child = state.apply(move)
                val = self.alphabeta_value(child, player, alpha, beta, depth + 1)
                value = max(value, val)
                alpha = max(alpha, value)
                if alpha >= beta:
                    break
            return value
            
        else:  # minimiser (AI opponent)
            value = 2
            for move in state.legal_moves():
                child = state.apply(move)
                val = self.alphabeta_value(child, player, alpha, beta, depth + 1)
                value = min(value, val)
                beta = min(beta, value)
                if alpha >= beta:
                    break
            return value        

    def best_move_alphabeta(self, state: TicTacToe, player: Player) -> Optional[Move]:
        """Return the best move for `player` from `state` using alpha-beta pruning.


        - Iterate legal moves and call alphabeta_value()
        - Track and return the move with the best score
        """

        # Return the best move for player from state after using Alpha-Beta pruning
        
        alpha = -2
        beta = 2
        best_move = None

        if state.next_player == player:
            best_val = -2 
        else:
            best_val = 2

        for move in state.legal_moves():
            child_state = state.apply(move)
            val = self.alphabeta_value(child_state, player, alpha, beta)

            if state.next_player == player:  # maximizer (AI's turn)
                if val > best_val:
                    best_val = val
                    best_move = move
                    alpha = max(alpha, best_val)

            else:  # minimizer (opponent's turn)
                if val < best_val:
                    best_val = val
                    best_move = move
                    beta = min(beta, best_val)

            if alpha >= beta: # pruning condition
                break

        return best_move
    
    def choose_move(self, state: TicTacToe) -> Move:
        return self.best_move_alphabeta(state, self.ai_player)