'''
Samip Vaidh
2/21/20
Knights Tour
'''

import random

#print board
def print_board(chess_board):
    for col in range (8):
        each_line = ''
        for row in range (8):
            each_line += '[ {} ] '.format(chess_board[col][row])

        print(each_line)

#knight class with functions to help move the knight with implemented back tracking
class Knight:
    def __init__(self, col, row, chess_board):
        self.x = col
        self.y = row
        self.chess_board = chess_board

        self.chess_board[self.x][self.y] = 'k'
        self.stack = []
        return

    #function condition that will tell the while loop if the condition is met
    def is_done(self):
        for row in range(8):
            for col in range(8):
                if self.chess_board[col][row] == '*': #if '*' is found then the loop will continue
                    return False
        return True

    #finds all the possible moves the knight can prouduce
    def find_moves(self, position = None):
        if position is None:
            col = self.x
            row = self.y
        else:
            col, row = position

        #stores all possible moves into a array
        moves = []
        #possible moves for the knight, hard coded into tuples
        possible_moves = [(2,1), (1,2), (-1, 2), (-2,1), (-2, -1), (-1, -2), (1, -2), (2, -1)]
        
        #loops through the list of possible moves array 
        for element in possible_moves: 
            x_move, y_move = element 
            #making sure that the knight piece does not go out of bounds
            if col + x_move < 8 and col + x_move > -1 and row + y_move < 8 and row + y_move > -1 and self.chess_board[col + x_move][row + y_move] == '*':
                moves.append((col + x_move, row + y_move)) #add this to the moves array since it can be done after this check
        return moves #returns the moves array at the end with all possible moves
    '''
    def degree(self, moves, col, row):
        deg_count = 0
        for square in range 8:

    def best_move(self, moves):
        for bm in moves:
            x_move, y_move = bm
            if bm 
    '''
    #uses the moves array to actually move the knight piece by random
    def make_move(self, moves):
        #looks at the array of possible moves and picks a random tuple as it's move
        move = random.choice(moves)
        col, row = (self.x, self.y)
        self.stack.append((col, row)) #append to the stack as visited
        self.chess_board [col][row] = 'v' #set the status of the sqaure to visited

        #make the knights position to set as 'k'
        col, row = move
        self.x = col
        self.y = row
        self.chess_board[col][row] = 'k'

    def backtrack(self):
        #setting tuple to be x, y
        position = (self.x, self.y)
        removed =[position] #store removed position including the current spot
        while len(self.find_moves(position)) == 0:
            position = self.stack.pop()
            removed.append(position)

        #position knight to the current sqaure it is on
        self.make_move(self.find_moves(position))

        #looks back into the removed array and checks the previous possible moves back to * since it cannot go back to those till it finds a valid move
        for element in removed:
            col, row = element
            self.chess_board[col][row] = '*' #set whatever was backtracked to unvisited

#create the node itself
class Node:
    def __init__(self, data = None):
        self.data = data
        self.next_node = None #setting the next node to null

#creating a single linked list
class SingleLinkedList:
    def __init__(self, head = None):
        self.head = head
        self.item = Node
    
    #returns the head
    def get_head(self):
        return self.head

    #breaks the link of the previous head and makes the next node the head
    def delete_head(self):
        if self.head is not None:
            self.head = self.head.next_node

    #adding a new head to the linked list
    def add(self, item):
        if self.head is not None:
            current = self.head
            while current.next_node is not None:
                current = current.next_node
            current.next_node = Node(item)
        else:
            self.head = Node(item)

#define the main program and create a 2D array for the chest board
if __name__ == '__main__':
    lst = SingleLinkedList()
    res = ''

    while res != 'EXIT':
        save_file = open("Tour.txt", 'w')
        intro = """
        Welcome to the Knights Tour, this program will give you a result of the Knights Tour from your desired input. Things to note are...

        * - unvisited square
        v - knight has visited
        k - current position of the knight
        """
        print(intro)
        x_move = int(input("What is your X coordinate start position for the Knight: "))
        y_move = int(input("What is your Y coordinate start position for the Knight: "))

        while x_move < 1 and x_move > 8 and y_move < 1 and y_move > 8:
            x_move = int(input("What is your X coordinate start position for the Knight: "))
            y_move = int(input("What is your Y coordinate start position for the Knight: "))

        lst.add((x_move - 1, y_move - 1))
        res = input("Type EXIT to see your result, or press ENTER to enter a new X and Y coordinate: ")

    while lst.head is not None:
        col, row = lst.get_head().data #tuple, unpacking values from initial position tuple 
        lst.delete_head()
        chess_board = [['*' for row in range (8)] for col in range (8)]
        k = Knight(col, row, chess_board) 
        #implement the Warndorff Huresitic here
        '''
        for in range 32:
            moves.k.find_moves
            for move in moves
        '''
        #will print each move till all of the board is set to 'v' for visited
        while not k.is_done():
            moves = k.find_moves() #list of moves
            if len(moves) > 0:
                k.make_move(moves) #picking moves and adding to the stack
            else:
                k.backtrack() #going back to find a possible move that is valid
        print("Back Tracking result... \n")
        print_board(chess_board) #print the board each time a move is made

    save_file.close()
        