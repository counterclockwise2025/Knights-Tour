'''
Samip Vaidh
2/15/20
Knights Tour
'''

#define the main program and create a 2D array for the chest board
def main():
    chess_board = [['[ * ]' for y in range (8)] for x in range (8)]
    save_file = open("Tour.txt", 'w')
    xMove = input("What is your x move for the Knight: ")
    yMove = input("What is your y move for the Knight: ")

    not_done = True
    while not_done:
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
    def __init__(self, x, y, chess_board):
        self.x = x
        self.y = y
        self.chess_board = chess_board
        self.stack = []

        return

    def move(self, x, y, chess_board):
        #checks the board bounds and size to make sure knight will not be out of bound
        if(x >= 0 and y >= 0 and x < 8 and y < 8 and chess_board[x][y] == -1):
            return True
        
        if():

        return

    def backtrack(self):
        #in dev
        if():

        return

class Node:
    #in dev, define head node
    def __init__(self, data):
        self.data = data
        self.next_node = None

        return

class SingleLinkedList:
    #in dev
    def __init__(self, item):
        self.head = None
        self.tail = None
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