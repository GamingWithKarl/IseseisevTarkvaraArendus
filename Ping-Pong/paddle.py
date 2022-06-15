#Import, värvus ning pilt
import pygame
must = (0,0,0)
image = pygame.image.load("Pildid/pad.png")

#Klass paddle
class Paddle(pygame.sprite.Sprite):
    def __init__(self, color, pX, pY):
        super().__init__()

        #Paddle'i transformimine õigeks resolutsiooniks. Samuti selle maskimine
        self.image = pygame.transform.scale(image, (120, 20))
        self.mask = pygame.mask.from_surface(self.image)

        # Paddle'i joonistamine ekraanile
        pygame.draw.rect(self.image, color, [0, 0, pX, pY])
        self.rect = self.image.get_rect()

    #Liikumise funksioon (vasakule liigutamine)
    def moveLeft(self, pixels):
        self.rect.x -= pixels

        if self.rect.x < 0:
            self.rect. x = 0

    #Liikumise funksioon (paremale liigutamine)
    def moveRight(self, pixels):
        self.rect.x += pixels

        if self.rect.x > 540:
            self.rect.x = 520
