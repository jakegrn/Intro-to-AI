from __future__ import annotations

from dataclasses import dataclass
from typing import List, Optional, Tuple


Player = str  # 'X' or 'O'
Move = int    # 0..8 inclusive


WIN_LINES: Tuple[Tuple[int, int, int], ...] = (
    (0, 1, 2), (5, 6, 7), (10, 11, 12), (15, 16, 17), (20, 21, 22), (1, 2, 3), (6, 7, 8), (11, 12, 13), (16, 17, 18), (21, 22, 23), (2, 3, 4), (7, 8, 9), (12, 13, 14), (17, 18, 19), (22, 23, 24),  # rows
    (0, 5, 10), (1, 6, 11), (2, 7, 12), (3, 8, 13), (4, 9, 14), (5, 10, 15), (6, 11, 16), (7, 12, 17), (8, 13, 18), (9, 14, 19), (10, 15, 20), (11, 16, 21), (12, 17, 22), (13, 18, 23), (14, 19, 24),  # cols
    (2, 8, 14), (1, 7, 13), (7, 13, 19), (0, 6, 12), (6, 12, 18), (12, 18, 24), (5, 11, 17), (11, 17, 23), (10, 16, 22),
    (2, 6, 10), (3, 7, 11), (7, 11, 15), (4, 8, 12), (8, 12, 16), (12, 16, 20), (9, 13, 17), (13, 17, 21), (14, 18, 22)    # diagonals
)


@dataclass
class TicTacToe:
    """A simple 3x3 Tic‑Tac‑Toe game state.

    Board squares are indexed like:
         0 |  1 |  2 |  3 |  4
        ---+----+----+----+---
         5 |  6 |  7 |  8 |  9
        ---+----+----+----+---
        10 | 11 | 12 | 13 | 14
        ---+----+----+----+---
        15 | 16 | 17 | 18 | 19
        ---+----+----+----+---
        20 | 21 | 22 | 23 | 24
    """

    board: List[str]
    next_player: Player = "X"

    @staticmethod
    def new() -> "TicTacToe":
        return TicTacToe(board=[" "] * 25, next_player="X")

    def legal_moves(self) -> List[Move]:
        return [i for i, v in enumerate(self.board) if v == " "]

    def apply(self, move: Move) -> "TicTacToe":
        if self.board[move] != " ":
            raise ValueError(f"Illegal move: square {move} is not empty.")
        b = self.board.copy()
        b[move] = self.next_player
        return TicTacToe(board=b, next_player=("O" if self.next_player == "X" else "X"))

    def winner(self) -> Optional[Player]:
        for a, b, c in WIN_LINES:
            if self.board[a] != " " and self.board[a] == self.board[b] == self.board[c]:
                return self.board[a]
        return None

    def is_terminal(self) -> bool:
        return self.winner() is not None or " " not in self.board

    def outcome_value(self) -> int:
        """Return +1 for X win, -1 for O win, 0 for draw/non-terminal."""
        w = self.winner()
        if w == "X":
            return 1
        if w == "O":
            return -1
        # If no winner, it's either draw (full board) or still in progress.
        return 0

    def render(self) -> str:
        def cell(i: int) -> str:
            return self.board[i] if self.board[i] != " " else str(i)

        # AI-Generated code for rendering the board. No need to understand this for the assignment.

        rows = []
        for r in range(0, 25, 5):
            row = "|".join(f"{cell(i):^3}" for i in range(r, r + 5))
            rows.append(row)
            if r < 20:
                rows.append("---+---+---+---+---")
        return "\n".join(rows)

