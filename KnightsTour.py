'''
Samip Vaidh
2/15/20
Knights Tour
'''

#define the main program and create a 2D array for the chest board
def main():
    chess_board = [['[ * ]' for y in range (8)] for x in range (8)]
    xMove = input("What is your x move for the Knight: ")
    yMove = input("What is your y Move for the Knight: ")

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

class Node():
    #in dev, define head node
    def __init__(self):

class LinkedList:
    #in dev
    def __init__(self):
