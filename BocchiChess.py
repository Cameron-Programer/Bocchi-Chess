import pygame
from sys import exit
clock = pygame.time.Clock()
icon = pygame.image.load("Assets\Visuals\icon.png")
pygame.display.set_icon(icon)
WIDTH = 835
HIGHT = 840
screen = pygame.display.set_mode((WIDTH,HIGHT))
pygame.display.set_caption("Bocchi The Rock Chess")

#Importing Visual assets from the assets folder
lTile = pygame.image.load("Assets\Visuals\LightTile-export.png")
lmTile = pygame.image.load("Assets\Visuals\LightTile-Wpingdot-export.png")
dTile = pygame.image.load("Assets\Visuals\DarkTile-export.png")
dmTile = pygame.image.load("Assets\Visuals\DarkTile-WpingDot-export.png")
board = pygame.image.load("Assets\Visuals\Chessboard(noB)-export50.png")
drunk = pygame.image.load("Assets\Visuals\Drunklady-export.png")
ryo = pygame.image.load("Assets\Visuals\Ryo-export.png")



po = [(1,1),(104,1),(210,1),(314,1),(419,1),(521,1),(626,1),(730,1)]
wpo = [1,104,210,314,419,521,626,730]
hpo = [1,104,211,314,420,524,630,734]

#Pece locations

drunkX = wpo[1];drunkY = hpo[1]
ryoX = 0; ryoY = 0
ryoX2 = wpo[7]; ryoY2 = hpo[0]

playercharlocalX = [drunkX, ryoX,ryoX2]
playercharlocalY = [drunkY, ryoY,ryoY2]



ryoRect = ryo.get_rect(topleft = (ryoX,ryoY))
drunkRect = drunk.get_rect(topleft = (drunkX, drunkY))
ryoRect2 = ryo.get_rect(topleft = (ryoX2, ryoY2))




def MkBoard():
    #64 total slots 
    #32 light ; 32 Dark 
    x = 0
    for i in range (0,7):
        if i == 7:
            x = x+1
        if i%2 == 0:
            screen.blit(lTile,(wpo[i],hpo[x]))
        else:
            screen.blit(dTile,(wpo[i],hpo[x]))



def ryoMove():
    ryoX = wpo[mouselocal()[0]]
    ryoY = hpo[mouselocal()[1]]
    return(ryoX,ryoY)

def drunkMove():
    if pygame.mouse.get_pressed()[0] == True:
        drunkX = wpo[mouselocal()[0]]
        drunkY = hpo[mouselocal()[1]]



def mouselocal():
    x = pygame.mouse.get_pos()[0]
    y = pygame.mouse.get_pos()[1]
    global xlocal
    global ylocal
    xlocal = False
    ylocal = False
    for i in range (0,8):
        if x > wpo[i]:
            xlocal = i 
        if y > hpo[i]:
            ylocal = i
    print(xlocal,",",ylocal)
    return(xlocal,ylocal)

screen.blit(board,(0,0))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit(); exit()
    pygame.display.update()
    clock.tick(60)
    screen.blit(board,(0,0))
    screen.blit(drunk,(drunkX,drunkY))
    screen.blit(ryo,(ryoX,ryoY))
    screen.blit(ryo,(ryoX2,ryoY2))
    if ryoRect.collidepoint(pygame.mouse.get_pos()):
        playerselcted = ryo
        print("poggers")
    
    if playerselcted == ryo:
        ryox = ryoMove()[0]
        ryoY = ryoMove()[1]
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                playerselcted = False

