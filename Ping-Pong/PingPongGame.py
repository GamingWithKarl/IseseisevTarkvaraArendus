# Importimine ning initialization
import pygame
from paddle import Paddle
from ball import Ball
pygame.init()
clock = pygame.time.Clock()

# Värvid
lWhite = (255, 255, 255)
red = (255, 0, 0)
blue = (0, 0, 255)
purple = (128, 0, 128)
black = (0, 0, 0)

# X, Y ja ekraani seaded..
X = 640
Y = 480
screen = pygame.display.set_mode([X, Y])
pygame.display.set_caption("PingPong - Karl Karulin")

#Spridid
all_sprites_list = pygame.sprite.Group()

#Paddle (Mida mängija liigutab
paddle = Paddle(black, 0, 0)
paddle.rect.x = 250
paddle.rect.y = 300

#Pall
ball = Ball(black, 0, 0)
ball.rect.x = 320
ball.rect.y = 240

#Spritide list
all_sprites_list.add(paddle)
all_sprites_list.add(ball)

# FPS ning skoor
FPS = 60
skoor = 0

#Main Loop
running = True
while running:

    # Mängu kinni panek ristist.
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    #Liikumine
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        paddle.moveLeft(5)
    if keys[pygame.K_RIGHT]:
        paddle.moveRight(5)

    # --- Main Game Logic --- #
    #Spritide uuendaine
    all_sprites_list.update()

    #Kood, mis teeb palli põrkavaks
    if ball.rect.x >=630:
        ball.velocity[0] = -ball.velocity[0]
    if ball.rect.x<=0:
        ball.velocity[0] = -ball.velocity[0]
    if ball.rect.y>470:
        skoor -= 2
        ball.velocity[1] = -ball.velocity[1]
    if ball.rect.y<30:
        ball.velocity[1] = -ball.velocity[1]

    #Collision palli ning paddle'i vahel         #Ei saa aru, miks peab pall läbi paddle'i minema aga okei.
    if pygame.sprite.collide_mask(ball, paddle) and ball.rect.y <= paddle.rect.y and ball.velocity[1] > 0:
        ball.rect.x -= ball.velocity[0]
        ball.rect.y -= ball.velocity[1]
        skoor += 1
        ball.bounce()

    #Skoor joon ning taustavörv
    screen.fill((135, 206, 250))
    pygame.draw.line(screen, lWhite, [0, 25], [640, 25], 2)

    #Skoor
    font = pygame.font.SysFont("consolas", 20)
    text = font.render("Skoor: " + str(skoor), 1, lWhite)
    screen.blit(text, (20,5))

        #Mangija saab punkti siis:
        #   -Kui pall puutub alust

        #Mängija EI saa punkti kui:
        #   -Kui pall puutub alumist äärt

    #Spritide kuvamine
    all_sprites_list.draw(screen)

    #Ekraani uuendamine
    pygame.display.flip()

    #FPS
    clock.tick(60)

#Mängust lahkumine, kui mäng saab läbi.
pygame.quit()