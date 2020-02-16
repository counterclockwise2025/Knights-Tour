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



#print board
def print_board(chess_board):
    for y in range (8):
        each_line = ''
        for x in range (8):
            each_line += '{} '.format(chess_board[x][y])

        print(each_line)

#create a knight class
class Knight:
    def __init__(self, x, y, chess_board):
        self.x = x
        self.y = y
        self.chess_board = chess_board
        self.stack = []

    def move(self):
        #in dev

    def choose_move(self):
        #in dev

    def backtrack(self):
        #in dev

def not_finished():
    #in dev

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