#                    IMPORTING LIBRARIES
import pygame
from pygame.locals import *
import random
import pygame,math
import random
import time

#                    INITIALIZING PYGAME MODULES
pygame.init()


#                    DECLARING TEXT SIZES

SMALLTEXT = pygame.font.Font('freesansbold.ttf', 20)
LARGETEXT = pygame.font.Font('freesansbold.ttf', 40)
EXTRALARGETEXT=pygame.font.Font('freesansbold.ttf', 55)

#                   COLORS CONSTANTS

BLACK=(0, 0, 0)
YELLOW=(0, 0, 255)
RED = (200, 0, 0)
GREEN = (0, 200, 0)
WHITE=(255, 255, 255)
BRIGHT_RED = (255, 0, 0)
BRIGHT_GREEN = (0, 255, 0)

#                   screen SIZE CONSTANTS

window_width = 800
window_height = 600
SIZE = (window_width, window_height)
screen = pygame.display.set_mode(SIZE, RESIZABLE)                            # screen refrence is stored in screen
IMG = pygame.image.load('123f.jpg').convert()                               # converted image of snake and ladder is stored in IMG

#                   DICE IMAGES
diceimg = {
    1: pygame.image.load('1f.png'),
    2: pygame.image.load('2f.png'),
    3: pygame.image.load('3f.png'),
    4: pygame.image.load('4f.png'),
    5: pygame.image.load('5f.png'),
    6: pygame.image.load('6f.png'),
}

#                   COIN IMAGES

coinimg = {
    1: pygame.image.load('green.png'),
    2: pygame.image.load('red.png'),
    3: pygame.image.load('yellow.jpg')
}


#                    BOARD  IN ARRAY
"""      0   1   2  3   4   5  6  7  8    9  10  """
board = (0, 381, 0, 0, 141, 0, 0, 0, 0, 311, 151,  # 0 - 10
            0, 0, 0, 0, 0, 0, 71, 0, 0, 0,  # 10 - 20
            421, 0, 0, 0, 0, 0, 0, 841, 0, 0,  # 20 - 30
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0,  # 30 - 40
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0,  # 40 - 50
            671, 0, 0, 391, 0, 0, 0, 0, 0, 0,  # 50 - 60
            0, 191, 0, 601, 0, 0, 0, 0, 0, 0,  # 60 - 70
            911, 0, 0, 0, 0, 0, 0, 0, 0, 1001,  # 70 - 80
            0, 0, 0, 0, 0, 0, 241, 0, 0, 0,  # 80 - 90
            0, 0, 731, 0, 751, 0, 0, 791, 0, 0,)  # 90 - 100

#                       USEFUL LISTS
SIZE = 3
flag = 0
pos = [0, 0, 0, 0, 0]
player = [0, 0, 0, 0, 0]
x = [0, 0, 0, 0, 0]
y = [0, 0, 0, 0, 0]

#                   FUNCTION TO PRINT ON BOARD


#def restart():


#                   FUNCTION TO PRINT TEXT ON TO screen


def text_print(text, font, color, B_COLOR , rect):
    pygame.draw.rect(screen, B_COLOR, rect)
    text = font.render(text, True, color)
    text_rect = text.get_rect()
    text_rect.center = (rect[0]+(rect[2]/2), rect[1]+(rect[3]/2))
    screen.blit(text, text_rect)

#                   FUNCTION TO RETURN XY CO-ORDINATES


def xy(i):
        x = 100-i
        y = x // 10
        if y % 2 == 1:
            x = 9-(x % 10)
        else:
            x = x % 10
        return x, y

#                   TO MOVE COIN FOR EACH PLAYER


def move_coin():
    count = 1
    screen.blit(IMG, (0, 0))
    for i in range(1, DUP_SIZE+1):
        for j in range(pos[i], player[i]+1):
            x[i], y[i] = xy(j)
            if count != 1:
                screen.blit(coinimg[2].convert(), (x[2] * 60 + 5 + 20, y[2] * 60 + 15))
            count += 1
            for k in range(1, i+1):
                coinpic = coinimg[k].convert()
                screen.blit(coinpic, (x[k]*60+5+k*10, y[k]*60+15))                               # TO DISPLAY ALL COINS
            pygame.display.flip()
            pygame.display.update()
            time.sleep(0.2)
            if j != player[i]:
                screen.blit(IMG, (0, 0))
            pos[i] = player[i]

#                    JUMPING OF COIN IN CASE OF LADDERS AND SNAKES


#def jmp_coin():
#   screen.blit(IMG, (0, 0))





    #                   DEFINING GAME PROCEDURE FOR EACH PLAYER


def player_play(num):
    time.sleep(1)
    sum1 = pos[num]
    text = "player" + str(num) + " got :"
    text_print(text, SMALLTEXT, WHITE, BLACK, (650, 100, 150, 75))
    sum = dice()
    dicepic = diceimg[sum].convert()
    screen.blit(dicepic, (665, 250))
    pygame.display.flip()
    pygame.display.update()
    print('player', num, 'turn')
    print("dice is ", sum)
    print("position is", sum1)
    if sum1 + sum <= 100:
        sum1 += sum
        player[num] = sum1
        move_coin()
    x, sum1 = x, player[num] = ladder_snake(sum1)
    if x == 1:
        move_coin()
    return sum, sum1

#                FUNCTION FOR DICE


def dice():
    from secrets import randbelow
    i = randbelow(6)
    i += 1
    return i

#                FUNCTION TO CLIMB LADDER OR DROP BY SNAKE


def ladder_snake(pos):
    if board[pos] % 10:
        pos = board[pos] // 10
        return 1,pos
    return 0,pos
#                   FUNCTION FOR DISPLAYING SNAKE AND LADDER BOARD


def game_intro():
    while True:
        screen.fill(WHITE)
        text_print("SNAKE AND LADDER", EXTRALARGETEXT, BLACK, WHITE,[window_width/2, window_height/2, 0, 0])
        text_print("GO!", SMALLTEXT, BLACK, GREEN, [150, 450, 100, 50])
        text_print("QUIT", SMALLTEXT, BLACK, RED, [550, 450, 100, 50])
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse = pygame.mouse.get_pos()
                if 250 > mouse[0] > 150 and 500 > mouse[1] > 450:
                    player_no()
                elif 600 > mouse[0] > 550 and 500 > mouse[1] > 450:
                    quit()


#                 FUNCTION TO DISPLAY NUMBER OF PLAYERS


def player_no():
    global SIZE, DUP_SIZE
    while True:
        FILL=WHITE
        screen.fill(FILL)
        text_print("choose no of players", LARGETEXT, BLACK, WHITE, [300, 100, 100, 50])
        text_print("ONE", SMALLTEXT, BLACK, YELLOW, [250, 300, 60, 50])
        text_print("TWO", SMALLTEXT, BLACK, GREEN, [350, 300, 60, 50])
        text_print("QUIT!", SMALLTEXT, BLACK, RED, [450, 300, 60, 50])
        pygame.display.update()
        for event in pygame.event.get():
            #print(event)
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse=pygame.mouse.get_pos()
                if 310 > mouse[0] > 250 and 350 > mouse[1] > 300:
                    SIZE = 1
                    DUP_SIZE=2
                    display_board()
                elif 410 > mouse[0] > 350 and 350 > mouse[1] > 300:
                    DUP_SIZE = SIZE = 2
                    display_board()
                elif 510 > mouse[0] > 450 and 350 > mouse[1] > 300:
                    game_intro()


def display_board():
    screen.fill(BLACK)
    screen.blit(IMG, (0, 0))
    sum1 = 0
    num = 0
    sum = 0
    while True:
        if sum1 != 100:                    # condition included conflict in won due to roll and quit
            text_print("ROLL", SMALLTEXT, BLACK, GREEN, [640, 350, 60, 50])
            text_print("QUIT!", SMALLTEXT, BLACK, RED, [720, 350, 60, 50])
            pygame.display.flip()
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    mouse = pygame.mouse.get_pos()
                    print(mouse)
                    if num != SIZE and sum != 6:
                        num += 1
                    elif num == SIZE and sum != 6:
                        num = 1
                    if 700 > mouse[0] > 640 and 400 > mouse[1] > 350:
                        sum, sum1 = player_play(num)
                        if SIZE == 1:
                            time.sleep(1)
                            sum, sum1 = player_play(2)
                        if sum1 == 100:
                            time.sleep(5)
                            won(num)
                    elif 780 > mouse[0] > 720 and 400 > mouse[1] >350:
                        player_no()
                break


def won(num):
    screen.fill(WHITE)
    text_print("Player"+str(num)+"Won", SMALLTEXT, BLACK, WHITE, [300, 100, 100, 50])
    text_print("RE GAME", SMALLTEXT, BLACK, YELLOW, [240, 350, 100, 50])
    text_print("QUIT!", SMALLTEXT, BLACK, GREEN, [540, 350, 100, 50])
    pygame.display.flip()
    pygame.display.update()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse = pygame.mouse.get_pos()
                if 340 > mouse[0] > 240 and 400 > mouse[1] > 350:
                    global player
                    player = [0, 0, 0, 0, 0]
                    global pos
                    pos = [0, 0, 0, 0, 0]
                    game_intro()
                elif 640 > mouse[0] > 540 and 400 > mouse[1] > 350:
                    quit()

#                                DEFINING RESTART GAME AFTER ENDING

game_intro()
quit()
