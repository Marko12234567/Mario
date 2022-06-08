import pygame
import os
pygame.init()

stepIndex = 0

stationary = pygame.image.load(os.path.join("stand.png"))
left = [pygame.image.load(os.path.join("step1.png")),
        pygame.image.load(os.path.join("step2.png")),
        pygame.image.load(os.path.join("step3.png"))]

right = [pygame.image.load(os.path.join("step_right1.png")),
        pygame.image.load(os.path.join("step_right2.png")),
        pygame.image.load(os.path.join("step_right3.png"))]

gumba1 = "gumba.png"
gumba2 = "gumba2.png"

bawser_left1 = "bawser_left.jpg"
bawser_left2 = "bawser_left2.jpg"
bawser_right1 = "bawser_right.jpg"
bawser_right2 = "bawser_right2.jpg"

fireball_img = "fireball.png"

lifes = 3
bg = "island_1.png"
width = 1200
height = 700


class GameSprite(pygame.sprite.Sprite):
    def init(self, player_image, player_x, player_y, player_speed, size_x, size_y):
        super().init()
        self.image = pygame.transform.scale(pygame.image.load(player_image), (size_x, size_y))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Enemy(GameSprite):
    direction = "left"
    def update(self):
        if self.rect.x <=470:
            self.direction = "right"
        if self.rect.x > win_width - 85:
            self.direction = "left"
        
        if self.direction == "left":
            self.rect.x -= self.speed
        else:
            self.rect.x += self.speed


class Fireball(GameSprite):
    def update(self):
        self.rect.x += self.speed
        if self.rect.x > win_width:
            self.kill()

fireballs = pygame.sprite.Group()

class Player(GameSprite):
    def update(self):
        global  stepIndex
        if stepIndex >= 3:
            stepIndex = 0
        if move_left:
            window.blit(left[stepIndex], (self.rect.x, self.rect.y))
            stepIndex +=1
        elif move_right:
            print(stepIndex)
            window.blit(right[stepIndex], (self.rect.x, self.rect.y))
            stepIndex +=1
        else:
            window.blit(stationary, (self.rect.x, self.rect.y))
    #def fire(self):
        #fireball = Fireball(fireball_img, self.rect.x, self.rect.y, 15, 15, 20)
        #fireballs.add(fireball)


#pygame.mixer.init()
#pygame.mixer.music.load("Mariogg.ogg")
#pygame.mixer.music.play()
#fireball_sound = mixer.Sound("fireballogg.ogg")


back = (130,146,255)
win_width, win_height = 1400,700
window = pygame.display.set_mode((win_width, win_height))
pygame.display.set_caption("Mario")
icon = pygame.image.load("stand.png")
pygame.display.set_icon(icon)
window.fill(back)
run = True
clock = pygame.time.Clock()
FPS = 60
finish = False
step = 10
radius = 15
jump = False
vel_y = 15
i = 0
move_left = False
move_right = False


player = Player(stationary, 5, win_height - 300, 4, 65, 65)
gumba = Enemy("gumba.png", win_width - 80, 100, 2, 65, 65)


while game:

    window.blit(bg, (i, 0))
    window.blit(bg, (i+width,0))
    window.blit(bg, (i - width, 0))
    if i == -width:
        window.blit(bg, (i, 0))
        i = 0
    if i == width:
        window.blit(bg, (i, 0))
        i = 0

    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            game = False

    userInput = pygame.key.get_pressed()
    if userInput[pygame.K_LEFT] and x > 15:
        move_left = True
        move_right = False
        i += step*2
    elif userInput[pygame.K_RIGHT] and x < width-15:
        move_right = True
        move_left = False
        i -= step*2
    else:
        move_right = False
        move_left = False
        stepIndex = 0

    if jump is False and userInput[pygame.K_SPACE]:
        jump = True

    if jump is True:
        player.rect.y -= vel_y
        vel_y -= 1
        move_right = False
        move_left = False
        if vel_y < -15:
            jump = False
            vel_y = 15
        if pygame.sprite.collidegroup(player, floors, False):
            jump = False
            vel_y = 15
            
    if not sprite.collidegroup(player, floors, False) and not jump:
        falling_down = True
    else:
        falling_down = False
    if falling_down ==True:
        y += 15


        pygame.display.update()
        clock.tick(FPS)