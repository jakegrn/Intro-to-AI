Students must implement:

* ai\_alphabeta\_stub.py

Provided for help/reference:

* tictactoe.py (game logic)
* ai\_minimax.py (complete minimax reference)
* main.py (run the game)
* benchmark.py (performance comparison)

Do NOT modify other files unless instructed.

Benchmarking Minimax AI: 1.895930 seconds per move

Benchmarking Alpha-Beta AI: 0.074955 seconds per move

I had issues with this, since I was confused whether the benchmark functions were even working.
Turns out I had underestimated the time taken for the game to be computed 200 time (default selection)
so I had reduced it to simply 10 games. This would give good enough answers as is since it is pretty obvious
that alpha-beta pruning would greatly reduce time taken for minimax search to take place.

Calculating this, I observed that Alpha-Beta pruning sped up the Minimax search operation by over 25 times.