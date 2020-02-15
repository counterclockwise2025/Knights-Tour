/*
Samip Vaidh
Last Edit: 2/15/20
*/

import java.io.*;
import java.util.*;

public class Tour
{
    public static void main(String[] args) 
    {
        //taking user input for the start of the knights location
        Scanner input = new Scanner(System.in);
        System.out.printLine("Welcome to the the Knight's Tour \n");
        System.out.printLine("Please set the size of your chess board: \n");
        int boardSize = input.next();
        System.out.printLine("Where do you want your Knight to start on the x coordinate: ");
        int xStart = input.next();
        System.out.printLine("What about the y coordinate");
        int yStart = input.next();
    }
}

