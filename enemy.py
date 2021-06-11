import pygame
import os
enemyRight = [
        pygame.image.load(os.path.join('Game_Characters', 'R1E.png')), 
        pygame.image.load(os.path.join('Game_Characters', 'R2E.png')), 
        pygame.image.load(os.path.join('Game_Characters', 'R3E.png')), 
        pygame.image.load(os.path.join('Game_Characters', 'R4E.png')), 
        pygame.image.load(os.path.join('Game_Characters', 'R5E.png')), 
        pygame.image.load(os.path.join('Game_Characters', 'R6E.png')), 
        pygame.image.load(os.path.join('Game_Characters', 'R7E.png')), 
        pygame.image.load(os.path.join('Game_Characters', 'R8E.png')), 
        pygame.image.load(os.path.join('Game_Characters', 'R9E.png')),
        pygame.image.load(os.path.join('Game_Characters', 'R10E.png')),
        pygame.image.load(os.path.join('Game_Characters', 'R11E.png'))
    ]
enemyLeft = [
        pygame.image.load(os.path.join('Game_Characters', 'L1E.png')), 
        pygame.image.load(os.path.join('Game_Characters', 'L2E.png')), 
        pygame.image.load(os.path.join('Game_Characters', 'L3E.png')), 
        pygame.image.load(os.path.join('Game_Characters', 'L4E.png')), 
        pygame.image.load(os.path.join('Game_Characters', 'L5E.png')), 
        pygame.image.load(os.path.join('Game_Characters', 'L6E.png')), 
        pygame.image.load(os.path.join('Game_Characters', 'L7E.png')), 
        pygame.image.load(os.path.join('Game_Characters', 'L8E.png')), 
        pygame.image.load(os.path.join('Game_Characters', 'L9E.png')),
        pygame.image.load(os.path.join('Game_Characters', 'L10E.png')),
        pygame.image.load(os.path.join('Game_Characters', 'L11E.png'))
    ]


class enemy(object):
    
    def __init__(self, x, y, width, height, end):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.path = [x, end]
        self.walkCount = 0
        self.vel = 3
        self.hitbox = (self.x + 17, self.y + 2, 31, 57)
        self.health = 10
        self.visible = True

    def move(self, game_win):
        if self.vel > 0 :
            if self.x + self.vel < self.path[1]:
                self.x += self.vel
            else:
                self.vel *= -1
                self.walkCount = 0
        else:
            if self.x - self.vel > self.path[0]:
                self.x += self.vel
            else:
                self.vel  *= -1
                self.walkCount = 0
        if self.health > 0:
            pygame.draw.rect(game_win, (255, 0, 0), (self.hitbox[0],self.hitbox[1] - 20, 50, 10))
            pygame.draw.rect(game_win, (0, 128, 0), (self.hitbox[0],self.hitbox[1] - 20, 50 - (5 * (10 - self.health)), 10))
        self.hitbox = (self.x + 17, self.y + 2, 31, 57)
        #pygame.draw.rect(game_win, (255, 0, 0), self.hitbox, 2)



    def draw(self, game_win):
        #The enemy automatically move
        self.move(game_win)
        if self.visible:
            if self.walkCount +1 >= 33:
                self.walkCount = 0

            if self.vel > 0:
                game_win.blit(enemyRight[self.walkCount // 3], (self.x, self.y))
                self.walkCount += 1
            else:
                game_win.blit(enemyLeft[self.walkCount // 3], (self.x, self.y))
                self.walkCount += 1

    def hit(self):
        if self.health > 0:
            self.health -= 1
        else:
            self.visible = False