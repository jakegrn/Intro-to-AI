from __future__ import annotations

from dataclasses import dataclass
from typing import List, Tuple

from tictactoe import TicTacToe, Move, Player, WIN_LINES


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
            value = self.minimax(child, depth=0)

            if self.ai_player == "X":
                if value > best_value:
                    best_value = value
                    best_move = move
            else:
                if value < best_value:
                    best_value = value
                    best_move = move

        return best_move

    def minimax(self, state: TicTacToe, depth: int) -> int:
        """Return the minimax value of the given state.

        Terminal states are assigned:
        - +1 if X has won
        - -1 if O has won
        - 0 if draw

        Recurrence:
        - If it's X to move: value = max(minimax(child) for child in successors)
        - If it's O to move: value = min(minimax(child) for child in successors)
        """
        if state.is_terminal():
            return state.outcome_value()

        # Task 3 of assignment involves returning the heuristic evaluation of the state, since a full search is impractical at endgame.
        # Therefore this is replaced with the recursive minimax search until a certain depth, at which point the heuristic evaluation is returned instead.

        if state.next_player == "X":
            best = float("-inf")
            for move in state.legal_moves():
                if depth <= 6:
                    best = max(best, self.heuristic(state.apply(move)))
                else:
                    best = max(best, self.minimax(state.apply(move), depth + 1))
            return int(best)
        else:
            best = float("inf")
            for move in state.legal_moves():
                if depth <= 6:
                    best = min(best, self.heuristic(state.apply(move)))
                else:
                    best = min(best, self.minimax(state.apply(move), depth + 1))
            return int(best)
        
    def heuristic(self, state: TicTacToe) -> int:

            """
            Heuristic evaluation of non terminal states.

            This happens by:
                - Searching through all possible winning lines in state (edited in tictactoe), and retreives the state of the 3 cells in that line.
                - If line is contested (e.g X,O,O) then that winning line is skipped.
                - Else, count how many X's (maximizing player) and O's (minimizing player) are in the line, add to the score according to the following rules:
                    - 1 X contributes +1 to the score
                    - 2 X's contributes +10 to the score
                    - 1 O contributes -1 to the score
                    - 2 O's contributes -10 to the score
                - Return the total score of the state, which is positive if it's favorable to X and negative if it's favorable to O.
            """

            # delegate terminal evaluation so callers don't have to check again
            if state.is_terminal():
                return state.outcome_value()

            score = 0
            # examine all potential winning triples
            for a, b, c in WIN_LINES:
                cells = [state.board[a], state.board[b], state.board[c]]

                # a contested line is worthless
                if "X" in cells and "O" in cells:
                    continue

                x_count = cells.count("X")
                o_count = cells.count("O")

                if x_count == 1:
                    score += 1
                elif x_count == 2:
                    score += 10
                elif o_count == 1:
                    score -= 1
                elif o_count == 2:
                    score -= 10

            return score
