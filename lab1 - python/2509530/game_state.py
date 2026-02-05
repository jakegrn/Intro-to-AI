"""CE213 Lab Exercise 1 (Python Starter Code)

State-space representation for the classic 'farmer, fox, goose, corn' river crossing puzzle.

Representation:
    Each entity is on either the LEFT bank (0) or RIGHT bank (1).
    A state is a 4-tuple of ints: (FARMER, FOX, GOOSE, CORN)

Rules (unsafe states):
    - If the farmer is NOT with the goose, the fox cannot be left alone with the goose.
    - If the farmer is NOT with the goose, the goose cannot be left alone with the corn.

    f AND g AND `m = FALSE
    c AND g AND `m = FALSE

    solution

    1) m AND g -> 1
    2) m -> 0
    2) m AND f -> 1
    3) m AND g -> 0
    4) m AND c -> 1
    5) m -> 0
    6) m AND g -> 1

TODO (student task in the lab):
    - Add explanatory comments where appropriate.
    - Review initial/goal states, operators, and transition function.
"""

from __future__ import annotations
from dataclasses import dataclass
from typing import Iterable, List, Optional, Tuple

LEFT = 0
RIGHT = 1

State = Tuple[int, int, int, int]  # (farmer, fox, goose, corn)

@dataclass(frozen=True)
class Move:
    """A move is defined by who crosses with the farmer."""
    name: str
    passenger: Optional[str]  # None means farmer crosses alone


MOVES: List[Move] = [
    Move("Farmer crosses alone", None),
    Move("Farmer takes fox", "fox"),
    Move("Farmer takes goose", "goose"),
    Move("Farmer takes corn", "corn"),
]


def initial_state() -> State:
    # All start on the LEFT bank
    return (LEFT, LEFT, LEFT, LEFT)


def goal_state() -> State:
    # All end on the RIGHT bank
    return (RIGHT, RIGHT, RIGHT, RIGHT)


def is_goal(s: State) -> bool:
    return s == goal_state()


def is_safe(s: State) -> bool: # Check at the end of every moving iteration

    """Return True if state is safe (no one gets eaten)."""
    farmer, fox, goose, corn = s

    # If farmer is away from goose, goose must not be alone with fox or corn.
    if farmer != goose:
        if fox == goose:
            return False  # fox eats goose
        if corn == goose:
            return False  # goose eats corn
    return True


def apply_move(s: State, move: Move) -> Optional[State]:
    """Apply a move; return the new state if legal & safe, else None."""
    farmer, fox, goose, corn = s

    # Determine the side farmer will move to
    new_side = RIGHT if farmer == LEFT else LEFT

    # Passenger must be on the same side as the farmer to travel
    if move.passenger is None:
        nf, nfox, ngoose, ncorn = new_side, fox, goose, corn
    elif move.passenger == "fox":
        if fox != farmer: # Check if fox is on the same side as farmer
            return None
        nf, nfox, ngoose, ncorn = new_side, new_side, goose, corn
    elif move.passenger == "goose":
        if goose != farmer:
            return None
        nf, nfox, ngoose, ncorn = new_side, fox, new_side, corn
    elif move.passenger == "corn":
        if corn != farmer:
            return None
        nf, nfox, ngoose, ncorn = new_side, fox, goose, new_side
    else:
        return None

    ns: State = (nf, nfox, ngoose, ncorn)
    return ns if is_safe(ns) else None      # return new state only if it's safe


def successors(s: State) -> Iterable[Tuple[State, str]]: # Generate all possible next states from the current state
    """Generate (next_state, action_name) pairs from the given state."""
    for m in MOVES:
        ns = apply_move(s, m)
        if ns is not None:
            yield ns, m.name # Yield only safe and legal states


def pretty_state(s: State) -> str:
    """Human-readable formatting for output.txt."""
    farmer, fox, goose, corn = s
    names = ["Farmer", "Fox", "Goose", "Corn"]
    sides = [farmer, fox, goose, corn]

    left = [names[i] for i,side in enumerate(sides) if side == LEFT] # List of entities on the LEFT bank
    right = [names[i] for i,side in enumerate(sides) if side == RIGHT] # List of entities on the RIGHT bank
    return f"LEFT: {', '.join(left):<25} | RIGHT: {', '.join(right)}" # Format the output nicely
