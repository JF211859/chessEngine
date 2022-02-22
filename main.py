import pygame
from board import *
tan = pygame.Color(210,180,140)
brown = pygame.Color(101,67,33)

def main():
    #initialize pygame
    pygame.init()
    
    #initializes display
    display = pygame.display.set_mode((400,400))

    #creates a surface that represents the board
    boardImage = makeBoard()

    #blits the board surface onto the display
    display.blit(boardImage,(0,0))

    #initializes the board class with the starting position
    board = Board()

    board.updateImage()

    #blits inital board onto surface
    display.blit(board.getImage(),(0,0))

    hoveringSquare = board.squares[0][0]

    #continuous loop
    while True:

        display.blit(boardImage,(0,0))

        #gets all events in pygame.event
        for event in pygame.event.get():

            #exits the game if the screen is closed
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()


            if event.type == pygame.MOUSEMOTION:
                mousePos = event.__dict__["pos"]
                col = int(mousePos[0] / 50)
                row = int(mousePos[1] / 50)
                if not hoveringSquare == board.squares[row][col]:
                    if hoveringSquare.state == "hovering":
                        hoveringSquare.state = "occupied"
                    hoveringSquare = board.squares[row][col]
                    if hoveringSquare.state == "occupied":
                        hoveringSquare.state = "hovering"
                    board.updateImage()
                    

        
        display.blit(board.getImage(),(0,0))

        #updates display
        #TODO doesn't need to update ever run
        pygame.display.update()
    

#creates a surface of the board
def makeBoard():
    boardImage = pygame.Surface((400,400))
    squareImageTan = pygame.Surface((50,50))
    squareImageTan.fill(tan)
    squareImageBrown = pygame.Surface((50,50))
    squareImageBrown.fill(brown)
    for row in range(8):
        for col in range(8):
            if (row+col)%2 == 0:
                boardImage.blit(squareImageTan, (col*50,row*50))
            else:
                boardImage.blit(squareImageBrown, (col*50,row*50))
    return boardImage


if __name__ == "__main__":
    main()