import pygame

display = pygame.display.set_mode((500,500))

image = pygame.Surface((50,50), pygame.SRCALPHA)

image.fill('blue')

display.fill('grey')

display.blit(image, (100,100))



while True:

            #gets all events in pygame.event
    for event in pygame.event.get():

        #exits the game if the screen is closed
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

        if event.type == pygame.MOUSEBUTTONDOWN:
            image = pygame.Surface((50,50), pygame.SRCALPHA)
            display.blit(image, (100,100))
    pygame.display.update()