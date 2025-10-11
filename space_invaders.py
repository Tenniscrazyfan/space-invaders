import pygame
from pygame.locals import *

pygame.init()
screen = pygame.display.set_mode((900,500))
playing = True

b = pygame.transform.scale(pygame.image.load("images/space backround 2.png"),(900,500))
yellow_spaceship = pygame.transform.scale(pygame.image.load("images/yellow ship.png"),(80,80))
yellow_spaceship = pygame.transform.rotate(yellow_spaceship,90)
red_spaceship = pygame.transform.scale(pygame.image.load("images/red ship.png"),(80,80))
red_spaceship = pygame.transform.rotate(red_spaceship,270)
font = pygame.font.SysFont("Times New Roman" , 20)

yellow = pygame.Rect(100,300,55,40)
red = pygame.Rect(700,300,55,40)
border = pygame.Rect(450,0,10,500)
ylist = []
rlist = []
rlife = 10
ylife = 10

def handle_bullets():
    global ylist,yellow,red,rlist,rlife,ylife
    for y in ylist:
        y.x += 10
        if y.colliderect(red):
            print("hellow")
            rlife -= 1
            ylist.remove(y)


    for r in rlist:
        r.x -= 10
        if r.colliderect(yellow):
            ylife -= 1
            rlist.remove(r)

    


while playing :
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            playing=False
            pygame.quit()

        if event.type == pygame.KEYDOWN:
            if event.key == K_UP:
                yellow.y -= 10
            if event.key == K_DOWN:
                yellow.y += 10
            if event.key == K_LEFT:
                yellow.x -= 10
            if event.key == K_RIGHT and yellow.x <= 350:
                yellow.x += 10 
            

        if event.type == pygame.KEYDOWN:
            if event.key == K_w:
                red.y -= 10
            if event.key == K_s:
                red.y += 10
            if event.key == K_a and red.x >= 460:
                red.x -= 10
            if event.key == K_d:
                red.x += 10 

        if event.type == pygame.KEYDOWN:
            if event.key == K_SPACE:
                ybullet = pygame.Rect(yellow.x+60,yellow.y+40,10,5)
                ylist.append(ybullet)
            if event.key == K_f:
                rbullet = pygame.Rect(red.x-30,red.y+40,10,5)
                rlist.append(rbullet)
    
    for y in ylist:
        y.x += 10
        if y.colliderect(red):
            print("hellow")
            rlife -= 1
            ylist.remove(y)


    for r in rlist:
        r.x -= 10
        if r.colliderect(yellow):
            ylife -= 1
            rlist.remove(r)        


    screen.blit(b,(0,0))
    screen.blit(yellow_spaceship,(yellow.x,yellow.y))
    screen.blit(red_spaceship,(red.x,red.y))

    text1 = font.render("red spaceship lives = " + str(rlife),True,"white")
    screen.blit(text1,(700,30))

    text2 = font.render("yellow spaceship lives = " + str(ylife),True, "white")
    screen.blit(text2,(20,30))
    pygame.draw.rect(screen,"white",border)
    for i in ylist:
        pygame.draw.rect(screen, "white",i)
    for i in rlist:
        pygame.draw.rect(screen,"white",i)

    handle_bullets()

    pygame.display.update()