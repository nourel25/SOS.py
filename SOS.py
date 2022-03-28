import pygame
import sys
import time

pygame.init()

board_row = 4
board_col = 4
WIDTH = 600
LENGTH = 600
round_num = 1
score = [0, 0]
i = [False] * 25
play_again = False
font = pygame.font.SysFont(None, 130, False, True)
screen = pygame.display.set_mode((WIDTH, LENGTH))
pygame.display.set_caption("S-O-S.Game")
# start_img = pygame.image.load('start_btn.png').convert_alpha()
# exit_img = pygame.image.load('exit_btn.png').convert_alpha()


BG_color = (28, 170, 156)
# array 2D
board = [[" ", " ", " ", " "], [" ", " ", " ", " "], [" ", " ", " ", " "], [" ", " ", " ", " "]]


def end_screen():
    if score[1] > score[0]:
        winner = "player1"
    elif score[0] > score[1]:
        winner = "player2"
    else:
        winner = "equal"

    screen_end = pygame.display.set_mode((500, 230))
    screen_end.fill(BG_color)
    font_end = pygame.font.SysFont(None, 40, False, True)
    res_1 = font_end.render(str(score[0]), True, (250, 250, 250), None)
    res_2 = font_end.render(str(score[1]), True, (30, 30, 30), None)
    win = font_end.render("player 1", True, (250, 250, 250), None)
    win2 = font_end.render("player 2", True, (30, 30, 30), None)
    screen_end.blit(win, (70, 80))
    screen_end.blit(win2, (300, 80))
    screen_end.blit(res_1, (110, 120))
    screen_end.blit(res_2, (340, 120))
    # screen.blit(start_img, (30, 370))
    # screen.blit(exit_img, (330, 370))


def draw_lines():  # 4 * 4
    line_width = 5
    line_color = (80, 80, 80)

    pygame.draw.line(screen, line_color, (0, 150), (600, 150), line_width)  # H1
    pygame.draw.line(screen, line_color, (0, 300), (600, 300), line_width)  # H2
    pygame.draw.line(screen, line_color, (0, 450), (600, 450), line_width)  # H3
    pygame.draw.line(screen, line_color, (150, 0), (150, 600), line_width)  # V1
    pygame.draw.line(screen, line_color, (300, 0), (300, 600), line_width)  # V2
    pygame.draw.line(screen, line_color, (450, 0), (450, 600), line_width)  # V3


def tx_start():
    screen.fill(BG_color)
    draw_lines()
    font = pygame.font.Font(None, 80)
    font_wel = pygame.font.SysFont(None, 40, False, True)
    so_test = font.render("S | O", True, (30, 30, 30), (0, 102, 102))
    welcome = font_wel.render("player 1 you Black, player 2 you White", True, (255, 255, 255), (0, 0, 0))

    for row in range(board_row):
        for col in range(board_col):
            screen.blit(so_test, (15 + 150 * row, 40 + 150 * col))

    screen.blit(welcome, (30, 120))
tx_start()


def draw_fig(s_or_o):
    global round_num
    screen.fill(BG_color)
    draw_lines()

    for idx, row in enumerate(board):
        for idx2, col in enumerate(board):

            if board[idx][idx2] == "s" or board[idx][idx2] == "o":
                letter = font.render(board[idx][idx2].upper(), True, (250, 250, 250))
                screen.blit(letter, (50 + idx2 * 150, 30 + idx * 150))

            else:
                letter_2 = font.render(board[idx][idx2], True, (30, 30, 30))
                screen.blit(letter_2, (50 + idx2 * 150, 30 + idx * 150))

    check_point()
    round_num += 1


def available(row, col):
    if board[clicked_row][clicked_col] == " ":
        board[clicked_row][clicked_col] = s_or_o


def is_board_full():
    for row in range(board_row):
        for col in range(board_col):
            if board[row][col] == " ":
                return False
    return True
    print(score)
print(is_board_full())


def check_point():
    row = 0
    col = 0
    global i
    global round_num

    if board[row][col].upper() == "S":
        if board[row + 1][col].upper() == "O" and board[row + 2][col].upper() == "S":
            if i[0] == False:
                round_num -= 1
                if round_num % 2:
                    score[0] += 1
                    i[0] = True
                else:
                    score[1] += 1
                    i[0] =True
        elif board[row][col + 1].upper() == "O" and board[row][col + 2].upper() == "S":
            if i[1] == False:
                round_num -= 1
                if round_num % 2:
                    score[0] += 1
                    i[1] = True
                else:
                    score[1] += 1
                    i[1] = True
        elif board[row + 1][col + 1].upper() == "O" and board[row + 2][col + 2].upper() == "S":
            if i[2] == False:
                round_num -= 1
                if round_num % 2:
                    score[0] += 1
                    i[2] = True
                else:
                    score[1] += 1
                    i[2] = True

    if board[row + 1][col].upper() == "S":
        if board[row + 2][col].upper() == "O" and board[row + 3][col].upper() == "S":
            if i[3] == False:
                round_num -= 1
                if round_num % 2:
                    score[0] += 1
                    i[3] = True
                else:
                    score[1] += 1
                    i[3] = True
        elif board[row + 1][col + 1].upper() == "O" and board[row + 1][col + 2].upper() == "S":
            if i[4] == False:
                round_num -= 1
                if round_num % 2:
                    score[0] += 1
                    i[4] = True
                else:
                    score[1] += 1
                    i[4] = True
        elif board[row + 2][col + 1].upper() == "O" and board[row + 3][col + 2].upper() == "S":
            if i[5] == False:
                round_num -= 1
                if round_num % 2:
                    score[0] += 1
                    i[5] = True
                else:
                    score[1] += 1
                    i[5] = True

    if board[row + 2][col].upper() == "S":
        if board[row + 2][col + 1].upper() == "O" and board[row + 2][col + 2].upper() == "S":
            if i[6] == False:
                round_num -= 1
                if round_num % 2:
                    score[0] += 1
                    i[6] = True
                else:
                    score[1] += 1
                    i[6] = True
        elif board[row + 1][col + 1].upper() == "O" and board[row][col + 2].upper() == "S":
            if i[7] == False:
                round_num -= 1
                if round_num % 2:
                    score[0] += 1
                    i[7] = True
                else:
                    score[1] += 1
                    i[7] = True

    if board[row][col + 1].upper() == "S":
        if board[row + 1][col + 1].upper() == "O" and board[row + 2][col + 1].upper() == "S":
            if i[8] == False:
                round_num -= 1
                if round_num % 2:
                    score[0] += 1
                    i[8] = True
                else:
                    score[1] += 1
                    i[8] = True
        elif board[row + 1][col + 2].upper() == "O" and board[row + 2][col + 3].upper() == "S":
            if i[9] == False:
                round_num -= 1
                if round_num % 2:
                    score[0] += 1
                    i[9] = True
                else:
                    score[1] += 1
                    i[9] = True
        elif board[row][col + 2].upper() == "O" and board[row][col + 3].upper() == "S":
            if i[10] == False:
                round_num -= 1
                if round_num % 2:
                    score[0] += 1
                    i[10] = True
                else:
                    score[1] += 1
                    i[10] = True

    if board[row][col + 2].upper() == "S":
        if board[row + 1][col + 2].upper() == "O" and board[row + 2][col + 2].upper() == "S":
            if i[11] == False:
                round_num -= 1
                if round_num % 2:
                    score[0] += 1
                    i[11] = True
                else:
                    score[1] += 1
                    i[11] = True

    if board[row][col + 3].upper() == "S":
        if board[row + 1][col + 3].upper() == "O" and board[row + 2][col + 3].upper() == "S":
            if i[12] == False:
                round_num -= 1
                if round_num % 2:
                    score[0] += 1
                    i[12] = True
                else:
                    score[1] += 1
                    i[12] = True
        elif board[row + 1][row + 2].upper() == "O" and board[row + 2][col + 1] == "S":
            if i[13] == False:
                round_num -= 1
                if round_num % 2:
                    score[0] += 1
                    i[13] = True
                else:
                    score[1] += 1
                    i[13] = True

    if board[row + 3][col].upper() == "S":
        if board[row + 3][col + 1].upper() == "O" and board[row + 3][col + 2].upper() == "S":
            if i[14] == False:
                round_num -= 1
                if round_num % 2:
                    score[0] += 1
                    i[14] = True
                else:
                    score[1] += 1
                    i[14] = True
        elif board[row + 2][col + 1].upper() == "O" and board[row + 1][col + 2].upper() == "S":
            if i[15] == False:
                round_num -= 1
                if round_num % 2:
                    score[0] += 1
                    i[15] = True
                else:
                    score[1] += 1
                    i[15] = True

    if board[row + 1][col + 1].upper() == "S":
        if board[row + 1][col + 2].upper() == "O" and board[row + 1][col + 3].upper() == "S":
            if i[16] == False:
                round_num -= 1
                if round_num % 2:
                    score[0] += 1
                    i[16] = True
                else:
                    score[1] += 1
                    i[16] = True
        elif board[row + 2][col + 1].upper() == "O" and board[row + 3][col + 1].upper() == "S":
            if i[17] == False:
                round_num -= 1
                if round_num % 2:
                    score[0] += 1
                    i[17] = True
                else:
                    score[1] += 1
                    i[17] = True
        elif board[row + 2][col + 2].upper() == "O" and board[row + 3][col + 3].upper() == "S":
            if i[18] == False:
                round_num -= 1
                if round_num % 2:
                    score[0] += 1
                    i[18] = True
                else:
                    score[1] += 1
                    i[18] = True
    if board[row + 1][col + 2].upper() == "S":
        if board[row + 2][col + 2].upper() == "O" and board[row + 3][col + 2].upper() == "S":
            if i[19] == False:
                round_num -= 1
                if round_num % 2:
                    score[0] += 1
                    i[19] = True
                else:
                    score[1] += 1
                    i[19] = True

    if board[row + 2][col + 1].upper() == "S":
        if board[row + 2][col + 2].upper() == "O" and board[row + 2][col + 3].upper() == "S":
            if i[20] == False:
                round_num -= 1
                if round_num % 2:
                    score[0] += 1
                    i[20] = True
                else:
                    score[1] += 1
                    i[20] = True

    if board[row + 3][col + 1].upper() == "S":
        if board[row + 3][col + 2].upper() == "O" and board[row + 3][col + 3].upper() == "S":
            if i[21] == False:
                round_num -= 1
                if round_num % 2:
                    score[0] += 1
                    i[21] = True
                else:
                    score[1] += 1
                    i[21] = True
        if board[row + 2][col + 2].upper() == "O" and board[row + 1][col + 3].upper() == "S":
            if i[22] == False:
                round_num -= 1
                if round_num % 2:
                    score[0] += 1
                    i[22] = True
                else:
                    score[1] += 1
                    i[22] = True

        if board[row + 1][col + 3].upper() == "S":
            if board[row + 2][col + 3].upper() == "O" and board[row + 3][col + 3].upper() == "S":
                if i[23] == False:
                    round_num -= 1
                    if round_num % 2:
                        score[0] += 1
                        i[23] = True
                    else:
                        score[1] += 1
                        i[23] = True


game_over = True
while game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        if is_board_full():
            end_screen()
            game_over = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            mouseX = event.pos[0]  # x
            mouseY = event.pos[1]  # y

            clicked_col = int(mouseX // 150)
            clicked_row = int(mouseY // 150)
            test = mouseX - 150 * clicked_col

            if round_num % 2:
                s_or_o = "S" if test < 75 else "O"
            else:
                s_or_o = "s" if test < 75 else "o"

            available(clicked_row, clicked_col)
            draw_fig(s_or_o)
            print(board)

    pygame.display.update()

time.sleep(3)
pygame.quit()