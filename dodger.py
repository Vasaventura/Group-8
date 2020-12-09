import pygame, random, sys
from pygame.locals import *

WINDOWWIDTH = 950
WINDOWHEIGHT = 750
WIN = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))
TEXTCOLOR = ('white')
BACKGROUNDCOLOR = (255, 255, 255)
ENDGAMEBACKGROUNDCOLOR = ('black')
MENUBACKGROUNDCOLOR = ('red')
# MenuGameBackground = pygame.image.load("snow.gif") #si vous voulez
FPS = 60
MINSIZE = 30  # ici le code a été modifié en suivant les conseils du livre (Ai Swegart) Ch. 20, Pg. 353-354
MEDSIZE = 45
MAXSIZE = 60  # la taille max d'un caractere
BADDIEMINSPEED = 1  # la vitesse minimale d'ennemi
BADDIEMAXSPEED = 4  # la vitesse maximale d'ennemi
ADDNEWBADDIERATE = 24  # le taux de reproduction de nouveaux ennemis
ADDNEWLUTINRATE=48 # le taux de reproduction de lutins
ADDNEWCHIMNEYRATE=316 # le taux de reproduction de cheminees
LUTINSPEED=1
CHIMNEYSPEED = 2
PLAYERMOVERATE = 5  # la vitesse de déplacement de jouer
player=["image pour jouer"]

def Menu():
    pygame.init()
    window = pygame.display.set_mode((WINDOWWIDTH,WINDOWHEIGHT))
    menu = pygame.image.load("écran_start.png").convert()
    img = pygame.transform.scale(menu, (WINDOWWIDTH, WINDOWHEIGHT))
    window.blit(img, (0,0))
    pygame.display.flip()
    player[0]=MenuPressKey()
    pygame.display.update()

def Chooseplayer():
    window = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))
    menu = pygame.image.load("choix_joueur.png").convert()
    img = pygame.transform.scale(menu, (WINDOWWIDTH, WINDOWHEIGHT))
    window.blit(img, (0,0))
    pygame.display.flip()
    MenuPressKey()
    pygame.display.update()

def Howtoplay():
    pygame.init()
    window = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))
    menu = pygame.image.load("How_to_play.png").convert()
    img = pygame.transform.scale(menu, (WINDOWWIDTH, WINDOWHEIGHT))
    window.blit(img, (0, 0))
    pygame.display.flip()
    MenuPressKey()
    pygame.display.update()

def drawText(text, font, surface, x, y):
    textobj = font.render(text, 1, TEXTCOLOR)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    surface.blit(textobj, textrect)

def terminate():
    pygame.quit()
    sys.exit()

def waitForPlayerToPressKey():
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                terminate()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:  # Pressing ESC quits.
                    terminate()
                return

def MenuPressKey():
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                terminate()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:  # Pressing ESC quits.
                    terminate()
                if event.key == K_j:
                    Chooseplayer()
                if event.key == K_p:
                    return "mario"
                if event.key == K_n:
                    return "peach"
                if event.key == K_t:
                    Menu()
                if event.key == K_q:
                    Howtoplay()
            if event.type == KEYUP:
                if event.key == K_p:
                    return "mario"
                if event.key == K_n:
                    return "peach"
def terminate():
    pygame.quit()
    sys.exit()

def playerHasHitBaddie(playerRect, baddies):
    for b in baddies:
        if playerRect.colliderect(b['rect']):
            baddies.remove(b)
            return True
    return False


def playerHasHitLutin(playerRect, lutin):    #code pour les lutins
   for l in lutin:
        if playerRect.colliderect(l['rect']):
            lutin.remove(l)
            return True

def send_Gift(playerRect, chimneys, score, feedback_sound):
    for c in chimneys:
       if playerRect.colliderect(c['rect']):
            for event in pygame.event.get():
                if event.type == KEYDOWN:

                    if event.key == K_SPACE:
                        feedback_sound.play()
                        score += 1
                        c['rect'].move_ip(0, 1000)
                        if event.key == K_z:
                            reverseCheat = True
                        if event.key == K_x:
                            slowCheat = True
                        if event.key == K_LEFT or event.key == K_a:
                            moveRight = False
                            moveLeft = True
                        if event.key == K_RIGHT or event.key == K_d:
                            moveLeft = False
                            moveRight = True
                        if event.key == K_UP or event.key == K_w:
                            moveDown = False
                            moveUp = True
                        if event.key == K_DOWN or event.key == K_s:
                            moveUp = False
                            moveDown = True
                            # option mute pour enlever le son du jeu. Par contre le son du Game Over reste toujours

                        if event.type == KEYUP:
                            if event.key == K_z:
                                reverseCheat = False
                                scoreLutin = 0
                            if event.key == K_x:
                                slowCheat = False
                                scoreLutin = 0
                            if event.key == K_ESCAPE:
                                terminate()

                            if event.key == K_LEFT or event.key == K_a:
                                moveLeft = False
                            if event.key == K_RIGHT or event.key == K_d:
                                moveRight = False
                            if event.key == K_UP or event.key == K_w:
                                moveUp = False
                            if event.key == K_DOWN or event.key == K_s:
                                moveDown = False

                        if event.type == MOUSEMOTION:
                            # If the mouse moves, move the player where to the cursor.
                            playerRect.centery = event.pos[1]
                        return True
                    else:
                        return False

def MouseControls(MOUSEMOTION):
    if event.type == MOUSEMOTION:
        # If the mouse moves, move the player where to the cursor.
        playerRect.centerx = event.pos[0]
        playerRect.centery = event.pos[1]

def PlayerMouvement(playerRect):
    # Move the player around.
    if moveLeft and playerRect.left > 0:
        playerRect.move_ip(-1 * PLAYERMOVERATE, 0)
    if moveRight and playerRect.right < WINDOWWIDTH:
        playerRect.move_ip(PLAYERMOVERATE, 0)
    if moveUp and playerRect.top > 0:
        playerRect.move_ip(0, -1 * PLAYERMOVERATE)
    if moveDown and playerRect.bottom < WINDOWHEIGHT:
        playerRect.move_ip(0, PLAYERMOVERATE)

def bad_character_movement(objects,WINDOWWIDTH):
    for o in objects:
        if not reverseCheat and not slowCheat:
            o['rect'].move_ip(-o['speed'], 0)
        elif reverseCheat:
            o['rect'].move_ip(5, 0)
        elif slowCheat:
            o['rect'].move_ip(-1, 0)

    # Delete baddies that have come from the left.
    for o in objects:
        if o['rect'].left > WINDOWWIDTH:
            objects.remove(o)
def good_character_movement(objects,WINDOWWIDTH):
        for o in objects:
            if not reverseCheat and not slowCheat:
                o['rect'].move_ip(-o['speed'], 0)
            elif reverseCheat:
                o['rect'].move_ip(-1, 0)
            elif slowCheat:
                o['rect'].move_ip(5, 0)

        # Delete lutins that have come from the left.
        for o in objects[:]:
            if o['rect'].left > WINDOWWIDTH:
                objects.remove(o)

def vie(lives):
    if lives != 0:
        windowSurface.blit(coeur, (10, WINDOWHEIGHT-40))
    if lives > 1:
        windowSurface.blit(coeur, (60, WINDOWHEIGHT-40))
    if lives == 3:
        windowSurface.blit(coeur, (110, WINDOWHEIGHT-40))


def drawText(text, font, surface, x, y):
    textobj = font.render(text, 1, TEXTCOLOR)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    surface.blit(textobj, textrect)

# Set up pygame, the window, and the mouse cursor.
Menu()
mainClock = pygame.time.Clock()
windowSurface = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))
pygame.display.set_caption('X-Mas Dodger')
pygame.mouse.set_visible(False)

# Set up the fonts.
font = pygame.font.SysFont(None, 48, bold=True)

# Set up sounds.
gameOverSound = pygame.mixer.Sound('grinch_gameoversound.mp3')
BellsSound = pygame.mixer.Sound('Bells Sound effect.mp3')
PresentSound = pygame.mixer.Sound('Present_sound.mp3')
PresentDelivered = pygame.mixer.Sound('presents_delivery.mp3')
damageSound = pygame.mixer.Sound('damage.mp3')
YaySound = pygame.mixer.Sound('Yay.mp3')
musicPlaying = True

playerImage = pygame.image.load('santa-player.png')
playerImage2= pygame.transform.scale(pygame.image.load('Mere_Noel.png'),(40, 70))
Santa_on_Sleigh_Image = pygame.image.load('Santa_on_sleigh.png')
santa = pygame.transform.scale(Santa_on_Sleigh_Image, (148, 92))
santaRect = santa.get_rect()

playerRect = playerImage.get_rect()
peachRect=playerImage2.get_rect()
baddieImage = pygame.image.load('gremlin.png')
charbonImage = pygame.image.load('Charbon.png')
lutinImage = pygame.image.load('bonlutin.png')
cadeauImage = pygame.image.load('cadeau.png')
thundercloudImage = pygame.image.load('thundercloud.png')
chimneyImage = pygame.image.load('chimney.png')
hp = pygame.image.load('hp.png')
coeur = pygame.transform.scale(hp, (30, 30))

gameBackground_lvl1 = pygame.image.load("winter_background.png")
gameBackground_lvl2 = pygame.image.load("lvl_2.png")
gameBackground_lvl3 = pygame.image.load("night_sky.png")
gameOverBackground = pygame.image.load("Grinch end game.png")


#todo set up pct score instead of absolute numbers
while True: #level 1

    # Set up the start of the game.
    baddies = []
    lutin = []
    scoreLutin = 0
    lives = 3  # The number of lives at the start of the game
    level = 1  # We start with the first level
    playerRect.topleft = (WINDOWWIDTH / 2, WINDOWHEIGHT - 80)
    moveLeft = moveRight = moveUp = moveDown = False
    reverseCheat = slowCheat = False
    baddieAddCounter = 0  # ajouter de baddies horizontalement
    lutinAddCounter = 0  # ajouter des lutins horizontalement
    pygame.mixer.music.load('Jingle_Bells-Kevin_MacLeod.mp3')
    pygame.mixer.music.play(-1, 0.0)
    while True:  # The game loop runs while the game part is playing.
        for event in pygame.event.get():
            if event.type == QUIT:
                terminate()
            if event.type == KEYDOWN:
                if event.key == K_z:
                    reverseCheat = True
                if event.key == K_x:
                    slowCheat = True
                if event.key == K_LEFT or event.key == K_a:
                    moveRight = False
                    moveLeft = True
                if event.key == K_RIGHT or event.key == K_d:
                    moveLeft = False
                    moveRight = True
                if event.key == K_UP or event.key == K_w:
                    moveDown = False
                    moveUp = True
                if event.key == K_DOWN or event.key == K_s:
                    moveUp = False
                    moveDown = True
                if event.key == K_t:
                    Menu() #pause
                    break
                # option mute pour enlever le son du jeu. Par contre le son du Game Over reste toujours
                if event.key == K_m:
                    if musicPlaying:
                        pygame.mixer.music.stop()
                    else:
                        pygame.mixer.music.play(-1, 0.0)
                musicPlaying = not musicPlaying  # le code a ete adapte depuis le livre de cours (Ai Swegart) Ch. 19 Page 325-326

            if event.type == KEYUP:
                if event.key == K_z:
                    reverseCheat = False
                    scoreLutin = 0
                if event.key == K_x:
                    slowCheat = False
                    scoreLutin = 0
                if event.key == K_ESCAPE:
                    terminate()

                if event.key == K_LEFT or event.key == K_a:
                    moveLeft = False
                if event.key == K_RIGHT or event.key == K_d:
                    moveRight = False
                if event.key == K_UP or event.key == K_w:
                    moveUp = False
                if event.key == K_DOWN or event.key == K_s:
                    moveDown = False
            MouseControls(MOUSEMOTION)
        # Add new baddies at the top of the screen, if needed.
        if not reverseCheat and not slowCheat:
            lutinAddCounter += 1
            baddieAddCounter += 1

        if baddieAddCounter == ADDNEWBADDIERATE:
            baddieAddCounter = 0
            baddieSize = random.randint(MINSIZE, MAXSIZE)
            newBaddie = {
                'rect': pygame.Rect(WINDOWWIDTH + 40 - baddieSize, random.randint(0, WINDOWHEIGHT - baddieSize),
                                    baddieSize,
                                    baddieSize),
                'speed': random.randint(BADDIEMINSPEED, BADDIEMAXSPEED),
                'surface': pygame.transform.scale(baddieImage, (baddieSize, baddieSize)),
            }

            baddies.append(newBaddie)

        if lutinAddCounter == ADDNEWLUTINRATE:
            lutinAddCounter = 0
            lutinSize = random.randint(MINSIZE, MEDSIZE)
            newLutin = {'rect': pygame.Rect(WINDOWWIDTH + 40 - lutinSize, random.randint(0, WINDOWHEIGHT - lutinSize),
                                             lutinSize,
                                             lutinSize),
                         'speed': LUTINSPEED,
                         'surface': pygame.transform.scale(lutinImage, (lutinSize, lutinSize)),
                         }

            lutin.append(newLutin)

        #Move the player around
        PlayerMouvement(playerRect)
        # Move the baddies to the left.
        bad_character_movement(baddies, WINDOWWIDTH)

        # Move the elves to the left.
        good_character_movement(lutin, WINDOWWIDTH)

        # Set up the background
        windowSurface.blit(gameBackground_lvl1, (0, -100))
        # Draw the Lutin score and top score.
        drawText('Elves Caught: %s' % (scoreLutin), font, windowSurface, 10, 0)
        vie(lives)
        drawText('Level: %s' % (level), font, windowSurface, WINDOWWIDTH - 150, 0)

        # Draw the player's rectangle.
        if player[0] == "mario":
            windowSurface.blit(playerImage, playerRect)
        if player[0] == "peach":
            playerRect = peachRect
            windowSurface.blit(playerImage2, peachRect)

        # Draw each baddie.
        for b in baddies:
            windowSurface.blit(b['surface'], b['rect'])

        # Draw each lutin.
        for l in lutin:
            windowSurface.blit(l['surface'], l['rect'])

        pygame.display.update()

        # Check if any of the lutins have been collected by the player.
        if playerHasHitLutin(playerRect, lutin) == True:
            scoreLutin += 1
            BellsSound.play()
            if scoreLutin >= 10:  # the player moves to the next level (for now the game stops)
                break
                #create method for levelling up
            else:
                continue


        # Check if any of the baddies have hit the player.
        if playerHasHitBaddie(playerRect, baddies) == True:
            lives -= 1
            damageSound.play()
            #todo add damage sound for peach
            for b in baddies:
                baddies.remove(b)
            if lives > 0:  # the player keeps playing if she/he has more than 0 lives
                pass
            else:  # when the player has 0 lives the game stops
                break

        mainClock.tick(FPS)

    # Stop the game and show the "Game Over" screen.
    if scoreLutin < 10:
        windowSurface.blit(gameOverBackground, (-850, 0))
        pygame.mixer.music.stop()
        gameOverSound.play()

        drawText('GAME OVER', font, windowSurface, (WINDOWWIDTH / 3), (WINDOWHEIGHT / 3))
        drawText('Press a key to retry', font, windowSurface, (WINDOWWIDTH / 3) - 45, (WINDOWHEIGHT / 3) + 50)
        drawText('to save Christmas', font, windowSurface, (WINDOWWIDTH / 3) - 45, (WINDOWHEIGHT / 3) + 100)
        pygame.display.update()
        waitForPlayerToPressKey()

        gameOverSound.stop()

 #-----------------------------------------------------------------------------------------------------------------------

    elif scoreLutin >= 10:                  #level-up code to lvl 2
        windowSurface.fill(ENDGAMEBACKGROUNDCOLOR)
        pygame.mixer.music.stop()
        YaySound.play()
        drawText("You WON!", font, windowSurface, (WINDOWWIDTH / 3) + 20, (WINDOWHEIGHT / 3))
        drawText("Press any key to start next level", font, windowSurface, (WINDOWWIDTH / 3) - 150,
                 (WINDOWHEIGHT / 3) + 50)
        pygame.display.update()
        waitForPlayerToPressKey()
        YaySound.stop()
        scoreLutin = 0
        while True: #lvl 2 of the game
            level += 1
            #Debug code
            if lives <= 0:  #this code helps to debug the previous problems
                break                  # when a player has less than 0 lives him/her back to the start of the game
            elif level >= 4:  #this code is useful when the player has completed the game, he can restart from lvl 1
                break
            # Set up the start of the game.
            baddies = []
            lutin = []
            scoreCadeau = 0
            playerRect.topleft = (WINDOWWIDTH / 2, WINDOWHEIGHT - 80)
            moveLeft = moveRight = moveUp = moveDown = False
            reverseCheat = slowCheat = False
            baddieAddCounter = 0  # ajouter de baddies horizontalement
            lutinAddCounter = 0  # ajouter des lutins horizontalement
            pygame.mixer.music.load('Jingle_Bell_Rock_(Instrumental).mp3')
            pygame.mixer.music.play(-1, 0.0)
            # level1 = GameLevel(1, "winter_background.png", 'gremlin_baddie.png')
            # level2=GameLevel(2, "night_sky.png", "bonlutin.png")
            while True:  # The game loop runs while the game part is playing.
                for event in pygame.event.get():
                    if event.type == QUIT:
                        terminate()
                    if event.type == KEYDOWN:
                        if event.key == K_z:
                            reverseCheat = True
                        if event.key == K_x:
                            slowCheat = True
                        if event.key == K_LEFT or event.key == K_a:
                            moveRight = False
                            moveLeft = True
                        if event.key == K_RIGHT or event.key == K_d:
                            moveLeft = False
                            moveRight = True
                        if event.key == K_UP or event.key == K_w:
                            moveDown = False
                            moveUp = True
                        if event.key == K_DOWN or event.key == K_s:
                            moveUp = False
                            moveDown = True
                        if event.key == K_t:
                            Menu()  # pause
                            #todo define exit to menu function if player chooses to go back to menu at any point in the game
                            break
                        # option mute pour enlever le son du jeu. Par contre le son du Game Over reste toujours
                        if event.key == K_m:
                            if musicPlaying:
                                pygame.mixer.music.stop()
                            else:
                                pygame.mixer.music.play(-1, 0.0)
                        musicPlaying = not musicPlaying  # le code a ete adapte depuis le livre de cours (Ai Swegart) Ch. 19 Page 325-326

                    if event.type == KEYUP:
                        if event.key == K_z:
                            reverseCheat = False
                            scoreCadeau = 0
                        if event.key == K_x:
                            slowCheat = False
                            scoreCadeau = 0
                        if event.key == K_ESCAPE:
                            terminate()

                        if event.key == K_LEFT or event.key == K_a:
                            moveLeft = False
                        if event.key == K_RIGHT or event.key == K_d:
                            moveRight = False
                        if event.key == K_UP or event.key == K_w:
                            moveUp = False
                        if event.key == K_DOWN or event.key == K_s:
                            moveDown = False

                    MouseControls(MOUSEMOTION)
                # Add new baddies at the top of the screen, if needed.
                if not reverseCheat and not slowCheat:
                    lutinAddCounter += 1
                    baddieAddCounter += 1

                if baddieAddCounter == ADDNEWBADDIERATE:
                    baddieAddCounter = 0
                    baddieSize = random.randint(MEDSIZE, MAXSIZE)
                    newBaddie = {
                        'rect': pygame.Rect(WINDOWWIDTH + 40 - baddieSize, random.randint(0, WINDOWHEIGHT - baddieSize),
                                            baddieSize,
                                            baddieSize),
                        'speed': random.randint(BADDIEMINSPEED, BADDIEMAXSPEED),
                        'surface': pygame.transform.scale(charbonImage, (baddieSize, baddieSize)),
                        }

                    baddies.append(newBaddie)

                if lutinAddCounter == ADDNEWLUTINRATE:
                    lutinAddCounter = 0
                    lutinSize = random.randint(MINSIZE, MEDSIZE)
                    newLutin = {
                        'rect': pygame.Rect(WINDOWWIDTH + 40 - lutinSize, random.randint(0, WINDOWHEIGHT - lutinSize),
                                            lutinSize,
                                            lutinSize),
                        'speed': LUTINSPEED,
                        'surface': pygame.transform.scale(cadeauImage, (lutinSize, lutinSize)),
                        }

                    lutin.append(newLutin)

                # Move the player around.
                PlayerMouvement(playerRect)

                # Move the charcoal to the left.
                bad_character_movement(baddies, WINDOWWIDTH)

                # Move the presents to the left.
                good_character_movement(lutin, WINDOWWIDTH)

                # Set up the background
                windowSurface.blit(gameBackground_lvl2, (0, -100))
                # Draw the Lutin score and top score.
                drawText(''
                         'Presents Caught: %s' % (scoreCadeau), font, windowSurface, 10, 0)
                vie(lives)
                drawText('Level: %s' % (level), font, windowSurface, WINDOWWIDTH - 150, 0)

                # Draw the player's rectangle.
                if player[0] == "mario":
                    windowSurface.blit(playerImage, playerRect)
                if player[0] == "peach":
                    playerRect = peachRect
                    windowSurface.blit(playerImage2, peachRect)

                # Draw each baddie.
                for b in baddies:
                    windowSurface.blit(b['surface'], b['rect'])

                # Draw each lutin.
                for l in lutin:
                    windowSurface.blit(l['surface'], l['rect'])

                pygame.display.update()

                # Check if any of the lutins have been collected by the player.
                if playerHasHitLutin(playerRect, lutin) == True:
                    scoreCadeau += 1
                    PresentSound.play()

                    if scoreCadeau >= 15:  # the player moves to the next level
                        break
                    else:
                        continue

                # Check if any of the baddies have hit the player.
                if playerHasHitBaddie(playerRect, baddies) == True:
                    lives -= 1
                    damageSound.play()
                    for b in baddies:
                        baddies.remove(b)
                    if lives > 0:  # the player keeps playing if she/he has more than 0 lives
                        pass
                    else:  # when the player has 0 lives the game stops
                        break
                        # Stop the game and show the "Game Over" screen.
                mainClock.tick(FPS)

            if scoreCadeau < 15:
                windowSurface.blit(gameOverBackground, (-850, 0))
                pygame.mixer.music.stop()
                gameOverSound.play()

                drawText('GAME OVER', font, windowSurface, (WINDOWWIDTH / 3), (WINDOWHEIGHT / 3))
                drawText('Press a key to retry', font, windowSurface, (WINDOWWIDTH / 3) - 45,
                         (WINDOWHEIGHT / 3) + 50)
                drawText('to save Christmas', font, windowSurface, (WINDOWWIDTH / 3) - 45, (WINDOWHEIGHT / 3) + 100)
                pygame.display.update()
                waitForPlayerToPressKey()

                gameOverSound.stop()

            # -----------------------------------------------------------------------------------------------------------------------
            elif scoreCadeau >= 15:  #level-up code to lvl 3
                santaRect
                windowSurface.fill(ENDGAMEBACKGROUNDCOLOR)
                pygame.mixer.music.stop()
                YaySound.play()
                drawText("You WON!", font, windowSurface, (WINDOWWIDTH / 3) + 20, (WINDOWHEIGHT / 3))
                drawText("Press any key to start next level", font, windowSurface, (WINDOWWIDTH / 3) - 150,
                         (WINDOWHEIGHT / 3) + 50)
                drawText("GAME RULES FOR LEVEL 3:", font, windowSurface, (WINDOWWIDTH / 3) - 250,
                         (WINDOWHEIGHT / 3) + 150)
                drawText("In level 3 use only up and down controls", font, windowSurface, (WINDOWWIDTH / 3) - 250,
                         (WINDOWHEIGHT / 3) + 200)
                drawText("When approaching a chimney", font, windowSurface, (WINDOWWIDTH / 3) - 160,
                         (WINDOWHEIGHT / 3) + 250)
                drawText("to send presents", font, windowSurface, (WINDOWWIDTH / 3) - 120,
                         (WINDOWHEIGHT / 3) + 300)
                drawText("quickly click on SPACE", font, windowSurface, (WINDOWWIDTH / 3) - 140,
                         (WINDOWHEIGHT / 3) + 350)

                pygame.display.update()
                waitForPlayerToPressKey()
                YaySound.stop()
                scoreCadeau=0
                while True:  # lvl 3 of the game
                    level += 1
                    # Debug code
                    if lives <= 0:    # this code helps to debug the previous problems
                        break         # when a player has less than 0 lives him/her back to the start of the game
                    elif level >= 4:  # this code is useful when the player has completed the game, he can restart from lvl 1
                        break         # this code in particular sends the player back to level 2
                    # Set up the start of the game.
                    baddies = []
                    chimneys = []
                    scoreCadeaux_livrés = 0
                    santaRect.topleft = (WINDOWWIDTH/2-200, WINDOWHEIGHT/2)
                    moveLeft = moveRight = moveUp = moveDown = False
                    reverseCheat = slowCheat = False
                    baddieAddCounter = 0  # ajouter de baddies horizontalement
                    chimneyAddCounter = 0 #ajouter les cheminees en bas d'ecran
                    lutinAddCounter = 0  # ajouter des lutins horizontalement
                    pygame.mixer.music.load('Katy Perry-CozyLittleChristmas.mp3')
                    pygame.mixer.music.play(-1, 0.0)
                    while True:  # The game loop runs while the game part is playing.
                        for event in pygame.event.get():
                            if event.type == QUIT:
                                terminate()
                            if event.type == KEYDOWN:
                                if event.key == K_z:
                                    reverseCheat = True
                                if event.key == K_x:
                                    slowCheat = True
                                if event.key == K_UP or event.key == K_w:
                                    moveDown = False
                                    moveUp = True
                                if event.key == K_DOWN or event.key == K_s:
                                    moveUp = False
                                    moveDown = True
                                if event.key == K_t:
                                    Menu()#pause
                                    break
                                # option mute pour enlever le son du jeu. Par contre le son du Game Over reste toujours
                                if event.key == K_m:
                                    if musicPlaying:
                                        pygame.mixer.music.stop()
                                    else:
                                        pygame.mixer.music.play(-1, 0.0)
                                musicPlaying = not musicPlaying  # le code a ete adapte depuis le livre de cours (Ai Swegart) Ch. 19 Page 325-326

                            if event.type == KEYUP:
                                if event.key == K_z:
                                    reverseCheat = False
                                    scoreCadeaux_livrés = 0
                                if event.key == K_x:
                                    slowCheat = False
                                    scoreCadeaux_livrés = 0
                                if event.key == K_ESCAPE:
                                    terminate()

                                if event.key == K_UP or event.key == K_w:
                                    moveUp = False
                                if event.key == K_DOWN or event.key == K_s:
                                    moveDown = False
                            if event.type == MOUSEMOTION:
                                # If the mouse moves, move the player vertically with the cursor.
                                santaRect.centery = event.pos[1]
                        # Add new baddies at the top of the screen, if needed.
                        if not reverseCheat and not slowCheat:
                            baddieAddCounter += 1
                            chimneyAddCounter += 1

                        if baddieAddCounter == 104:
                            baddieAddCounter = 0
                            baddieSize = random.randint(MINSIZE, MAXSIZE)
                            newBaddie = {
                                'rect': pygame.Rect(WINDOWWIDTH + 40 - baddieSize,
                                                    random.randint(0, WINDOWHEIGHT - baddieSize),
                                                    baddieSize,
                                                    baddieSize),
                                'speed': random.randint(BADDIEMINSPEED, BADDIEMAXSPEED),
                                'surface': pygame.transform.scale(thundercloudImage, (baddieSize, baddieSize)),
                            }

                            baddies.append(newBaddie)

                        if chimneyAddCounter == ADDNEWCHIMNEYRATE:
                            chimneyAddCounter = 0
                            chimneySize = random.randint(40, 750)
                            newChimney = {
                                'rect': pygame.Rect(WINDOWWIDTH,
                                                    WINDOWHEIGHT - chimneySize + 8,
                                                    chimneySize,
                                                    chimneySize),
                                'speed': CHIMNEYSPEED,
                                'surface': pygame.transform.scale(chimneyImage, (MEDSIZE, chimneySize)),
                            }

                            chimneys.append(newChimney)

                        # Move the player vertically.
                        PlayerMouvement(santaRect)

                        # Move the baddies to the left.
                        bad_character_movement(baddies, WINDOWWIDTH)

                        # Move the chimneys to the left.
                        good_character_movement(chimneys, WINDOWWIDTH)

                        # Set up the background
                        windowSurface.blit(gameBackground_lvl3, (0, -100))
                        # Draw the score, the number of lives remaining and the level of the game.
                        drawText('Presents delivered: %s' % (scoreCadeaux_livrés), font, windowSurface, 10, 0)
                        vie(lives)
                        drawText('Level: %s' % (level), font, windowSurface, WINDOWWIDTH - 150, 0)

                        # Draw the player's rectangle.
                        windowSurface.blit(santa, santaRect) #santaImage

                        # Draw each baddie.
                        for b in baddies:
                            windowSurface.blit(b['surface'], b['rect'])

                        # Draw each chimney.
                        for c in chimneys:
                            windowSurface.blit(c['surface'], c['rect'])

                        pygame.display.update()

                        # Check if any of the lutins have been collected by the player.
                        if send_Gift(santaRect, chimneys, scoreCadeaux_livrés, PresentDelivered) == True:
                            scoreCadeaux_livrés += 1
                            if scoreCadeaux_livrés >= 15:  # the player moves to the next level
                                break
                            else:
                                continue

                        # Check if any of the baddies have hit the player.
                        if playerHasHitBaddie(santaRect, baddies) == True:
                            lives -= 1
                            damageSound.play()
                            for b in baddies:
                                baddies.remove(b)
                            if lives > 0:  # the player keeps playing if she/he has more than 0 lives
                                pass
                            else:  # when the player has 0 lives the game stops
                                break
                                # Stop the game and show the "Game Over" screen.
                        mainClock.tick(FPS)

                    if scoreCadeaux_livrés < 15:
                        windowSurface.blit(gameOverBackground, (-850, 0))
                        pygame.mixer.music.stop()
                        gameOverSound.play()

                        drawText('GAME OVER', font, windowSurface, (WINDOWWIDTH / 3), (WINDOWHEIGHT / 3))
                        drawText('Press a key to retry', font, windowSurface, (WINDOWWIDTH / 3) - 45,
                                 (WINDOWHEIGHT / 3) + 50)
                        drawText('to save Christmas', font, windowSurface, (WINDOWWIDTH / 3) - 45,
                                 (WINDOWHEIGHT / 3) + 100)
                        pygame.display.update()

                        waitForPlayerToPressKey()
                        gameOverSound.stop()

                    # -----------------------------------------------------------------------------------------------------------------------
                    elif scoreCadeaux_livrés >= 15:  # End of the game
                        windowSurface.fill(ENDGAMEBACKGROUNDCOLOR)
                        pygame.mixer.music.stop()
                        YaySound.play()
                        drawText("Well Done!", font, windowSurface, (WINDOWWIDTH / 3) + 30, (WINDOWHEIGHT / 3))
                        drawText("You have finished the game!", font, windowSurface, (WINDOWWIDTH / 3) -120,
                                 (WINDOWHEIGHT / 3) + 50)
                        drawText("To restart press any key!", font, windowSurface, (WINDOWWIDTH / 3) -120,
                                 (WINDOWHEIGHT / 3) + 100)
                        pygame.display.update()
                        waitForPlayerToPressKey()
                        YaySound.stop()
                        Menu()
                        break
