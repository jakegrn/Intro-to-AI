"""CE213 Lab Exercise 1 

Student task:
  Implement breadth-first search (BFS) in solve().
  The rest of the file is provided to help you run and test your code.
"""

from __future__ import annotations
from collections import deque
from typing import Deque, Optional, Set

import game_state as gs
from node import Node


def report_solution(goal_node: Node, out_file: str = "output.txt") -> None:
    """Write the solution path to a text file."""
    path = goal_node.path()
    with open(out_file, "w", encoding="utf-8") as f:
        f.write("Corn–Goose–Fox problem solved by breadth-first search (BFS)\n\n")
        for i, n in enumerate(path):
            if i == 0:
                f.write(f"Step {i}: START\n")
            else:
                f.write(f"Step {i}: {n.action}\n")
            f.write(gs.pretty_state(n.state) + "\n\n")
        f.write(f"Total moves: {len(path) - 1}\n")


# Answers to questions can be found in the README.txt


def solve() -> Optional[Node]:
    """Return the goal node if a solution is found, else None."""
    start_state = gs.initial_state()
    start = Node(state=start_state, parent=None, action=None, depth=0)

    # Unexpanded nodes queue (FIFO for BFS)
    frontier: Deque[Node] = deque([start])

    # Visited set (to avoid loops)
    visited: Set[gs.State] = {start_state} 

    # TODO: Implement BFS using the provided pseudocode in the lab sheet.
    # Hints:
    #   - Use frontier.popleft() to expand the next node (FIFO).
    #   - Use gs.successors(state) to generate (next_state, action_name).
    #   - Create child nodes with Node(state=..., parent=..., action=..., depth=...).
    #   - Use visited to prevent adding the same state more than once.

    while frontier:                     # While the frontier deque is not empty, run below
            n = frontier.popleft()      # BFS uses queue, so will be using FIFO
            if gs.is_goal(n.state):     # If goal state (1,1,1,1) matches, return goal state 
                return n                                    
            else:
                for nextState, actionName in gs.successors(n.state):    # gs.successors(n.state) returns max of 4 actions that could be taken by farmer from the current state
                    if nextState not in visited:                        # Visited set stops the BFS becoming an infinite traversal, so checks if child state is visited already
                        child = Node(state=nextState, parent=n, action=actionName, depth=n.depth+1)
                        frontier.append(child)                          # Appends child node to back of queue, whilst listing child's state as visited
                        visited.add(nextState)                         
    return None                                                         # Failure represented as None, to fit condition in main
                

    # raise NotImplementedError("Implement BFS in solve()")


def main() -> None:
    goal = solve()
    if goal is None:
        print("No solution found.")
    else:
        report_solution(goal)
        print("Solution written to output.txt")


if __name__ == "__main__":
    main()
