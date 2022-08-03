import random
import sys
import time
import pygame
from audio.media import MediaPlayer


pygame.init()
md = MediaPlayer('audio/sound/yummy.ogg')


dis_width = 600
dis_height = 400
dis = pygame.display.set_mode((dis_width,dis_height))
pygame.display.update()
pygame.display.set_caption("Snake Xenzia")
game_over = False
BLUE = (0,0,255)
RED = (255,0,0)
WHITE = (255,255,255)
BLACK = (0,0,0)
SNAKE_SPEED = 10
SNAKE_BLOCK = 10

x1=dis_width/2
y1=dis_height/2

x1_change = 0
y1_change = 0


font_style = pygame.font.SysFont(None,25)
score_style = pygame.font.SysFont('comicsansms',35)

def our_snake(SNAKE_BLOCK,SNAKE_LIST:list):
    for x in SNAKE_LIST:
        pygame.draw.rect(dis,BLACK,[x[0],x[1],SNAKE_BLOCK,SNAKE_BLOCK])
def alert(msg,color):
    msg = font_style.render(msg,True,color)
    dis.blit(msg,[dis_width/2,dis_height/2])

clock = pygame.time.Clock()


def main_loop():
    global game_over
    global x1
    global x1_change
    global y1
    global y1_change
    game_close = False
    SNAKE_LIST = []
    length_of_snake = 1
    foodx = round(random.randrange(0,dis_width - SNAKE_BLOCK)/10.0)
    foody = round(random.randrange(0,dis_width - SNAKE_BLOCK)/10.0)

    while not game_over:
        while game_close == True:
            dis.fill(BLUE)
            alert('You lost! Press C to play again or Q to Quit',RED)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        main_loop()
        for event in pygame.event.get():
            # print(event)
            if event.type == pygame.QUIT:
                game_over = True
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_change = -SNAKE_BLOCK
                    y1_change = 0
                elif event.key == pygame.K_RIGHT:
                    x1_change = SNAKE_BLOCK
                    y1_change = 0
                elif event.key == pygame.K_UP:
                    y1_change = -SNAKE_BLOCK
                    x1_change = 0
                elif event.key == pygame.K_DOWN:
                    y1_change = SNAKE_BLOCK
                    x1_change = 0

        if x1 >= dis_width or x1 < 0 or y1 >= dis_height or y1 < 0:
            game_close = True


        x1 += x1_change
        y1 += y1_change
        dis.fill(WHITE)
        pygame.draw.rect(dis,BLUE,[foodx,foody,SNAKE_BLOCK,SNAKE_BLOCK])
        pygame.draw.rect(dis,BLACK,[x1,y1,SNAKE_BLOCK,SNAKE_BLOCK])

        pygame.display.update()

        if x1 == foodx and y1 == foody:
            print("yummy!!!")
        

        
        # pygame.draw.rect(dis,BLUE,[200,150,10,10])
        pygame.display.update()
        clock.tick(SNAKE_SPEED)

main_loop()
