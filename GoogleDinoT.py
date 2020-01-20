import pygame
import os
import random

def load_image(name, colorkey=None):
    fullname = os.path.join('data', name)
    image = pygame.image.load(fullname).convert()
    return image
pygame.init()
size = width, height = 500, 500
screen = pygame.display.set_mode(size)
running = True
clock = pygame.time.Clock()
image_cactus = load_image("Cactus.png")
image_dino1 = load_image("Dino1.png")
image_dino2 = load_image("Dino2.png")
image_dinojump = load_image("DinoJump.png")
all_sprites = pygame.sprite.Group()
sprite_dino = pygame.sprite.Sprite()
sprite_dino.image = image_dino1
sprite_dino.rect = sprite_dino.image.get_rect()
sprite_dino.rect.x = 20
sprite_dino.rect.y = 250
all_sprites.add(sprite_dino)
sprite_cactus = pygame.sprite.Sprite()
sprite_cactus.image = image_cactus
sprite_cactus.rect = sprite_cactus.image.get_rect()
sprite_cactus.rect.x = 470
sprite_cactus.rect.y = 250
all_sprites.add(sprite_cactus)
all_sprites.draw(screen)
score = 0
h = 0
v = 0
jump = False
b = 0
dif = 3
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if not(jump):
                jump = True
                v = 21
                h = 1
    if jump:
        v -= h
        sprite_dino.rect.y -= v
        if v == -20:
            v = 0
            h = 0
            jump = False
            sprite_dino.image = image_dino1
        sprite_dino.image = image_dinojump
    if sprite_dino.image == image_dino1 and b == 10:
        sprite_dino.image = image_dino2
        b = 0
        score += 1
    elif b == 10:
        sprite_dino.image = image_dino1
        b = 0
        score += 1
    b += 1
    if sprite_cactus.rect.x < 0:
        sprite_cactus.rect.x = 470
    else:
        sprite_cactus.rect.x -= dif
    if score % 50 == 0 and score != 0:
        dif += 0.1
    if pygame.Rect.colliderect(sprite_dino.rect, sprite_cactus.rect):
        running = False
    screen.fill((0,0,0))
    font = pygame.font.Font(None, 40)
    text = font.render(str(score), 1, (255, 0, 0))
    screen.blit(text, (400, 0))
    all_sprites.draw(screen)
    clock.tick(60)
    pygame.display.flip()
pygame.quit()