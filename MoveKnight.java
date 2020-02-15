import java.io.*;

public class MoveKnight 
{
    //create a constructor for the move the knight piece
    public Move (int xMove, int yMove, int boardSize, int board [][])
    {
        this.xMove = xMove;
        this.yMove = yMove;
        this.boardSize = boardSize;
        this.board = board;
    }
    //getters to access the constructor attributes
    public int getX()
    {
        return xMove; 
    }

    public int getY()
    {
        return yMove;
    }

    public int getBoardSize()
    {
        return boardSize;
    }

    public int getBoard()
    {
        return board;
    }
}
