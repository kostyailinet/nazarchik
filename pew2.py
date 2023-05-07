from pygame import *
import pygame
import random

pygame.display.set_icon(pygame.image.load("pix.jpg"))

mixer.init()
mixer.music.load('oliveee.mp3')
mixer.music.play()
fire_sound = mixer.Sound('123.mp3')

bullets = []
playyer = []

img_b = "ke2.png" 
img_h = "ada.jpg"  
img_e = "pix.jpg"

pygame.init()
pygame.font.get_default_font()
f = pygame.font.Font(None, 35)

pygame.init()
pygame.font.get_default_font()
h = pygame.font.Font(None, 35)

class GameSprite(sprite.Sprite):
    
    def __init__(self, player_image, player_x, player_y, size_x, size_y, player_speed):
        
        sprite.Sprite.__init__(self)
        self.image = transform.scale(
            image.load(player_image), (size_x, size_y))
        self.speed = player_speed

        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y

    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def update(self):
        keys = key.get_pressed()
        if keys[K_a] and self.rect.x > 2:
            self.rect.x -= self.speed
        if keys[K_d] and self.rect.x < win_width - self.rect.width:
            self.rect.x += self.speed
        if keys[K_SPACE]:
            self.fire()
        playyer.append(ship)

    def fire(self):
        bul = Bullet("ner.jpg", self.rect.centerx, self.rect.top, 15, 20, -15)
        bullets.append(bul)

class Enemy(GameSprite):
    def update(self):
        self.rect.y += self.speed
        if self.rect.y > win_height + 10:
            self.rect.y = -80
            self.rect.x = random.randint(0, win_width - 80)
            self.speed = random.uniform(2, 5)
            return True

class Bullet(GameSprite):
    def update(self):
        self.rect.y += self.speed
        if self.rect.y <= 0:
            self.kill()

propuhcheno = 0
schet = 0
pln = 10
pon = 100



win_width = 700
win_height = 500
display.set_caption("Шутер")
window = display.set_mode((win_width, win_height))
background = transform.scale(image.load(img_b), (win_width, win_height))

ship = Player(img_h, 5, win_height - 100, 80, 100, 5)

enemys = []
for i in range(5):
    e = Enemy(img_e, random.randint(0, win_width - 100), -80, 70, 40, random.uniform(2, 5))
    enemys.append(e)

clock = time.Clock()

finish = False

run = True  

while run:
    
    for e in event.get():
        if e.type == QUIT:
            run = False

    if not finish:
        window.blit(background, (0, 0))

        r = f.render("пропущено:" + str(propuhcheno), True, (255, 250, 250))
        window.blit(r, (10, 10))

        b = h.render("Рахунок:" + str(schet), True, (255, 250, 250))
        window.blit(b, (10, 40))

        for e in enemys:
            g = e.update()
            e.reset()
            if g:
                propuhcheno += 1

            if propuhcheno >= pon:
                enemys.remove(e)
                playyer.remove(ship)
                b = h.render("ти" + " програв", True, (255, 250, 250))
                window.blit(b, (250, 250))
                b = h.render("рахунок:" + str(schet), True, (255, 250, 250))
                window.blit(b, (270, 280))
                finish = True
            else:
                finish = False

        if schet == pln:
            enemys.remove(e)
            playyer.remove(ship)
            b = h.render("ти" + " виграв", True, (255, 250, 250))
            window.blit(b, (250, 250))
            b = h.render("Счёт:" + str(schet), True, (255, 250, 250))
            window.blit(b, (270, 280))
            finish = True

        ship.update()
        ship.reset()

        for bul in bullets:
            bul.update()
            bul.reset()
            for e  in enemys:
                if pygame.sprite.collide_rect(bul, e):
                    bullets.remove(bul)
                    e.rect.y = 0
                    e.rect.x = random.randint(0, 600)
                    schet += 1
                    break

        for e in enemys:
            if pygame.sprite.collide_rect(ship, e):
                enemys.remove(e)
                playyer.remove(ship)
                b = h.render("ти" + " програл", True, (255, 250, 250))
                window.blit(b, (250, 250))
                b = h.render("Счёт:" + str(schet), True, (255, 250, 250))
                window.blit(b, (270, 280))
                finish = True

        display.update()
    clock.tick(60)