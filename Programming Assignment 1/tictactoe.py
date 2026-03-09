from __future__ import annotations

from dataclasses import dataclass
from typing import List, Optional, Tuple


Player = str  # 'X' or 'O'
Move = int    # 0..8 inclusive


WIN_LINES: Tuple[Tuple[int, int, int], ...] = (
    (0, 1, 2), (3, 4, 5), (6, 7, 8),  # rows
    (0, 3, 6), (1, 4, 7), (2, 5, 8),  # cols
    (0, 4, 8), (2, 4, 6),             # diagonals
)


@dataclass
class TicTacToe:
    """A simple 3x3 Tic‑Tac‑Toe game state.

    Board squares are indexed like:
        0 | 1 | 2
        --+---+--
        3 | 4 | 5
        --+---+--
        6 | 7 | 8
    """

    board: List[str]
    next_player: Player = "X"

    @staticmethod
    def new() -> "TicTacToe":
        return TicTacToe(board=[" "] * 9, next_player="X")

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

        rows = [
            f" {cell(0)} | {cell(1)} | {cell(2)} ",
            "---+---+---",
            f" {cell(3)} | {cell(4)} | {cell(5)} ",
            "---+---+---",
            f" {cell(6)} | {cell(7)} | {cell(8)} ",
        ]
        return "\n".join(rows)
