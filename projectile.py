import pygame

class projectile(object):
    def __init__(self, x, y, radius, color, facing):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.facing = facing
        self.velocity = 8 * facing

    def draw(self, game_win):
        pygame.draw.circle(game_win, self.color, (self.x, self.y), self.radius)