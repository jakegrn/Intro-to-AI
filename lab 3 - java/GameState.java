import java.util.ArrayList;

/*
      Instances of the class GameState represent states that can arise in the sliding block puzzle.
      The char array board represents the board configuration; that is, the location of each of the
      six tiles. Black tiles are represented by the char 'B', white tiles by the char 'W' and the
      empty location by the space character.
      The int spacePos holds the position of the empty location. (Although this is redundant it saves a
      lot of computation as it is frequently necessary to refer to this location).
      INITIAL_BOARD and GOAL_BOARD are constant arrays holding the initial and goal board configurations.
 */

public class GameState {
    final char[] board;
    private int spacePos;
    static final char[] INITIAL_BOARD = {'B','B','B',' ','W','W','W'};
    static final char[] GOAL_BOARD = {'W','W','W',' ','B','B','B'};

    /*
        GameState is a constructor that takes a char array holding a board configuration as argument.
     */
    public GameState(char[] board) {
        this.board = board;
        for (int j = 0; j < 7; j++){
            if (board[j] == ' ') {
                this.spacePos = j;
                break;
            }
        }
    }

    /*
        clone returns a new GameState with the same board configuration as the current GameState.
     */
    public GameState clone() {
        char[] clonedBoard = new char[7];
        System.arraycopy(this.board, 0, clonedBoard, 0, 7);
        return new GameState(clonedBoard);
    }

    public int getSpacePos() {
        return spacePos;
    }

    /*
        toString returns the board configuration of the current GameState as a printable string.
    */
    public String toString() {
        String s = "[";
        for (char c : this.board) s = s + c;
        return s + "]";
    }

    /*
        isGoal returns true if and only if the board configuration of the current GameState is the goal
        configuration.
    */
    public boolean isGoal() {
        for (int j = 0; j < 7; j++) {
            if (this.board[j] != GOAL_BOARD[j]) return false;
        }
        return true;
    }

    /*
         sameBoard returns true if and only if the GameState supplied as argument has the same board
         configuration as the current GameState.
     */
    public boolean sameBoard (GameState gs) {
        for (int j = 0; j < 7; j++) {
            if (this.board[j] != gs.board[j]) return false;
        }
        return true;
    }

    /*
        possibleMoves returns a list of all GameStates that can be reached in a single move from the current GameState.
     */
    public ArrayList<GameState> possibleMoves() {
        ArrayList<GameState> moves = new ArrayList<GameState>();
        for (int start = 0; start < 7; start++) {
            if (start != this.spacePos) {
                int distance = Math.abs(this.spacePos - start);
                if (distance <= 3) {
                    GameState newState = this.clone();
                    newState.board[this.spacePos] = this.board[start];
                    newState.board[start] = ' ';
                    newState.spacePos = start;
                    moves.add(newState);
                }
            }
        }
        return moves;
    }

}

