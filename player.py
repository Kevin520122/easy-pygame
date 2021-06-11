#Load pictures
import pygame
import os

#Load player pictures
walkRight = [
        pygame.image.load(os.path.join('Game_Characters', 'R1.png')), 
        pygame.image.load(os.path.join('Game_Characters', 'R2.png')), 
        pygame.image.load(os.path.join('Game_Characters', 'R3.png')), 
        pygame.image.load(os.path.join('Game_Characters', 'R4.png')), 
        pygame.image.load(os.path.join('Game_Characters', 'R5.png')), 
        pygame.image.load(os.path.join('Game_Characters', 'R6.png')), 
        pygame.image.load(os.path.join('Game_Characters', 'R7.png')), 
        pygame.image.load(os.path.join('Game_Characters', 'R8.png')), 
        pygame.image.load(os.path.join('Game_Characters', 'R9.png'))
    ]
walkLeft = [
        pygame.image.load(os.path.join('Game_Characters', 'L1.png')), 
        pygame.image.load(os.path.join('Game_Characters', 'L2.png')), 
        pygame.image.load(os.path.join('Game_Characters', 'L3.png')), 
        pygame.image.load(os.path.join('Game_Characters', 'L4.png')), 
        pygame.image.load(os.path.join('Game_Characters', 'L5.png')), 
        pygame.image.load(os.path.join('Game_Characters', 'L6.png')), 
        pygame.image.load(os.path.join('Game_Characters', 'L7.png')), 
        pygame.image.load(os.path.join('Game_Characters', 'L8.png')), 
        pygame.image.load(os.path.join('Game_Characters', 'L9.png'))
    ]

class player(object):
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y 
        self.width = width
        self.height = height
        self.velocity = 5
        self.jumpCount = 10
        self.walkCount = 0
        self.isLeft = False
        self.isRight = False
        self.isJump = False
        self.standing = True
        self.hitbox = (self.x + 17, self.y+11, 29, 52)

    def draw(self, game_win):
        #To load picture, since there are 9 pictures(max index 8)
        #No more than 27(1 pic => 3 steps)
        if self.walkCount + 1 >= 27:
            self.walkCount = 0


        #If moving
        if not (self.standing):
            if self.isLeft:
                game_win.blit(walkLeft[self.walkCount // 3], (self.x, self.y))
                self.walkCount += 1

            elif self.isRight:
                game_win.blit(walkRight[self.walkCount // 3], (self.x, self.y))
                self.walkCount += 1
        #The case shooting
        else:
            if self.isRight:
                #Looking to the right
                game_win.blit(walkRight[0], (self.x, self.y))
            else:
                #Looking to the left
                game_win.blit(walkLeft[0], (self.x, self.y))
        self.hitbox = (self.x + 17, self.y + 11, 29, 52)
        #pygame.draw.rect(game_win, (255, 0, 0), self.hitbox, 2)
    def hit(self, game_win):
        #Reset jump section to avoid run the jump code when hitting
        self.isJump = False
        self.jumpCount =10
        #Reset player position
        self.x = 60
        self.y = 410
        self.walkCount = 0
        #Show the minus score
        font1 = pygame.font.SysFont("comicsans", 100)
        text = font1.render('-5', 1, (255, 0, 0))
        game_win.blit(text, (250 - (text.get_width() / 2), 200))
        pygame.display.update()
        i = 0
        while i < 300:
            pygame.time.delay(10)
            i += 1
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    i = 301
                    pygame.quit()