from __future__ import annotations

from dataclasses import dataclass
from typing import List, Tuple

Grid = Tuple[int, ...]  # length 9; 0 represents the blank


@dataclass(frozen=True)
class PuzzleState:
    """Immutable 8-puzzle state.

    Representation:
      - A 1D tuple of length 9 (row-major).
      - 0 represents the blank.
    """
    grid: Grid

    def blank_index(self) -> int:
        return self.grid.index(0)

    def legal_moves(self) -> List[str]:
        """Return legal blank moves: 'U','D','L','R'.

        TODO (student):
          - Use the blank location to determine which moves are valid.
          - Return a list containing any of: 'U','D','L','R'.
        """

        blank_index = self.blank_index()
        legal_moves = []

        if blank_index in [0, 1, 2]:  # blank in the top row
            legal_moves.append('U')
        if blank_index in [6, 7, 8]:  # blank in bottom row
            legal_moves.append('D')
        if blank_index in [0, 3, 6]:  # blank in left column
            legal_moves.append('L')
        if blank_index in [2, 5, 8]:  # blank in right column
            legal_moves.append('R')

        return legal_moves
    
    def apply(self, move: str) -> "PuzzleState":
        """Return a new state produced by applying one move.

        TODO (student):
          - Swap the blank with the neighbour indicated by the move.
          - Return the resulting PuzzleState.
        """

        if move not in self.legal_moves():
            raise ValueError(f"Illegal move: {move}")
        
        switch = {
            'U': -3,
            'D': 3,
            'L': -1,
            'R': 1
        }

        # ^ dictionary to determine the index change based on the move taken

        blank = self.blank_index()
        new_grid = list(self.grid) # cant update tuple - create new list
        new_blank= blank + switch[move]

        new_grid[blank] = new_grid[new_blank]
        new_grid[new_blank] = 0
        
        return PuzzleState(tuple(new_grid))

    def is_goal(self, goal: "PuzzleState") -> bool:
        return self.grid == goal.grid

    def one_line(self) -> str:
        parts = [(" " if v == 0 else str(v)) for v in self.grid] # ["8","7","6","5","4","3","2","1"," "]
        return " ".join(parts) # string representation of grid -> 8 7 6 5 4 3 2 1

    def pretty_lines(self) -> List[str]:
        out = []
        for r in range(3):
            row = []
            for c in range(3):
                v = self.grid[r * 3 + c]
                row.append(" " if v == 0 else str(v))
            out.append(" ".join(row))
        return out


def heuristic(state: PuzzleState, goal: PuzzleState) -> int:
    """Heuristic for A* search.

    TODO (student):
      - Implement a heuristic such as Manhattan distance.
      - Return an integer estimate of distance-to-goal.
    """

    for initial_index, number in enumerate(state):
        goal_index = goal.index(number)


        # https://www.almabetter.com/bytes/tutorials/artificial-intelligence/8-puzzle-problem-in-ai

    


    raise NotImplementedError

'''

top: [0,1,2]
middle: [3,4,5]
bottom: [6,7,8]

if (oldI MOD 3):

is 1 then 

'''