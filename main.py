import pygame
import sys
from settings import *
from player import Player
from obs import Obstacle
from text_obj import Text_Obj
from bg import Background
from start import Start

# создание объектов и групп
pygame.init()
screen = pygame.display.set_mode((SC_WIDTH, SC_HEIGHT))
clock = pygame.time.Clock()
#группы
all_sprites = pygame.sprite.Group()
items = pygame.sprite.Group()

#объекты
player = Player(PLAYER_X, PLAYER_Y,"player.png")
all_sprites.add(player)

for i in range(5):
    obs = Obstacle("ham.png", True)
    all_sprites.add(obs)
    items.add(obs)

for i in range(2):
    obs = Obstacle("paper.png", False)
    all_sprites.add(obs)
    items.add(obs)

game_over_bg = Background("game_over.png")

# переменные
score = 0
hp = 1000
score_text = Text_Obj(10, 10, str(score), screen)


run = True

start_screen = Start("start_image.png")
running = False

while not running:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                running = True
 
# главный цикл
while run:
    # задержка
    clock.tick(FPS)
    # цикл обработки событий
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
            
    # изменение объектов, update
    all_sprites.update()
    score_text.update(score)
    hp -= 1
    if hp <= 0:
        run = False
 
    #пересечение объектов, collisions
    hits = pygame.sprite.spritecollide(player, items, True)
    for hit in hits:
        if hit.get_edible() == True:
            score += 10
            obs = Obstacle("ham.png", True)
            all_sprites.add(obs)
            items.add(obs)
            
    # обновление экрана
    screen.fill(BLACK)
    all_sprites.draw(screen)
    score_text.draw()
    pygame.display.update()

while True:
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.fill(BLACK)
    game_over_bg.draw(screen)
    pygame.display.update()


    
