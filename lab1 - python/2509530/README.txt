CE213 Lab Exercise 1 — Python 
=========================================

Files
-----
- game_state.py : State-space representation + successor generation
- node.py       : Search node wrapper (state + parent pointers etc.)
- solver.py     : BFS solver (solve() is the main focus of the lab)
- output.txt    : Generated when you run solver.py (after BFS works)

How to run
----------
1) Open a terminal in this folder
2) Run:
       python3 solver.py
   (On Windows you may need: python solver.py)

What to submit
--------------
Zip all .py files (and any additional helper files you create), named with your registration number.

Notes
-----
- BFS (with a FIFO queue) guarantees an optimal solution in terms of number of moves when each move has equal cost.
- Use a visited set to avoid infinite loops / repeated states.


Questions

1) 4 Possible moves are implemented to the successors method. These are:

Farmer crosses alone
Farmer takes fox
Farmer takes goose
Farmer takes corn

2) 

A state is:
- A tuple (immutable)
- Filled with integer values
- Stores current state.

A node:
- An object
- Stores current state.
- Stores most recent action in order to reach state
- Stores parent node (which action led to the current, self state)
- Stores tree depth


solver.py does not produce output.txt at first. Instead returning NotImplementedError: Implement BFS in solve()

After implementing breadth-first search, output.txt generates the optimal minimum solution, which is only 7 steps.

If we were to implement iterative depth search instead of breadth first search, running time would slightly increase
however it would prove the correct solution with minimal memory usage.