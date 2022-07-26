import pygame, sys, random

pygame.init()

screen = pygame.display.set_mode((800,600))
pygame.display.set_caption('Snake')
clock = pygame.time.Clock()

White = (255,255,255)
Green = (0,255,0)
Black = (0,0,0)
Red = (255,0,0)

pygame.draw.rect(screen, Black, [4, 5, 791, 590], 10)

gameQuit = False

block_size = 10

lead_x = 400
lead_y = 300

lead_x_change = 0
lead_y_change = 0

randAppleX = 300
randAppleY = 300

def randomApplePos():
    newX = round(random.randrange(11, 800 - block_size - 11))#/10.0)*10.0
    newY = round(random.randrange(11, 600 - block_size - 11))#/10.0)*10.0
    return newX, newY

while not gameQuit:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameQuit = True
        if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    lead_y_change = 0
                    lead_x_change = -block_size
                elif event.key == pygame.K_RIGHT:
                    lead_y_change = 0
                    lead_x_change = block_size
                elif event.key == pygame.K_UP:
                    lead_x_change = 0
                    lead_y_change = -block_size
                elif event.key == pygame.K_DOWN:
                    lead_x_change = 0
                    lead_y_change = block_size
                elif event.key == pygame.K_m:       ## TO DO: remove this and add collision 
                    randAppleX, randAppleY = randomApplePos()

        
    lead_x += lead_x_change
    lead_y += lead_y_change

    screen.fill(Black)
    pygame.draw.rect(screen, Green, [4, 5, 791, 590], 10)

    AppleThickness = 10
    pygame.draw.rect(screen, Red, [randAppleX, randAppleY, AppleThickness, AppleThickness])

    pygame.draw.rect(screen, Green, [lead_x, lead_y, 10, 10])    
    pygame.display.update()

    clock.tick(30)


pygame.quit()
quit()
