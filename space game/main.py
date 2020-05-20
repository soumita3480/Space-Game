import pygame
import random
import math
pygame.init()
run=True
screen=pygame.display.set_mode((800,500))
icon=pygame.image.load('spaceship.png')
sky=pygame.image.load('sky.jpg')
pygame.display.set_icon(icon)
spaceship=pygame.image.load('spaceship.png')
pygame.display.set_caption('space game')

#ship
player=pygame.image.load('player.png')
shipx=370
shipy=430
shipmovex=0

#monster
monsterx=random.randint(0,730)
monstery=random.randint(50,150)
monstermovex=2
monstermovey=50
monster=pygame.image.load('monster.png')

#bullet
bullet=pygame.image.load('bullet.png')
bulletx=370
bullety=370
bulletmovey=2
bulletseen=0
count=0

#score
score=0
scorefont=pygame.font.Font('freesansbold.ttf',32)
scoreposx=10
scoreposy=10

#game over
overfont=pygame.font.Font('freesansbold.ttf',64)
overposx=200
overposy=100
gamedone=0

#score function

def scorfun(scoreval,x,y):
    score_value=scorefont.render("score:"+str(scoreval),True,(255,255,255))
    screen.blit(score_value,(x,y))

#ship function

def spaceship(x,y):
    screen.blit(player,(x,y))

#game over function
def gameover(x,y):
    global gamedone
    gamedone=1
    gameover=overfont.render("GAME OVER",True,(255,0,0))
    screen.blit(gameover,(x,y))


#monster function

def devil(x,y):
    if gamedone==0:
        screen.blit(monster,(x,y))

#bullet function
def bulet(x,y):
    screen.blit(bullet,(x,y))

#collision of bullet and monster
def collision(bulletx,bullety,monsterx,monstery):
    col=math.sqrt(math.pow((bulletx-monsterx),2)+math.pow((bullety-monstery),2))
    return col

#game loop
while run:
    screen.fill((0, 0, 0))
    screen.blit(sky,(0,0))
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            run=False
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_LEFT:
                shipmovex=-2
            if event.key==pygame.K_RIGHT:
                shipmovex=+2
        if event.type==pygame.KEYUP:
            if event.key==pygame.K_RIGHT or pygame.K_LEFT:
                shipmovex=0
            if event.key==pygame.K_SPACE:
                bulletseen=1

    monsterx += monstermovex
    if monsterx<=2:
        monstermovex=+2
        monstery += monstermovey
    elif monsterx>=735:
        monstermovex=-2
        monstery+=monstermovey

    if monstery >230:
        gameover(overposx, overposy)

    shipx+=shipmovex
    if shipx>=735:
        shipx=735
    if shipx<=2:
        shipx=2

    if bulletseen==1:
        bullety -= bulletmovey
        count+=1
        if bullety<=0:
            bulletseen=0
            bullety=370
            bulletx=350
            count=0
        if count==1:
            tempshipx=shipx
            bulet(tempshipx,bullety)
        else:
            bulet(tempshipx,bullety)

#function call
    spaceship(shipx,shipy)
    devil(monsterx,monstery)
    col = collision(bulletx, bullety, monsterx, monstery)

    if bulletseen==1:
        if col < 90:
            bulletseen = 0
            bullety = 370
            bulletx = 350
            count=0
            monsterx = random.randint(0, 730)
            monstery = random.randint(50, 150)
            score += 1
    scorfun(score,scoreposx,scoreposy)

    pygame.display.update()
