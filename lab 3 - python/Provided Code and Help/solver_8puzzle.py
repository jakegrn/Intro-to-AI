from __future__ import annotations

import time
from dataclasses import dataclass
from heapq import heappop, heappush
from typing import Dict, List, Optional, Tuple

from eight_puzzle import PuzzleState, heuristic


@dataclass
class Node:
    state: PuzzleState
    parent: Optional["Node"]
    move: Optional[str]  # move taken to reach this node
    g: int               # path cost (depth)
    f: int               # priority for queue


def reconstruct_path(node: Node) -> List[Node]:
    path: List[Node] = []
    cur: Optional[Node] = node
    while cur is not None:
        path.append(cur)
        cur = cur.parent
    path.reverse()
    return path


def uniform_cost_search(start: PuzzleState, goal: PuzzleState) -> Tuple[Node, int, int]:
    counter = 0
    open_heap: List[Tuple[int, int, Node]] = []
    start_node = Node(start, None, None, g=0, f=0)
    heappush(open_heap, (start_node.f, counter, start_node))
    counter += 1

    best_g: Dict[PuzzleState, int] = {start: 0}
    expanded = 0

    while open_heap:
        _, _, node = heappop(open_heap)
        expanded += 1

        if node.state.is_goal(goal):
            return node, expanded, len(open_heap)

        for mv in node.state.legal_moves():
            nxt = node.state.apply(mv)
            ng = node.g + 1
            if nxt not in best_g or ng < best_g[nxt]:
                best_g[nxt] = ng
                nn = Node(nxt, node, mv, g=ng, f=ng)  # UCS priority = g
                heappush(open_heap, (nn.f, counter, nn))
                counter += 1

    raise RuntimeError("No solution found.")


def astar_search(start: PuzzleState, goal: PuzzleState) -> Tuple[Node, int, int]:
    counter = 0
    open_heap: List[Tuple[int, int, Node]] = []

    h0 = heuristic(start, goal)
    start_node = Node(start, None, None, g=0, f=h0)
    heappush(open_heap, (start_node.f, counter, start_node))
    counter += 1

    best_g: Dict[PuzzleState, int] = {start: 0}
    expanded = 0

    while open_heap:
        _, _, node = heappop(open_heap)
        expanded += 1

        if node.state.is_goal(goal):
            return node, expanded, len(open_heap)

        for mv in node.state.legal_moves():
            nxt = node.state.apply(mv)
            ng = node.g + 1
            if nxt not in best_g or ng < best_g[nxt]:
                best_g[nxt] = ng
                h = heuristic(nxt, goal)
                nn = Node(nxt, node, mv, g=ng, f=ng + h)
                heappush(open_heap, (nn.f, counter, nn))
                counter += 1

    raise RuntimeError("No solution found.")


def write_output(path_nodes: List[Node], expanded: int, unexpanded: int, outfile: str) -> None:
    with open(outfile, "w", encoding="utf-8") as f:
        for n in path_nodes:
            f.write(n.state.one_line() + "\n")
        f.write(f"\n###### Nodes expanded\n{expanded}\n")
        f.write(f"## Nodes unexpanded\n{unexpanded}\n")


def main() -> None:
    # Initial and goal configurations from the lab sheet figure:
    start = PuzzleState((8, 7, 6, 5, 4, 3, 2, 1, 0))
    goal = PuzzleState((1, 2, 3, 4, 5, 6, 7, 8, 0))

    print("Choose search strategy:")
    print("1) Uniform Cost Search (UCS)")
    print("2) A* Search")
    choice = input("Enter 1 or 2: ").strip()

    t0 = time.time()
    if choice == "1":
        node, expanded, unexpanded = uniform_cost_search(start, goal)
        outfile = "outputUniCost.txt"
    elif choice == "2":
        node, expanded, unexpanded = astar_search(start, goal)
        outfile = "outputAstar.txt"
    else:
        print("Invalid choice.")
        return
    t1 = time.time()

    path_nodes = reconstruct_path(node)
    write_output(path_nodes, expanded, unexpanded, outfile)

    print(f"Solution written to: {outfile}")
    print(f"Moves: {len(path_nodes) - 1}")
    print(f"Time: {t1 - t0:.4f} seconds")


if __name__ == "__main__":
    main()
