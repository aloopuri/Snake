import pygame, sys

pygame.init()

screen = pygame.display.set_mode((800,600))
pygame.display.set_caption('Snake')
clock = pygame.time.Clock()

White = (255,255,255)
Green = (0,255,0)
Black = (0,0,0)
#screen.fill(White)

pygame.draw.rect(screen, Black, [4, 5, 791, 590], 10)

gameQuit = False

while not gameQuit:
    ## asdf
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameQuit = True
        
    
    pygame.draw.rect(screen, Green, [4, 5, 791, 590], 10)
    pygame.draw.rect(screen, Green, [300, 300, 10, 10])    
    pygame.display.update()

pygame.quit()
quit()
