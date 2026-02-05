from __future__ import annotations

from typing import Optional

from tictactoe import TicTacToe
from ai_minimax import MinimaxAI
from ai_alphabeta_stub import AlphaBetaAI
import benchmark as bm

# For the lab, you will switch to:
# from ai_alphabeta_stub import AlphaBetaAI


def prompt_move(state: TicTacToe) -> int:
    while True:
        raw = input("Enter your move (0-8): ").strip()
        if not raw.isdigit():
            print("Please enter a number from 0 to 8.")
            continue
        move = int(raw)
        if move not in range(9):
            print("Move must be between 0 and 8.")
            continue
        if move not in state.legal_moves():
            print("That square is not available. Try again.")
            continue
        return move


def main() -> None:
    state = TicTacToe.new()

    # AI plays X, human plays O
    # ai = MinimaxAI(ai_player="X")
    ab = AlphaBetaAI(ai_player="X")
    human = "O"

    print("Tic-Tac-Toe: You are O, AI is X.")
    print("Board squares are numbered 0..8 as shown when empty.")
    print()

    while not state.is_terminal():
        print(state.render())
        print()

        if state.next_player == human:
            mv = prompt_move(state)
            state = state.apply(mv)
        else:
            mv = ab.choose_move(state)
            print(f"AI plays: {mv}")
            state = state.apply(mv)
            

        

    print(state.render())
    w = state.winner()
    if w is None:
        print("\nResult: Draw.")
    else:
        print(f"\nResult: {w} wins.")


if __name__ == "__main__":
    main()
