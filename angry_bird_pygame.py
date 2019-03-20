# -*- coding: utf-8 -*-
"""
Created on Tue Mar 19 23:18:47 2019

@author: 王一晨
"""
import pygame
from random import randint
from math import cos,sin,radians,sqrt
from time import sleep

pig_size = 8
bird_size = 8
angle = 45
force = 60
life = 3
score = 0
fail = False

class pig(pygame.sprite.Sprite):
    x = randint(200,610)
    y = randint(30,290)
    def __init__(self,radium,color):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface([radium*2,radium*2], pygame.SRCALPHA, 32)
        #self.image.fill((0,0,0))
        self.image = self.image.convert_alpha()
        pygame.draw.circle(self.image,color,(radium,radium),radium,0)
        self.rect = self.image.get_rect()
        self.rect.center = (self.x,self.y)
    def reflash(self):
        self.x = randint(200,610)
        self.y = randint(30,290)
        self.rect.center = (self.x,self.y)
    def pos(self):
        return self.x,self.y
        
class bird(pygame.sprite.Sprite):
    x = 30
    y = 290
    dx = 0
    dy = 0
    def __init__(self,radium,color):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface([radium*2,radium*2], pygame.SRCALPHA, 32)
        #self.image.fill((0,0,0))
        self.image = self.image.convert_alpha()
        pygame.draw.circle(self.image,color,(radium,radium),radium,0)
        self.rect = self.image.get_rect()
        self.rect.center = (self.x,self.y)
    def setting(self,angle,force):
        self.dx = force*cos(radians(angle))/15
        self.dy = -force*sin(radians(angle))/15
    def update(self):
        self.x += self.dx
        self.y += self.dy+0.5*9.80225/225
        self.dy += 9.80225/225
        self.rect.center = (self.x,self.y)    
    def reset(self):
        self.x = 30
        self.y = 290
        self.dx = 0
        self.dy = 0
        self.rect.center = (self.x,self.y)
    def bound(self,enter,check):
        if self.rect.bottom >screen.get_height()-5 or self.rect.right > screen.get_width():
            self.reset()
            return False,False,True
        else:
            return enter,check,False
    def pos(self):
        return self.x,self.y

pygame.init()
screen = pygame.display.set_mode((640,320))
pygame.display.set_caption("angry bird")
background = pygame.Surface(screen.get_size())
background = background.convert()
background.fill((255,255,255))
screen.blit(background,(0,0))

allsprite = pygame.sprite.Group()
pig1 = pig(pig_size,(0,255,0))
allsprite.add(pig1)
bird1 = bird(bird_size,(0,0,255))
allsprite.add(bird1)

clock = pygame.time.Clock()
running = True
enter = False
check = False 

while running:
    clock.tick(100)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    keys = pygame.key.get_pressed()
    if keys[pygame.K_SPACE]:
        enter = True
    if enter == False:
        if keys[pygame.K_LEFT] and angle < 90:
            angle += 0.5
        elif keys[pygame.K_RIGHT] and angle >0:
            angle -= 0.5
        elif keys[pygame.K_UP] and force<=110:
            force += 0.5
        elif keys[pygame.K_DOWN] and force>0:
            force -= 0.5
    background.fill((255,255,255))
    if enter == False:       
        pygame.draw.line(background,(50,50,50),(30,290),(30+force*cos(radians(angle)),290-force*sin(radians(angle))),3)
    else:
        if check == False:
            bird1.setting(angle,force)
            check = True
        bird1.update()
    x1,y1 = pig1.pos()
    x2,y2 = bird1.pos()
    
    if sqrt((x1-x2)**2+(y1-y2)**2)< (pig_size+bird_size):
        bird1.reset()
        pig1.reflash()
        enter,check = False,False
        score+=1
        
    enter,check,fail = bird1.bound(enter,check)
    if fail == True:
        life-=1
        fail = False
    if life == 0:
        font3 = pygame.font.SysFont("simhei",30)
        text1 = font3.render("Game Over  score:"+str(score),True,(255,0,0),(255,255,255))
        background.blit(text1,(190,130))
        screen.blit(background,(0,0))
        pygame.display.update() 
        sleep(1.5)
        break
        
    font2 = pygame.font.SysFont("simhei",15)
    text1 = font2.render("Life:"+str(life),True,(0,0,0),(255,255,255))
    background.blit(text1,(570,20))
    text2 = font2.render("score:"+str(score),True,(0,0,0),(255,255,255))
    background.blit(text2,(270,20))
    screen.blit(background,(0,0))
    allsprite.draw(screen)
    pygame.display.update()   
pygame.quit()