'''
Samip Vaidh
2/15/20
Knights Tour
'''

#define the main program and create a 2D array for the chest board
def main():
    chess_board = [['[ * ]' for y in range (8)] for x in range (8)]
    save_file = open("Tour.txt", 'w')
    print("Welcome to the Knights Tour, this program will show you the shortest path the Knight piece will take from your desired start position. \n")
    x_move = input("What is your X coordinate start position for the Knight: ")
    y_move = input("What is your Y coordinate start position for the Knight: ")
    #do not know if this line is even correct on storing the value in the LinkedList
    #SingleLinkedList(xMove, yMove)

    #While the program is not done it will still run through the program until there is a solution found
    not_done = True
    while not_done:
        Knight.valid_move()
        Knight.backtrack()
        print_board()

    save_file.close()

    return

#print board
def print_board(chess_board):
    for y in range (8):
        each_line = ''
        for x in range (8):
            each_line += '{} '.format(chess_board[x][y])

        print(each_line)

    return

def not_finished():
    #in dev

    return

#create a knight class with functions to help move the knight with implemented back tracking
class Knight:
    def __init__(self, x, y, chess_board, move_count):
        self.x = x
        self.y = y
        self.chess_board = chess_board
        self.move_count = move_count
        self.stack = []

        return

    def valid_move(self, x, y, chess_board):
        #checks the board bounds and size to make sure knight will not be out of bound
        if(x >= 0 and y >= 0 and x < 8 and y < 8 and chess_board[x][y] == 0):
            return True
        return False

    def backtrack(self, x, y, chess_board, move_count):
        #8 possible ways for the knight to move
        pos_x_move = [2, 1, -1, -2, -2, -1, 1, 2]
        pos_y_move = [1, 2, 2, 1, -1, -2, -2, -1]

        if(move_count == 32):
            return True

        for p in range (0, 8):
            next_x = x + pos_x_move[p]
            next_y = y + pos_y_move[p]

            if(valid_move(next_x, next_y, chess_board)):
                chess_board [next_x][next_y] = move_count
                if(backtrack(chess_board, next_x, next_y, move_count + 1, pos_x_move, pos_y_move)):
                    stack.append(move_count)
                    return True
                else #finish this statement and figure it out
                    stack.pop(move_count)


class Node:
    #in dev
    def __init__(self, data):
        self.data = data
        self.next_node = None

        return

class SingleLinkedList:
    #in dev
    def __init__(self, NULL, item):
        self.head = None
        self.tail = NULL
        self.item = item
        '''
        if not isinstance(item, Node):
            item = Node(item)
        '''
        if self.head is None:
            self.head = item
        else:
            self.tail.next = item

        self.tail = item

        return