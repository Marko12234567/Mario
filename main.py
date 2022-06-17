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

down = [pygame.image.load(os.path.join("step1.png"))]

gumba_left = [pygame.image.load("gumba.png"),
              pygame.image.load("gumba2.png")]

bawser_left1 = "bawser_left.jpg"
bawser_left2 = "bawser_left2.jpg"
bawser_right1 = "bawser_right.jpg"
bawser_right2 = "bawser_right2.jpg"

fireball_img = "fireball.png"

lifes = 3

enemies = pygame.sprite.Group()

class GameSprite(pygame.sprite.Sprite):
    def __init__(self, player_image, player_speed, player_x, player_y, size_x, size_y):
        super().__init__()
        self.size_x, self.size_y = size_x, size_y
        self.image = pygame.transform.scale(
            player_image, (self.size_x, self.size_y))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
        self.stepIndex = 0
        self.vel_y = 0
        self.time_out_animatio = 15


class Enemy(GameSprite):
    def update(self):
        self.rect.x -= self.speed
        self.vel_y += 1
        if self.stepIndex >= 2:
            self.stepIndex = 0
        if True:
            self.image = pygame.transform.scale(
                gumba_left[self.stepIndex], (self.size_x, self.size_y))
            self.time_out_animatio -= 1
            if self.time_out_animatio == 0:
                self.time_out_animatio = 30
                self.stepIndex += 1
        if self.vel_y >= 10:
            self.vel_y = 10
        self.rect.y += self.vel_y
        global step
        for tile in world.tile_list:
            if tile[1].colliderect(self.rect.x, self.rect.y, self.size_x, self.size_y):
                if self.vel_y < 0:
                    self.rect.y -= tile[1].bottom - self.rect.top
                    self.vel_y = 0
                if self.vel_y >= 0:
                    self.rect.y += tile[1].top - self.rect.bottom
                    self.vel_y = 0


class Fireball(GameSprite):
    def update(self):
        self.rect.x += self.speed
        if self.rect.x > win_width:
            self.kill()


fireballs = pygame.sprite.Group()


class Player1(GameSprite):
    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE] and self.jump == False:
            self.vel_y = -20
            self.jump = True
        if not keys[pygame.K_SPACE]:
            self.jump = False
        self.vel_y += 1
        if self.vel_y >= 10:
            self.vel_y = 10
        self.rect.y += self.vel_y
        global step
        for tile in world.tile_list:
            if tile[1].colliderect(self.rect.x, self.rect.y, self.size_x, self.size_y):
                #if self.vel_y < 0:
                    #self.rect.y -= tile[1].bottom - self.rect.top
                    #self.vel_y = 0
                if self.vel_y >= 0:
                    self.rect.y += tile[1].top - self.rect.bottom
                    self.vel_y = 0
    def reset(self):
        if self.stepIndex >= 3:
            self.stepIndex = 0
        if move_left:
            window.blit(pygame.transform.scale(
                left[self.stepIndex], (self.size_x, self.size_y)), (self.rect.x, self.rect.y))
            self.time_out_animatio -= 1
            if self.time_out_animatio == 0:
                self.time_out_animatio = 8
                self.stepIndex += 1
        elif move_right:
            window.blit(pygame.transform.scale(
                right[self.stepIndex], (self.size_x, self.size_y)), (self.rect.x, self.rect.y))
            self.time_out_animatio -= 1
            if self.time_out_animatio == 0:
                self.time_out_animatio = 8
                self.stepIndex += 1
        else:
            window.blit(stationary, (self.rect.x, self.rect.y))
    # def fire(self):
        #fireball = Fireball(fireball_img, self.rect.x, self.rect.y, 15, 15, 20)
        # fireballs.add(fireball)
tile_size = 50
# 1-земля
# 2-блок
# 3-знак питання
# 4-труба
# 44-труба
#45-труба
#46-труба
#5-зелена земля
#6-зелений блок
#7-зелена цегла
#8-цегла
# 9-серце

tile_list = pygame.sprite.Group

class World(pygame.sprite.Sprite):
    def __init__(self,data):
        super().__init__()
        self.tile_list = []
        broken_img = pygame.image.load("broken.png")
        whole_img = pygame.image.load("whole.png")
        question_img = pygame.image.load("question.png")
        broken_green_img = pygame.image.load("brocken_green.png")
        whole_green_img = pygame.image.load("whole_green.png")
        brick_green_img = pygame.image.load("brick_green.png")
        tube1_img = pygame.image.load("tube2 (1).png")
        tube2_img = pygame.image.load("tube2 (2).png")
        tube3_img = pygame.image.load("tube2 (3).png")
        tube4_img = pygame.image.load("tube2 (4).png")
        castle3_img = pygame.image.load("castle (3).png")
        castle4_img = pygame.image.load("castle (4).png")
        castle5_img = pygame.image.load("castle (5).png")
        castle6_img = pygame.image.load("castle (6).png")
        brick_img = pygame.image.load("brick.png")
        row_count = 0
        for row in data:
            col_count = 0
            for tile in row:
                if tile == 1:
                    img = pygame.transform.scale(broken_img, (tile_size, tile_size))
                    img_rect = img.get_rect()
                    img_rect.x = col_count * tile_size
                    img_rect.y = row_count * tile_size
                    tile = (img, img_rect)
                    self.tile_list.append(tile)
                if tile == 2:
                    img = pygame.transform.scale(whole_img, (tile_size, tile_size))
                    img_rect = img.get_rect()
                    img_rect.x = col_count * tile_size
                    img_rect.y = row_count * tile_size
                    tile = (img, img_rect)
                    self.tile_list.append(tile)
                if tile == 3:
                    img = pygame.transform.scale(question_img, (tile_size, tile_size))
                    img_rect = img.get_rect()
                    img_rect.x = col_count * tile_size
                    img_rect.y = row_count * tile_size
                    tile = (img, img_rect)
                    self.tile_list.append(tile)
                if tile == 5:
                    img = pygame.transform.scale(broken_green_img, (tile_size, tile_size))
                    img_rect = img.get_rect()
                    img_rect.x = col_count * tile_size
                    img_rect.y = row_count * tile_size
                    tile = (img, img_rect)
                    self.tile_list.append(tile)
                if tile == 6:
                    img = pygame.transform.scale(whole_green_img, (tile_size, tile_size))
                    img_rect = img.get_rect()
                    img_rect.x = col_count * tile_size
                    img_rect.y = row_count * tile_size
                    tile = (img, img_rect)
                    self.tile_list.append(tile)
                if tile == 7:
                    img = pygame.transform.scale(brick_green_img, (tile_size, tile_size))
                    img_rect = img.get_rect()
                    img_rect.x = col_count * tile_size
                    img_rect.y = row_count * tile_size
                    tile = (img, img_rect)
                    self.tile_list.append(tile)
                if tile == 44:
                    img = pygame.transform.scale(tube1_img, (tile_size, tile_size))
                    img_rect = img.get_rect()
                    img_rect.x = col_count * tile_size
                    img_rect.y = row_count * tile_size
                    tile = (img, img_rect)
                    self.tile_list.append(tile)
                if tile == 45:
                    img = pygame.transform.scale(tube2_img, (tile_size, tile_size))
                    img_rect = img.get_rect()
                    img_rect.x = col_count * tile_size
                    img_rect.y = row_count * tile_size
                    tile = (img, img_rect)
                    self.tile_list.append(tile)
                if tile == 46:
                    img = pygame.transform.scale(tube3_img, (tile_size, tile_size))
                    img_rect = img.get_rect()
                    img_rect.x = col_count * tile_size
                    img_rect.y = row_count * tile_size
                    tile = (img, img_rect)
                    self.tile_list.append(tile)
                if tile == 4:
                    img = pygame.transform.scale(tube4_img, (tile_size, tile_size))
                    img_rect = img.get_rect()
                    img_rect.x = col_count * tile_size
                    img_rect.y = row_count * tile_size
                    tile = (img, img_rect)
                    self.tile_list.append(tile)
                if tile == 55:
                    img = pygame.transform.scale(castle3_img, (tile_size, tile_size))
                    img_rect = img.get_rect()
                    img_rect.x = col_count * tile_size
                    img_rect.y = row_count * tile_size
                    tile = (img, img_rect)
                    self.tile_list.append(tile)
                if tile == 56:
                    img = pygame.transform.scale(castle4_img, (tile_size, tile_size))
                    img_rect = img.get_rect()
                    img_rect.x = col_count * tile_size
                    img_rect.y = row_count * tile_size
                    tile = (img, img_rect)
                    self.tile_list.append(tile)
                if tile == 57:
                    img = pygame.transform.scale(castle5_img, (tile_size, tile_size))
                    img_rect = img.get_rect()
                    img_rect.x = col_count * tile_size
                    img_rect.y = row_count * tile_size
                    tile = (img, img_rect)
                    self.tile_list.append(tile)
                if tile == 58:
                    img = pygame.transform.scale(castle6_img, (tile_size, tile_size))
                    img_rect = img.get_rect()
                    img_rect.x = col_count * tile_size
                    img_rect.y = row_count * tile_size
                    tile = (img, img_rect)
                    self.tile_list.append(tile)
                if tile == 8:
                    img = pygame.transform.scale(brick_img, (tile_size, tile_size))
                    img_rect = img.get_rect()
                    img_rect.x = col_count * tile_size
                    img_rect.y = row_count * tile_size
                    tile = (img, img_rect)
                    self.tile_list.append(tile)
                col_count += 1
            row_count += 1
    def draw(self):
        for tile in self.tile_list:
            window.blit(tile[0], tile[1])


map = [
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2,2,2,2,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,2,2,2,2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,3,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2,2,2,2,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,2,2,2,2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2,2,2,2,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,2,2,2,2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2,2,2,2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2,2,2,2,7,7,7,7,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,7,7,7,0,0,0,7,7,7,7,7,0,0,0,0,6,6,6,6,6,0,0,0,0,0,0,0,7,7,7,7,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,7,7,7,7,2,2,2,2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2,2,2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2,2,2,2,7,7,7,7,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,7,7,7,0,0,0,7,7,7,7,7,0,0,0,0,6,6,6,6,6,0,0,0,0,0,0,0,7,7,7,7,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,7,7,7,7,2,2,2,2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2,2,2,2,7,7,7,7,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,7,7,7,7,0,0,0,0,0,0,3,3,3,3,7,0,0,0,0,6,6,6,6,6,0,0,0,7,7,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,7,7,7,7,2,2,2,2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2,2,2,2,2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2,2,2,2,7,7,7,7,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,7,7,7,7,0,0,0,0,0,0,0,0,0,0,7,0,0,0,0,0,6,0,0,0,0,0,0,7,7,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,7,7,7,7,2,2,2,2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2,2,2,2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2,2,2,2,7,7,7,7,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,7,0,0,0,0,0,0,0,7,0,0,7,7,7,7,0,0,0,0,0,0,0,0,0,0,7,0,0,0,0,0,6,0,0,0,0,0,0,7,7,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,7,7,7,7,2,2,2,2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,9,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2,0,0,0,2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,44,45,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2,2,2,2,7,7,7,7,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,6,0,6,0,0,0,7,0,0,0,0,0,0,0,7,0,7,7,7,7,7,0,7,0,0,0,0,0,0,7,7,7,0,0,7,7,7,7,7,7,0,0,0,0,0,6,0,0,6,0,0,0,7,7,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,6,6,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,7,7,7,7,2,2,2,2,0,0,0,0,0,0,56,56,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,2,2,0,0,0,2,3,2,3,2,0,0,0,0,0,0,0,0,0,0,0,0,2,2,0,0,0,2,2,0,0,0,0,0,0,0,0,0,0,0,44,45,0,0,0,46,4,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2,2,0,0,0,2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,3,3,3,3,3,0,0,0,0,0,0,6,0,6,0,6,0,6,0,0,0,6,0,0,0,0,0,7,7,7,0,0,0,7,7,7,0,0,0,0,0,0,7,7,7,0,0,0,0,0,0,0,0,0,0,0,0,0,6,6,6,6,0,0,0,7,7,0,0,7,7,7,7,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,6,6,6,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,7,7,7,7,2,2,2,2,0,0,0,0,0,0,55,55,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2,2,2,0,0,0,2,2,2,0,0,0,0,0,0,44,45,0,0,46,4,0,0,0,46,4,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2,2,2,0,0,0,0,0,0,2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,2,2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,6,0,6,0,6,0,6,0,6,0,0,0,6,0,6,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,7,7,0,0,0,0,0,0,6,6,6,6,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,8,8,58,8,8,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2,2,2,2,0,0,0,2,2,2,2,0,0,0,0,0,46,4,0,0,46,4,0,0,0,46,4,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2,2,2,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,2,2,2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,6,0,6,0,6,0,6,0,6,0,6,0,0,0,6,0,6,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,7,7,0,0,0,0,0,6,6,6,6,6,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,8,8,57,8,8,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,2,2,2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,0,0,5,5,0,0,5,5,5,5,5,5,5,5,0,0,0,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
    [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,0,0,5,5,0,0,5,5,5,5,5,5,5,5,0,0,0,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]]


world = World(map)


# pygame.mixer.init()
# pygame.mixer.music.load("Mariogg.ogg")
# pygame.mixer.music.play()
#fireball_sound = mixer.Sound("fireballogg.ogg")


back = (130, 146, 255)
win_width, win_height = 1400, 700
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

#    U    D      L      R
player1 = Player1(stationary, 5, 300, 400, 65, 75)
gumba = Enemy(gumba_left[0], 2, win_width - 80, 100, 65, 65)
width = 2000
height = 700
bg = pygame.image.load("bg1.png")
bg = pygame.transform.scale(bg, (width, height))
game = True
gravity = 5
zero_point = 0
spavn_points = [500, 550, 1000, 1500, 2000, 2500, 2600, 2680, 3200, 5000, 4000, 3500, 6850, 7000, 7200, 7500, 7700, 8000]
pygame.font.init()
font1 = pygame.font.SysFont("Arial", 215)
text = font1.render("YOU WIN",1, (212,241,0))
text2 = font1.render("GAME OVER",1, (250,0,0))
while game:
    window.blit(bg, (i, 0))
    window.blit(bg, (i+width, 0))
    window.blit(bg, (i-width, 0))
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
    if userInput[pygame.K_LEFT]:
        move_left = True
        move_right = False
        for enemy in enemies:
            enemy.rect.x += step
        i += step
        zero_point -= step
        for tile_index in range(len(world.tile_list)):
            world.tile_list[tile_index][1][0] += step
    elif userInput[pygame.K_RIGHT]:
        move_right = True
        move_left = False
        i -= step
        for enemy in enemies:
            enemy.rect.x -= step
        zero_point += step
        for tile_index in range(len(world.tile_list)):
            world.tile_list[tile_index][1][0] -= step
    else:
        move_right = False
        move_left = False
        stepIndex = 0
    for x_coor in spavn_points:
        if zero_point - 2 <= x_coor and zero_point + 2 >= x_coor:
            gumba_a = Enemy(gumba_left[0], 2, win_width + 100, 300, 65, 65)
            enemies.add(gumba_a)

    for enemy in enemies:
        if pygame.sprite.collide_rect(player1, enemy):
            if player1.rect.bottom - enemy.rect.top <= 50:
                enemies.remove(enemy)
            if player1.rect.left - enemy.rect.right <= 50 or player1.rect.right - enemy.rect.left <= 50:
                player1.kill()
                window.fill((0, 0, 0), (0, 0, win_width, win_height))
                window.blit(text2, (250, 250))
                pygame.display.update()
                pygame.time.delay(5000)
                game = False
            
 

    for tile in world.tile_list:
        if tile[1].colliderect(player1):
            if abs(player1.rect.top - tile[1].bottom) <= 20:
                world.tile_list.remove(tile)
            if zero_point >= 12950:
                if abs(player1.rect.right - tile[1].left) <= 20:
                    window.fill((0, 0, 0), (0, 0, win_width, win_height))
                    window.blit(text, (250, 250))
                    pygame.display.update()
                    pygame.time.delay(5000)
                    game = False

            

    world.draw()
    player1.update()
    player1.reset()
    enemies.update()
    enemies.draw(window)

    pygame.display.update()
    clock.tick(FPS)