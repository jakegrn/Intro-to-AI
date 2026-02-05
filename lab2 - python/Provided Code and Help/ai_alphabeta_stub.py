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

        """ This uses alpha beta pruning. This is an in order binary tree traversal, which
            takes in the state, player type, alpha and beta integers.
            If node is terminal, return score evaluation (+1,0,-1)
            Else
            For each possible move:
                
            

        """
        
        """Return the minimax value of `state` for `player` using alpha-beta pruning."""

        if depth > 10:
            raise RuntimeError("Maximum recursion depth exceeded.")
        
        if state.is_terminal():
            return state.outcome_value()
            
        next_player = state.next_player

        if next_player == player:  # max
            value = -2
            for move in state.legal_moves():
                child = state.apply(move)
                val = self.alphabeta_value(child, player, alpha, beta, depth + 1)
                value = max(value, val)
                alpha = max(alpha, value)
                if alpha >= beta:
                    break
            return value
            
        else:  # min
            value = 2
            for move in state.legal_moves():
                child = state.apply(move)
                val = self.alphabeta_value(child, player, alpha, beta, depth + 1)
                value = min(value, val)
                beta = min(beta, value)
                if alpha >= beta:
                    break
            return value
        #raise NotImplementedError("Student must implement alphabeta_value().")
        

    def best_move_alphabeta(self, state: TicTacToe, player: Player) -> Optional[Move]:
        """Return the best move for `player` from `state` using alpha-beta pruning.


        - Iterate legal moves and call alphabeta_value()
        - Track and return the move with the best score
        """

        """Return the best move for `player` from `state` using alpha-beta pruning."""
        
        alpha, beta = -2, 2
        best_move: Optional[Move] = None
        best_val = -2 if state.next_player == player else 2
        for move in state.legal_moves():
            child = state.apply(move)
            val = self.alphabeta_value(child, player, alpha, beta)

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

            if alpha >= beta:
                break

        return best_move
    
    def choose_move(self, state: TicTacToe) -> Move:
        if state.is_terminal():
            raise ValueError("Game is already over.")
        if state.next_player != self.ai_player:
            raise ValueError("It is not the AI's turn.")

        move = self.best_move_alphabeta(state, self.ai_player)
        if move is None:
            raise ValueError("No legal moves available.")
        return move