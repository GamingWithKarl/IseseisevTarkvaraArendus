#Import ja värvid
import pygame
from random import randint
black = (0,0,0)

#klass pall
class Ball(pygame.sprite.Sprite):

    def __init__(self, color, X, Y):

        super().__init__()
        #Palli pilt ning selle mask
        self.image = pygame.image.load("Pildid/ball.png")
        self.mask = pygame.mask.from_surface(self.image)

        #Palli joonistamine ekraanile
        pygame.draw.rect(self.image, color, [0, 0, X, Y])
        self.velocity = [randint(4, 8), randint(-8, 8)]
        self.rect = self.image.get_rect()

    #Uuendamine palli x ja y kordinaate
    def update(self):
        self.rect.x += self.velocity[0]
        self.rect.y += self.velocity[1]

    #Palli põrkamine.
    def bounce(self):
        self.velocity[0] = -self.velocity[0]
        self.velocity[1] = randint(-8, 8)
