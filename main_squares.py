import pygame
import random
import os

pygame.init()

pygame.display.set_caption("EndToper's squares")
WHITE = (255,255,255)
BLACK = (0,0,0)
HEIGHT = 450
WIDTH = 450
print(WIDTH)
FPS = 60
screen = pygame.display.set_mode((WIDTH,HEIGHT))
run = True
clock = pygame.time.Clock()


class sq(pygame.sprite.Sprite):
    def __init__(self,x,y,color):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((40, 40))
        self.rect = self.image.get_rect()
        self.rect.center = (x,y)
        self.color = color
        self.image.fill(color)
    def update(self):
        color = (random.randint(0,255),random.randint(0,255),random.randint(0,255))
        self.image.fill(color)
        

all_sprites = pygame.sprite.Group()
squares = []
poses = []
qw = 0
qw2 = 0
mqw = 0
mqw2 = 0
for i in range(1,100):
    x = 22.5+45*qw
    y = 22.5+45*qw2
    qw2 = qw2 + 1
    if i % 10 == 0 and i != 0:
        qw2 = 0
        qw = qw + 1
    color = (random.randint(0,255),random.randint(0,255),random.randint(0,255))
    q = sq(x,y,color)
    all_sprites.add(q)
    squares.append(q)
    if qw2 != 0:
        mqw = qw + 1
    mqw2 = qw2
    if mqw2 == 0:
        mqw2 = 3
    poses.append((mqw,mqw2))
print(poses)
while run:
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            run = False
        if i.type == pygame.KEYDOWN and game_run == True:
            if i.key == pygame.K_ESCAPE:
                run = False
        elif i.type == pygame.MOUSEBUTTONDOWN:
            for i2 in range(len(squares)):
                if squares[i2].rect.collidepoint(pygame.mouse.get_pos()) and i.button == 1 or squares[i2].rect.collidepoint(pygame.mouse.get_pos()) and i.button == 3 or i.button == 2 or i.button == 4 or i.button == 5:
                    if i.button == 3 or i.button == 2 or i.button == 4 or i.button == 5:
                        print("симулятор танцпола активирован")
                    else:
                        print(poses[i2])
                    squares[i2].update()
    all_sprites.draw(screen)
    pygame.display.flip()
pygame.quit()