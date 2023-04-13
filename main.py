import pygame, sys
from pygame.locals import QUIT
import math

pygame.init()
DISPLAYSURF = pygame.display.set_mode((400, 300))
pygame.display.set_caption('TIC TAC TOE!')
game = [["", "", ""], ["", "", ""], ["", "", ""]]

XWinMoves = [["", "X", "X"], ["X", "", "X"], ["X", "X", ""]]


def changesomething():
    print("changed in repl test 04")


def checkValue(m, p):
    r = math.ceil(p / 3) - 1
    c = (p - (r * 3)) - 1
    return m[r][c]


def coordinates(p):
    r = math.ceil(p / 3) - 1
    c = (p - (r * 3)) - 1
    return (r, c)


def DisplayGameBoard(game):
    pygame.draw.line(DISPLAYSURF, (255, 0, 0), (100, 10), (100, 200))
    pygame.draw.line(DISPLAYSURF, (255, 0, 0), (150, 10), (150, 200))
    pygame.draw.line(DISPLAYSURF, (255, 0, 0), (20, 80), (220, 80))
    pygame.draw.line(DISPLAYSURF, (255, 0, 0), (20, 120), (220, 120))
    c_count = 0
    r_count = 0
    for r in game:
        for c in r:
            if c.upper() == "X":
                draw_x(c_count, r_count)
            elif c.upper() == "O":
                draw_o(c_count, r_count)
            c_count += 1
        r_count += 1
        c_count = 0


def draw_o(x, y):
    font = pygame.font.Font('freesansbold.ttf', 32)
    text = font.render('O', True, (0, 255, 0), (0, 0, 0))
    textRect = text.get_rect()
    textRect.center = ((70 * x) + 50, (50 * y) + 50)
    DISPLAYSURF.blit(text, textRect)


def draw_x(x, y):
    font = pygame.font.Font('freesansbold.ttf', 32)
    text = font.render('X', True, (0, 255, 0), (0, 0, 0))
    textRect = text.get_rect()
    textRect.center = ((70 * x) + 50, (50 * y) + 50)
    DISPLAYSURF.blit(text, textRect)


def isWinning(m, p):
    result = False
    s = "X"
    tmp = m
    r, c = coordinates(p)
    tmp[r][c] = s
    # print (f"m:{tmp} -- p:{tmp[r][c]}")
    if tmp[0] == [s, s, s] or tmp[1] == [s, s, s] or tmp[2] == [
            s, s, s
    ]:  # Check rows
        result = True
    if [tmp[0][0], tmp[1][0], tmp[2][0]] == [s, s, s] or [
            tmp[0][1], tmp[1][1], tmp[2][1]
    ] == [s, s, s] or [tmp[0][2], tmp[1][2], tmp[2][2]] == [s, s, s
                                                            ]:  # Check cols
        result = True
    if [m[0][0], m[1][1], m[2][2]] == [s, s, s] or [
            m[0][2], m[1][1], m[2][0]
    ] == [s, s, s]:  #Check diagonals
        result = True
    return result


def winningMoves(lm):
    tmp = game
    winningMoves = []
    for i in range(0, len(lm)):
        print(tmp, i)
        if isWinning(tmp, i):
            print(f"{i} is a winning move")
            winningMoves.append(i)
    return winningMoves


def checkWin(s):
    result = False
    # Check Horizontal positions
    if game[0] == [s, s, s] or game[1] == [s, s, s] or game[2] == [s, s, s]:
        result = True
    # Check Vertical positions
    if [game[0][0], game[0][1], game[0][2]] == [s, s, s] or [
            game[1][0], game[1][1], game[1][2]
    ] == [s, s, s] or [game[2][0], game[2][1], game[2][2]] == [s, s, s]:
        result = True
    # Check Diagonal positions
    if [game[0][0], game[1][1], game[2][2]
        ] == [s, s, s] or [game[0][2], game[1][1], game[2][0]] == [s, s, s]:
        result = True
    return result


def legalXMoves():
    lm = []
    for p in range(1, 10):
        v = checkValue(game, p)
        # print (f"position:{p} - value:{v}")
        if v == "":
            lm.append(p)
    return lm


def PlayerMove(selection):
    v = checkValue(game, selection)
    result = v.strip() != ""
    # print (f"Player Move: {selection} - [{v}] - {result}")
    if not result:
        pos = coordinates(selection)
        game[pos[0]][pos[1]] = "O"
    return result


def checkXMoves():
    #creates a list of legal moves
    xMoves = []
    legalMoves = []
    for i in range(0, 9):
        if game[i] == "":
            legalMoves.append(i)
    for lm in legalMoves:
        tmp = game
        tmp[lm] = "X"
        # Check rows
        if tmp[0] in winningMoves or tmp[1] in winningMoves or tmp[
                2] in winningMoves:
            xMoves.append(lm)
        #Check cols
        if [tmp[0][0], tmp[0][1], tmp[0][2]] in winningMoves or [
                tmp[1][0], tmp[1][1], tmp[2][2]
        ] in winningMoves or [tmp[2][0], tmp[2][1], tmp[2][2]] in winningMoves:
            xMoves.append(lm)
        #Check diagonals
        if [tmp[0][0], tmp[1][1], tmp[2][2]
            ] in winningMoves or [tmp[0][2], tmp[1][1], tmp[2][0]]:
            xMoves.append(lm)
    return xMoves


def PythonMove():

    # returns the python move or a negative number
    # the nagative number means that the player won, there are no valid moves for python
    print("Python turn")
    legal_moves = []
    winning_moves = []
    # Creates a list of legal move
    legal_moves = legalXMoves()
    # Check if any of the legal moves bring python to a win situation
    winning_moves = winningMoves(legal_moves)
    if len(winning_moves) <= 0:
        print("There are no winning moves")
    else:
        print("There is at least one winning move")


def main():

    # print ("SRART")
    # game = [["O", "", "O"], ["X", "X", ""], ["X", "X", "O"]]
    # # game = [["1", "2", "3"], ["4", "5", "6"], ["7", "8", "9"]]
    # print (f"outcome:{isWinning(game,2)}")
    # print ("END")

    while True:
        DisplayGameBoard(game)
        player_turn = True
        gameOver = False
        for event in pygame.event.get():
            if event.type == QUIT or gameOver:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN and player_turn and not gameOver:
                if event.key == pygame.K_1:
                    plater_turn = PlayerMove(1)
                elif event.key == pygame.K_2:
                    plater_turn = PlayerMove(2)
                elif event.key == pygame.K_3:
                    plater_turn = PlayerMove(3)
                elif event.key == pygame.K_4:
                    plater_turn = PlayerMove(4)
                elif event.key == pygame.K_5:
                    plater_turn = PlayerMove(5)
                elif event.key == pygame.K_6:
                    plater_turn = PlayerMove(6)
                elif event.key == pygame.K_7:
                    plater_turn = PlayerMove(7)
                elif event.key == pygame.K_8:
                    plater_turn = PlayerMove(8)
                elif event.key == pygame.K_9:
                    plater_turn = PlayerMove(9)
                else:
                    print("Illegal Move")
                gameOver = checkWin("O")
                if gameOver:
                    print("GAME OVER")
                if not plater_turn:
                    PythonMove()
                    player_turn = True
        pygame.display.update()


if __name__ == "__main__":
    main()
