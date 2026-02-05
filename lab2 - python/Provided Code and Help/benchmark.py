from __future__ import annotations

import time

from tictactoe import TicTacToe
from ai_minimax import MinimaxAI
from ai_alphabeta_stub import AlphaBetaAI


def time_ai(ai, n: int = 200) -> float:
    """Average time per move (seconds) from the initial position.

    For a fair comparison we time `choose_move()` repeatedly from the same state.
    """
    state = TicTacToe.new()
    start = time.perf_counter()
    for _ in range(n):
        _ = ai.choose_move(state)
    end = time.perf_counter()
    return (end - start) / n


def main() -> None:
    n = 400
    minimax = MinimaxAI(ai_player="X")
    alphabeta = AlphaBetaAI(ai_player="X")

    t1 = time_ai(minimax, n=n)
    t2 = time_ai(alphabeta, n=n)

    print(f"Average time per AI move over {n} runs:")
    print(f"  Minimax (no pruning): {t1:.6f} s")
    print(f"  Alpha-beta:           {t2:.6f} s")
    if t2 > 0:
        print(f"  Speedup:              {t1/t2:.2f}x")


if __name__ == "__main__":
    main()
