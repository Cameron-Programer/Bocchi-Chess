import pygame
from sys import exit
clock = pygame.time.Clock()
WIDTH = 835
HIGHT = 840
screen = pygame.display.set_mode((WIDTH,HIGHT))
#Setting app name and icon
pygame.display.set_caption("Bocchi The Rock Chess")
icon = pygame.image.load("Assets\Visuals\icon.png")
pygame.display.set_icon(icon)
#Importing Visual assets from the assets folder
lTile = pygame.image.load("Assets\Visuals\LightTile-export.png")
lmTile = pygame.image.load("Assets\Visuals\LightTile-Wpingdot-export.png")
dTile = pygame.image.load("Assets\Visuals\DarkTile-export.png")
dmTile = pygame.image.load("Assets\Visuals\DarkTile-WpingDot-export.png")
board = pygame.image.load("Assets\Visuals\Chessboard(noB)-export50.png")
drunk = pygame.image.load("Assets\Visuals\Drunklady-export.png")
ryo = pygame.image.load("Assets\Visuals\Ryo-export.png")
kita = pygame.image.load("Assets\Visuals\Kita-export.png")
bocchi = pygame.image.load("Assets\Visuals\Bocchi(normal)-export.png")
ni = pygame.image.load("Assets\\Visuals\\Nijika-export.png")
gitar = pygame.image.load("Assets\Visuals\GuitarDude-export.png")

#Moveable positions
po = [(1,1),(104,1),(210,1),(314,1),(419,1),(521,1),(626,1),(730,1)]
wpo = [1,104,210,314,419,521,626,730]
hpo = [1,104,211,314,420,524,630,734]

#STARTUP Pece locations
def reset():
    global drunkX
    global drunkY
    global ryoX
    global ryoY
    global kitaX
    global kitaY
    global niX
    global niY
    global bocchiX
    global bocchiY
    global ryoX2
    global ryoY2
    global nijiX2
    global nijiY2
    global drunkX2
    global drunkY2
    global pawnXY
    global pawnrect
    drunkX = wpo[1];drunkY = hpo[0]
    ryoX = 0; ryoY = 0
    ryoX2 = wpo[7]; ryoY2 = hpo[0]
    kitaX = wpo[3]; kitaY = hpo[0]
    bocchiX = wpo[4]; bocchiY = hpo[0]
    niX = wpo[2]; niY = hpo[0]
    drunkX2 = wpo[6];drunkY2 = hpo[0]
    nijiX2 = wpo[5]; nijiY2 = hpo[0]
    pawnXY = [[wpo[0],hpo[1]],[wpo[1],hpo[1]],[wpo[2],hpo[1]],[wpo[3],hpo[1]],[wpo[4],hpo[1]],[wpo[5],hpo[1]],[wpo[6],hpo[1]],[wpo[7],hpo[1]]]
    pawnrect = []
reset()

playerselcted = False

def move():
    x = wpo[mouselocal()[0]]
    y = hpo[mouselocal()[1]]
    return(x,y)

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
    #print(xlocal,",",ylocal)
    return(xlocal,ylocal)

screen.blit(board,(0,0))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit(); exit()
    pygame.display.update()
    clock.tick(60)
    #Get rectanglas for the icons
    ryoRect = ryo.get_rect(topleft = (ryoX,ryoY))
    drunkRect = drunk.get_rect(topleft = (drunkX, drunkY))
    ryoRect2 = ryo.get_rect(topleft = (ryoX2, ryoY2))
    kitaRect = kita.get_rect(topleft = (kitaX,kitaY))
    bocchiRect = bocchi.get_rect(topleft = (bocchiX,bocchiY))
    niRect = ni.get_rect(topleft = (niX,niY))
    drunkRect2 = drunk.get_rect(topleft = (drunkX2, drunkY2))
    nijiRect2 = kita.get_rect(topleft = (nijiX2,nijiY2))
    for i in range (0,8):
        pawnrect.append(gitar.get_rect(topleft = (pawnXY[i])))
        
    #load the screen with assets
    screen.blit(board,(0,0))
    screen.blit(drunk,(drunkRect))
    screen.blit(ryo,(ryoRect))
    screen.blit(ryo,(ryoRect2))
    screen.blit(kita,(kitaRect))
    screen.blit(bocchi,(bocchiRect))
    screen.blit(ni,(niRect))
    screen.blit(drunk,(drunkRect2))
    screen.blit(ni,(nijiRect2))
    for i in range (0,8):
        screen.blit(gitar,(pawnXY[i]))
    #check if the player is trying to select a item
    if ryoRect.collidepoint(pygame.mouse.get_pos()):
        if pygame.mouse.get_pressed()[0] == True:
            playerselcted = ryo
            print("Ryo Selected")
    elif drunkRect.collidepoint(pygame.mouse.get_pos()):
        if pygame.mouse.get_pressed()[0] == True:
            playerselcted = drunk
            print("Drunk Selected")
    elif ryoRect2.collidepoint(pygame.mouse.get_pos()):
        if pygame.mouse.get_pressed()[0] == True:
            playerselcted = "ryo2"
            print("Ryo2 Selected")
    elif kitaRect.collidepoint(pygame.mouse.get_pos()):
        if pygame.mouse.get_pressed()[0] == True:
            playerselcted = kita
            print("Kita Selected")
    elif bocchiRect.collidepoint(pygame.mouse.get_pos()):
        if pygame.mouse.get_pressed()[0] == True:
            playerselcted = bocchi
            print("Bocchi Selected")
    elif niRect.collidepoint(pygame.mouse.get_pos()):
        if pygame.mouse.get_pressed()[0] == True:
            playerselcted = ni
            print("Nijika Selected")
    elif drunkRect2.collidepoint(pygame.mouse.get_pos()):
        if pygame.mouse.get_pressed()[0] == True:
            playerselcted = "drunk2"
            print("Drunk2 Selected")
    elif nijiRect2.collidepoint(pygame.mouse.get_pos()):
        if pygame.mouse.get_pressed()[0] == True:
            playerselcted = "niji2"
            print("niji2 Selected")
    else: 
        for i in range (0,8):
            if pawnrect[i].collidepoint(pygame.mouse.get_pos()):
                if pygame.mouse.get_pressed()[0] == True:
                    playerselcted = ("pawn",i)
                    print("Gitar Selected")

    

    if playerselcted == ryo:
        ryoX = move()[0]
        ryoY = move()[1]
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                playerselcted = False
        elif pygame.mouse.get_pressed()[2] == True:
            playerselcted = False
    elif playerselcted == drunk:
        drunkX = move()[0]
        drunkY = move()[1]
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                playerselcted = False
        elif pygame.mouse.get_pressed()[2] == True:
            playerselcted = False
    elif playerselcted == "ryo2":
        ryoX2 = move()[0]
        ryoY2 = move()[1]
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                playerselcted = False
        elif pygame.mouse.get_pressed()[2] == True:
            playerselcted = False
    elif playerselcted == kita:
        kitaX = move()[0]
        kitaY = move()[1]
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                playerselcted = False
        elif pygame.mouse.get_pressed()[2] == True:
            playerselcted = False
    elif playerselcted == bocchi:
        bocchiX = move()[0]
        bocchiY = move()[1]
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                playerselcted = False
        elif pygame.mouse.get_pressed()[2] == True:
            playerselcted = False
    elif playerselcted == ni:
        niX = move()[0]
        niY = move()[1]
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                playerselcted = False
        elif pygame.mouse.get_pressed()[2] == True:
            playerselcted = False
    elif playerselcted == "drunk2":
        drunkX2 = move()[0]
        drunkY2 = move()[1]
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                playerselcted = False
        elif pygame.mouse.get_pressed()[2] == True:
            playerselcted = False
    elif playerselcted == "niji2":
        nijiX2 = move()[0]
        nijiY2 = move()[1]
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                playerselcted = False
        elif pygame.mouse.get_pressed()[2] == True:
            playerselcted = False
   
    for i in range (0,8):
        if playerselcted == ("pawn",i):
            print("/")
            pawnXY[i][0] = move()[0]
            pawnXY[i][1] = move()[1]
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    playerselcted = False
            elif pygame.mouse.get_pressed()[2] == True:
                playerselcted = False

    if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                reset()
                print("Board reset")
            
