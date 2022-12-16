import pygame, sys, random

class Snake:

    pygame.init()
    White = (255,255,255)
    Green = (0,255,0)
    Black = (0,0,0)
    Red = (255,0,0)

    display_width = 800
    display_height = 600
    screen = pygame.display.set_mode((display_width,display_height))
    pygame.display.set_caption('Snake')
    clock = pygame.time.Clock()            
    
    pygame.draw.rect(screen, Black, [4, 5, 791, 590], 10)

    def __init__(self):
        self.lead_x = 400
        self.lead_y = 300
        self.lead_x_change = 0
        self.lead_y_change = 0
        self.randAppleX = 300
        self.randAppleY = 300    
        self.block_size = 10    
        self.snakeList = []
        self.snakeLength = 1

    def snake(self, block_size, snakeList):
        for XnY in snakeList:
            pygame.draw.rect(self.screen, self.Green, [XnY[0], XnY[1], block_size, block_size])  

    #generate new position for the apple
    def randomApplePos(self):
        newX = round((random.randrange(11, self.display_width - self.block_size - 11)) / 10)*10
        newY = round((random.randrange(11, self.display_height - self.block_size - 11)) / 10)*10
        return newX, newY

    def gameLoop(self):
        gameQuit = False

        block_size = self.block_size

        while not gameQuit:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    gameQuit = True
                if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_LEFT:
                            self.lead_y_change = 0
                            self.lead_x_change = -block_size
                        elif event.key == pygame.K_RIGHT:
                            self.lead_y_change = 0
                            self.lead_x_change = block_size
                        elif event.key == pygame.K_UP:
                            self.lead_x_change = 0
                            self.lead_y_change = -block_size
                        elif event.key == pygame.K_DOWN:
                            self.lead_x_change = 0
                            self.lead_y_change = block_size
                        elif event.key == pygame.K_m:       ## TO DO: remove this and add collision 
                            self.randAppleX, self.randAppleY = self.randomApplePos()

                
            self.lead_x += self.lead_x_change
            self.lead_y += self.lead_y_change

            self.screen.fill(self.Black)
            pygame.draw.rect(self.screen, self.Green, [4, 5, 791, 590], 10)

            AppleThickness = 10
            pygame.draw.rect(self.screen, self.Red, [self.randAppleX, self.randAppleY, AppleThickness, AppleThickness])

            pygame.draw.rect(self.screen, self.Green, [self.lead_x, self.lead_y, block_size, block_size])    

            snakeHead = []
            snakeHead.append(self.lead_x)
            snakeHead.append(self.lead_y)
            self.snakeList.append(snakeHead)

            if len(self.snakeList) > self.snakeLength:
                del self.snakeList[0]

            self.snake(block_size, self.snakeList)    
            pygame.display.update()

            if self.lead_x == self.randAppleX and self.lead_y == self.randAppleY:
                self.randAppleX, self.randAppleY = self.randomApplePos()
                self.snakeLength +=1

            self.clock.tick(20)

        
        pygame.quit()
        quit()


if __name__== "__main__" :
    Snake().gameLoop()
    

