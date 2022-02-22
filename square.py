import pygame

class Square:

    #states: unoccupied(0) -> occupied(1) -> hovering(2) -> showingMoves(3)
    #                                     -> underAttack(4)

    # 

    def __init__(self, row_in, col_in):
        self.images = [pygame.Surface((50,50), pygame.SRCALPHA) for i in range(5)]
        self.images[2].fill((0,255,0))
        self.images[3].fill((0,255,0))
        self.images[4].fill((255,0,0))
        self.state = "unoccupied"
        self.row = row_in
        self.col = col_in


    def set(self, piece_in = None, isLight_in = None):
        self.piece = piece_in
        self.isLight = isLight_in
        self.availableSquares = []
        self.attackingPieces = []
        if self.piece:
            self.state = "occupied"
            if self.isLight:
                picture = pygame.image.load(f"pieces/Light{self.piece}.png")
            else:
                picture = pygame.image.load(f"pieces/Dark{self.piece}.png")
            piecePicture = pygame.transform.scale(picture, (50,50)) 
            for i in range(1,5):
                self.images[i].blit(piecePicture,(0,0))


    
    def getImage(self):
        if self.state == "unoccupied":
            return None
        elif self.state == "occupied":
            return self.images[1]
        elif self.state == "hovering":
            return self.images[2]
        elif self.state == "showingMoves":
            return self.images[3] 
        elif self.state == "underAttack":
            return self.images[4] 