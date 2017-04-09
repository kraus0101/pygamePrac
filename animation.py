import pygame,sys,time
from pygame.locals import *

#set up the pygame
pygame.init()

#set up a window
WINDOWWIDTH=400
WINDOWHEIGHT=400
windowSurface=pygame.display.set_mode((WINDOWWIDTH,WINDOWHEIGHT),0,32)
pygame.display.set_caption('Animation')

#set up the direction variable
DOWNLEFT=1
DOWNRIGHT=3
UPLEFT=7
UPRIGHT=9

MOVESPEED=4

#SET UP THE COLOR
BLACK=(0,0,0)
RED=(255,0,0)
GREEN=(0,255,0)
BLUE=(0,0,255)

#set up the block data structure
b1={'rect':pygame.Rect(300,80,50,100),'color':RED, 'dir':UPRIGHT}
b2={'rect':pygame.Rect(200,200,20,20),'color':GREEN,'dir':UPLEFT}
b3={'rect':pygame.Rect(100,150,60,60),'color':BLUE,'dir':DOWNLEFT}
block=[b1,b2,b3]

#Do the game loop
while True:
    #confirm the event
    for event in pygame.event.get():
        if event.type==QUIT:
            pygame.quit()
            sys.exit()

    #fill the windowSurface
    windowSurface.fill(BLACK)

    for b in block:
        #draw block data structure
        if b['dir']==UPRIGHT:
            b['rect'].left+=MOVESPEED
            b['rect'].top-=MOVESPEED
        if b['dir']==UPLEFT:
            b['rect'].left-=MOVESPEED
            b['rect'].top-=MOVESPEED
        if b['dir']==DOWNLEFT:
            b['rect'].left-=MOVESPEED
            b['rect'].top+=MOVESPEED
        if b['dir']==DOWNRIGHT:
            b['rect'].left+=MOVESPEED
            b['rect'].top+=MOVESPEED

        #confirm the block go out of the window
        if b['rect'].top<0:
            #if block go out of the top window
            if b['dir']==UPLEFT:
                b['dir']=DOWNLEFT
            if b['dir']==UPRIGHT:
                b['dir']=DOWNRIGHT
        if b['rect'].bottom>WINDOWHEIGHT:
            #if block go out of the bottom of the window
            if b['dir']==DOWNRIGHT:
                b['dir']=UPRIGHT
            if b['dir']==DOWNLEFT:
                b['dir']=UPLEFT
        if b['rect'].left<0:
            #if block go out of the left of the window
            if b['dir']==DOWNLEFT:
                b['dir']=DOWNRIGHT
            if b['dir']==UPLEFT:
                b['dir']=UPRIGHT
        if b['rect'].right>WINDOWWIDTH:
            #if block go out of the right of the window
            if b['dir']==DOWNRIGHT:
                b['dir']=DOWNLEFT
            if b['dir']==UPRIGHT:
                b['dir']=UPLEFT

        #draw the surface on the windowSurface
        pygame.draw.rect(windowSurface,b['color'],b['rect'])

    #draw the surface on the screen
    pygame.display.update()
    time.sleep(0.02)