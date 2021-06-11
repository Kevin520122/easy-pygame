import pygame
import os
import player
import enemy
import projectile

#Init game
pygame.init()

#Set the game window
game_win = pygame.display.set_mode((500, 480))
pygame.display.set_caption("First game")

#Load background picture
bg = pygame.image.load(os.path.join('Game_Characters', 'bg.jpg'))
stay = pygame.image.load(os.path.join('Game_Characters', 'standing.png'))

#Set time
clock = pygame.time.Clock()

#Set scroe
score = 0

#Sound Effect
bullet_sound = pygame.mixer.Sound(os.path.join('Game_Characters',"bullet.mp3"))
hit_sound = pygame.mixer.Sound(os.path.join('Game_Characters',"hit.mp3"))
#Play background music continuedly
background_music = pygame.mixer.music.load(os.path.join('Game_Characters',"music.mp3"))
pygame.mixer.music.play(-1)



def redraw_game_window():
    #Load the background
    game_win.blit(bg, (0,0))
    #Display the prompt
    text = font.render("Score: " + str(score), 1, (0, 0, 0))
    game_win.blit(text, (350, 10))
    #Draw the player
    man.draw(game_win)
    #Draw the enemy
    goblin.draw(game_win)
    for bullet in bullets:
        bullet.draw(game_win)
    #After changing GUI in the game, need call update function
    pygame.display.update()




#(name, size, bold, Italic)
font = pygame.font.SysFont('comicsans', 30, True, True)
man = player.player(200, 410, 64, 64)
goblin = enemy.enemy(100, 410, 64, 64, 450)
shootLoop = 0
bullets = []
run = True

#Game Loop
while run:
    clock.tick(27)
    #The situation player collides with the goblin
    if goblin.visible == True:
        if man.hitbox[1]  < goblin.hitbox[1] + goblin.hitbox[3] and man.hitbox[1] + man.hitbox[3] > goblin.hitbox[1]:
            if man.hitbox[0] + man.hitbox[2] > goblin.hitbox[0] and man.hitbox[0] < goblin.hitbox[0] + goblin.hitbox[2]:
                #If bullet in the hitbox range
                #Hit succeed!
                man.hit(game_win)
                score -= 5
            
    if shootLoop > 0:
        shootLoop += 1
    if shootLoop > 3:
        shootLoop = 0
    
    #Quit section
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    #Projectile section
    for bullet in bullets:
        if goblin.visible == True:
            #If bullet hits the enemy
            if bullet.y - bullet.radius < goblin.hitbox[1] + goblin.hitbox[3] and bullet.y + bullet.radius > goblin.hitbox[1]:
                if bullet.x + bullet.radius > goblin.hitbox[0] and bullet.x - bullet.radius < goblin.hitbox[0] + goblin.hitbox[2]:
                    #If bullet in the hitbox range
                    #Hit succeed!
                    hit_sound.play()
                    goblin.hit()
                    score += 1
                    #Remove current bullet
                    bullets.pop(bullets.index(bullet))


        #If bullet is moving in the range
        if bullet.x > 0 and bullet.x < 500:
            bullet.x += bullet.velocity
        else:
            bullets.pop(bullets.index(bullet))

    #Refers to the keys in keyboard
    keys = pygame.key.get_pressed()

    if keys[pygame.K_SPACE] and shootLoop == 0:
        #Play the bullet sound effect
        bullet_sound.play()
        if man.isRight:
            facing = 1
        else:
            facing = -1
        #The play own 5 bullets at most
        if len(bullets) < 5:
            bullets.append(projectile.projectile(round(man.x + man.width // 2), round(man.y + man.height // 2), 6, (0, 0 , 0), facing))
    
        shootLoop = 1
    
    if keys[pygame.K_LEFT] and man.x > man.velocity:
        man.x -= man.velocity
        man.isLeft = True
        man.isRight = False
        man.standing = False

    elif keys[pygame.K_RIGHT] and man.x < 800 - man.width - man.velocity:
        man.x += man.velocity
        man.isRight = True
        man.isLeft = False
        man.standing = False


    else:
        man.standing = True
        man.walkCount = 0


    if not(man.isJump):
        if keys[pygame.K_UP]:
            man.isJump = True
           
            man.walkCount = 0

    else:
        if man.jumpCount >= -10:
            #Going up
            neg = 1
            #Falling down
            if man.jumpCount < 0:
                neg = -1

           
            man.y -= (man.jumpCount ** 2) * 0.5*neg
            man.jumpCount -= 1
        else:
            man.isJump = False
            man.jumpCount = 10
    #Every iteration, redraw game window
    redraw_game_window()

pygame.quit()



