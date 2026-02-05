"""Search node definition (Python Starter Code).

A *state* is a compact description of the problem configuration (see game_state.py).
A *node* is a wrapper used by the search algorithm to track:
    - the current state,1
    - the parent node (for backtracking the solution),
    - the action taken to reach this node,
    - depth (path length so far).
"""

from __future__ import annotations
from dataclasses import dataclass
from typing import Optional, Tuple

from game_state import State

@dataclass # dataclass decorator to automatically generate init and repr methods, less boilerplate code
class Node:
    state: State
    parent: Optional["Node"] = None
    action: Optional[str] = None # action taken to reach this node
    depth: int = 0

    def path(self) -> list["Node"]:
        """Return nodes from root to this node."""
        out = []
        n: Optional[Node] = self # Start from the current node
        while n is not None:
            out.append(n)
            n = n.parent
        return list(reversed(out))
