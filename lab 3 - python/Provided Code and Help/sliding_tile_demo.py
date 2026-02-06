from __future__ import annotations

from dataclasses import dataclass
from heapq import heappop, heappush
from typing import Dict, List, Optional, Tuple


# Reference example: a small sliding-tile puzzle solved with best-first search.
# Use it to understand:
# - how states can be represented
# - how legal moves are generated
# - how a solution path can be reconstructed


@dataclass(frozen=True)
class GameState:
    board: Tuple[str, ...]  # 'B', 'W', '_' for empty

    @staticmethod
    def initial() -> "GameState":
        return GameState(tuple("BBB_WWW"))

    @staticmethod
    def goal() -> "GameState":
        return GameState(tuple("WWW_BBB"))

    def empty_index(self) -> int:
        return self.board.index("_")

    def legal_moves(self) -> List[int]:
        e = self.empty_index()
        movers: List[int] = []
        for jump in (1, 2, 3):
            for sgn in (-1, 1):
                i = e + sgn * jump
                if 0 <= i < len(self.board) and self.board[i] != "_":
                    movers.append(i)
        return movers

    def apply_move(self, tile_index: int) -> "GameState":
        b = list(self.board)
        e = self.empty_index()
        b[e], b[tile_index] = b[tile_index], b[e]
        return GameState(tuple(b))

    def h_misplaced(self) -> int:
        # goal is WWW_BBB -> first 3 are W, last 3 are B
        score = 0
        for i, t in enumerate(self.board):
            if t == "_":
                continue
            if i < 3 and t != "W":
                score += 1
            if i > 3 and t != "B":
                score += 1
        return score

    def __str__(self) -> str:
        return " ".join(self.board)


@dataclass
class Node:
    state: GameState
    parent: Optional["Node"]
    g: int
    f: int


def reconstruct_path(node: Node) -> List[GameState]:
    path: List[GameState] = []
    cur: Optional[Node] = node
    while cur is not None:
        path.append(cur.state)
        cur = cur.parent
    path.reverse()
    return path


def solve() -> Node:
    start = GameState.initial()
    goal = GameState.goal()

    open_heap: List[Tuple[int, int, Node]] = []
    counter = 0

    start_node = Node(start, None, g=0, f=start.h_misplaced())
    heappush(open_heap, (start_node.f, counter, start_node))
    counter += 1

    best_g: Dict[GameState, int] = {start: 0}

    while open_heap:
        _, _, node = heappop(open_heap)
        if node.state == goal:
            return node

        for tile_i in node.state.legal_moves():
            nxt = node.state.apply_move(tile_i)
            ng = node.g + 1
            if nxt not in best_g or ng < best_g[nxt]:
                best_g[nxt] = ng
                nn = Node(nxt, node, g=ng, f=ng + nxt.h_misplaced())
                heappush(open_heap, (nn.f, counter, nn))
                counter += 1

    raise RuntimeError("No solution found.")


def main() -> None:
    goal_node = solve()
    path = reconstruct_path(goal_node)
    for s in path:
        print(s)
    print(f"Moves: {len(path) - 1}")


if __name__ == "__main__":
    main()
