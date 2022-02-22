<<<<<<< HEAD
from numpy import square
import pygame
from square import Square

class Board:


    def __init__(self, FEN = "rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR"):

        self.squares = [[Square(row,col) for col in range(8)] for row in range(8)]

        self.FENinput(FEN)




    #returns the surface of the board
    def getImage(self):
        boardSurface = pygame.Surface((400,400), pygame.SRCALPHA)
        for row in range(8):
            for col in range(8):
                if not self.squares[row][col].state == "unoccupied":
                    boardSurface.blit(self.squares[row][col].getImage(),(col*50,row*50))
        return boardSurface
                




    #handles the FEN string and gives fills in the squares array
    def FENinput(self, FEN):
        row = 0
        col = 7
        for c in FEN:
            if c.isdigit():
                col -= int(c)
            elif c == "/":
                row += 1
                col = 7
            elif c == "R":
                self.squares[row][col].set( "Rook", True)
                col -= 1
            elif c == "r":
                self.squares[row][col].set("Rook", False)
                col -= 1
            elif c == "K":
                self.squares[row][col].set("King", True)
                col -= 1
            elif c == "k":
                self.squares[row][col].set( "King", False)
                col -= 1
            elif c == "B":
                self.squares[row][col].set("Bishop", True)
                col -= 1
            elif c == "b":
                self.squares[row][col].set("Bishop", False)
                col -= 1
            elif c == "Q":
                self.squares[row][col].set("Queen", True)
                col -= 1
            elif c == "q":
                self.squares[row][col].set("Queen", False)
                col -= 1
            elif c == "P":
                self.squares[row][col].set("Pawn", True)
                col -= 1
            elif c == "p":
                self.squares[row][col].set("Pawn", False)
                col -= 1
            elif c == "N":
                self.squares[row][col].set("Knight", True)
                col -= 1
            elif c == "n":
                self.squares[row][col].set("Knight", False)
                col -= 1
=======
import pygame
from square import Square

class Board:


    def __init__(self, FEN = "rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR"):

        self.squares = [[Square(row,col) for col in range(8)] for row in range(8)]

        self.FENinput(FEN)




    #returns the surface of the board
    def getImage(self):
        self.boardSurface = pygame.Surface((400,400), pygame.SRCALPHA)
        for row in range(8):
            for col in range(8):
                if not self.squares[row][col].state == "unoccupied":
                   self.boardSurface.blit(self.squares[row][col].image,(col*50,row*50))
        return self.boardSurface

    def updateImage(self):
        self.boardSurface = pygame.Surface((400,400), pygame.SRCALPHA)
        showingMoveSquare = None
        for row in range(8):
            for col in range(8):
                if not self.squares[row][col].state == "unoccupied":
                    self.boardSurface.blit(self.squares[row][col].setImage(),(col*50,row*50))
                #if self.squares[row][col].state == "showingMoves"
        return self.boardSurface
                




    #handles the FEN string and gives fills in the squares array
    def FENinput(self, FEN):
        row = 0
        col = 7
        for c in FEN:
            if c.isdigit():
                col -= int(c)
            elif c == "/":
                row += 1
                col = 7
            elif c == "R":
                self.squares[row][col].set( "Rook", True)
                col -= 1
            elif c == "r":
                self.squares[row][col].set("Rook", False)
                col -= 1
            elif c == "K":
                self.squares[row][col].set("King", True)
                col -= 1
            elif c == "k":
                self.squares[row][col].set( "King", False)
                col -= 1
            elif c == "B":
                self.squares[row][col].set("Bishop", True)
                col -= 1
            elif c == "b":
                self.squares[row][col].set("Bishop", False)
                col -= 1
            elif c == "Q":
                self.squares[row][col].set("Queen", True)
                col -= 1
            elif c == "q":
                self.squares[row][col].set("Queen", False)
                col -= 1
            elif c == "P":
                self.squares[row][col].set("Pawn", True)
                col -= 1
            elif c == "p":
                self.squares[row][col].set("Pawn", False)
                col -= 1
            elif c == "N":
                self.squares[row][col].set("Knight", True)
                col -= 1
            elif c == "n":
                self.squares[row][col].set("Knight", False)
                col -= 1
>>>>>>> f4d0133b0b3da9ca5a5d803e74b997e5132daa48
