from __future__ import annotations

from dataclasses import dataclass
from typing import List, Tuple

from tictactoe import TicTacToe, Move, Player


@dataclass
class MinimaxAI:
    """Minimax AI for Tic‑Tac‑Toe (no alpha‑beta pruning).

    The AI assumes:
    - 'X' is the maximizing player
    - 'O' is the minimizing player
    """

    ai_player: Player = "X"

    def choose_move(self, state: TicTacToe) -> Move:
        if state.is_terminal():
            raise ValueError("Game is already over.")
        if state.next_player != self.ai_player:
            raise ValueError("It is not the AI's turn.")

        best_move: Move = -1
        best_value = float("-inf") if self.ai_player == "X" else float("inf")

        for move in state.legal_moves():
            child = state.apply(move)
            value = self.minimax(child)

            if self.ai_player == "X":
                if value > best_value:
                    best_value = value
                    best_move = move
            else:
                if value < best_value:
                    best_value = value
                    best_move = move

        return best_move

    def minimax(self, state: TicTacToe) -> int:
        """Return the minimax value of the given state.

        Terminal states are assigned:
        - +1 if X has won
        - -1 if O has won
        - 0 if draw

        Recurrence:
        - If it's X to move: value = max(minimax(child) for child in successors)
        - If it's O to move: value = min(minimax(child) for child in successors)
        """
        # Base case: if the state is terminal, return its utility value.
        if state.is_terminal():
            return state.outcome_value()

        # Recursive case: explore all successor states.
        if state.next_player == "X":
            best = float("-inf")
            for move in state.legal_moves():
                best = max(best, self.minimax(state.apply(move)))
            return int(best)
        else:
            best = float("inf")
            for move in state.legal_moves():
                best = min(best, self.minimax(state.apply(move)))
            return int(best)
