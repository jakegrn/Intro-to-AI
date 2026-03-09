"""Alpha-Beta Pruning 

Implement alpha-beta pruning for Tic-Tac-Toe.

Requirements:
  - Implement a recursive search that returns an evaluation score.
  - Use alpha and beta bounds to prune branches.
  - Provide a function to select the best move from a given game state.

"""

from __future__ import annotations
from typing import Optional, Tuple

# You may import the Game/Board types used in the provided support code.



def alphabeta_value(state: GameState, player: Player, alpha: int, beta: int) -> int:
    """Return the minimax value of `state` for `player` using alpha-beta pruning.

  
      - Handle terminal states (win/lose/draw).
      - Generate legal moves and recurse.
      - Update alpha/beta and prune when possible.
    """
    raise NotImplementedError("Student must implement alphabeta_value().")


def best_move_alphabeta(state: GameState, player: Player) -> Optional[Move]:
    """Return the best move for `player` from `state` using alpha-beta pruning.


      - Iterate legal moves and call alphabeta_value()
      - Track and return the move with the best score
    """
    raise NotImplementedError("Student must implement best_move_alphabeta().")
