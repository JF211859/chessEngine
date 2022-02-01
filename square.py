import pygame

class Square:

    #states: unoccupied(0) -> occupied(1) -> hovering(2) -> showingMoves(3)
    #                                     -> underAttack(4)

    # 

    def __init__(self, row_in, col_in):
        self.state = "unoccupied"
        self.row = row_in
        self.col = col_in
        self.image = pygame.Surface((50,50), pygame.SRCALPHA)



    def set(self, piece_in = None, isLight_in = None):
        self.piece = piece_in
        self.isLight = isLight_in
        self.availableSquares = []
        self.attackingPieces = []
        if self.piece:
            self.state = "occupied"
        
    def setImage(self):
        self.image = pygame.Surface((50,50), pygame.SRCALPHA)
        if not self.state == "unoccupied":
            if self.state == "hovering":
                self.image.fill("green")
            if self.state == "underAttack":
                self.image.fill("red")
            unsizedPiecePicture = pygame.Surface((50,50), pygame.SRCALPHA)
            if self.isLight:
                unsizedPiecePicture = pygame.image.load(f"pieces/Light{self.piece}.png")
            else:
                unsizedPiecePicture = pygame.image.load(f"pieces/Dark{self.piece}.png")
            piecePicture = pygame.transform.scale(unsizedPiecePicture, (50,50))
            self.image.blit(piecePicture,(0,0))
        return self.image


    def updateAvailableMoves(self, pieces):
        if self.piece == "Pawn":
            self.updateAvailablePawnMoves(pieces)
        if self.piece == "Rook":
            self.updateAvailableRookMoves(pieces)
        if self.piece == "Bishop":
            self.updateAvailableBishopMoves(pieces)
        if self.piece == "Knight":
            self.updateAvailableKnightMoves(pieces)
        if self.piece == "Queen":
            self.updateAvailableQueenMoves(pieces)
        if self.piece == "King":
            self.updateAvailableKingMoves(pieces)
    

    def updateAvailablePawnMoves(self, pieces):
        self.attackingPieces = []
        self.availableSquares = []

        #seperates whether it is a light pawn or a dark pawn, direction gets added to the row.
        if self.isLight:
            direction = -1
        else:
            direction = 1

        #gets the basic moves up 1 square
        if pieces[self.row + direction][self.col].state == "unoccupied":
            self.availableSquares.append((self.row + direction, self.col))

        #allows the movement of 2 squares if it is on the 6th rank
        if self.row == 6:
            if pieces[self.row + 2*direction][self.col].state == "unoccupied":
                self.availableSquares.append((self.row - 2, self.col))

        #looks up and left to see if it can take
        if not pieces[self.row + direction][self.col - 1].state == "unoccupied":
            if not pieces[self.row + direction][self.col - 1].isLight:
                self.attackingPieces.append(pieces[self.row + direction][self.col - 1])
        
        #looks up and right to see if it can take
        if not pieces[self.row + direction][self.col + 1].state == "unoccupied":
            if not pieces[self.row + direction][self.col + 1].isLight:
                self.attackingPieces.append(pieces[self.row + direction][self.col + 1])
                

    def updateAvailableRookMoves(self, pieces):
        return None

    def updateAvailableBishopMoves(self, pieces):
        return None

    def updateAvailableKnightMoves(self, pieces):
        return None

    def updateAvailableQueenMoves(self, pieces):
        return None

    def updateAvailableKingMoves(self, pieces):
        return None