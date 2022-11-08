import pygame
import sys



def check_win(mas, sign):
    zeryes = 0
    for row in mas:
        zeryes += row.count(0)
        if row.count(sign) == 3:
            return sign
    for col in range(3):
        if mas[0][col] == sign and mas[1][col] == sign and mas[2][col] == sign:
            return sign
    if mas[0][0] == sign and mas[1][1] == sign and mas[2][2] == sign:
        return sign
    if mas[0][2] == sign and mas[1][1] == sign and mas[2][0] == sign:
        return sign
    if zeryes == 0:
        return 'НИЧЬЯ'
    return False

pygame.init()
size_block =100
margin = 15
width = heigt = size_block*3 +margin*4

size_window =(width, heigt)
screen = pygame.display.set_mode(size_window)
pygame.display.set_caption('Крестики - нолики')

black = (0, 0, 0)
red = (255, 0, 0)
green = (0, 255, 0)
white = (255, 255, 255)
mas = [[0]*3 for i in range(3)]
queri = 0
game_over = False

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN and not game_over:
            x_mouse, y_mouse = pygame.mouse.get_pos()
            col = x_mouse // (size_block+margin)
            row = y_mouse // (size_block + margin)
            if mas[row][col] == 0:
                if queri % 2 == 0:
                    mas[row][col] = 'X'
                else:
                    mas[row][col] = 'O'
                queri += 1
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            game_over = False
            mas = [[0] * 3 for i in range(3)]
            queri = 0
            screen.fill(black)

    if not game_over:
        for row in range(3):
            for col in range(3):
                if mas[row][col] == 'X':
                    color = red
                elif mas[row][col] == 'O':
                    color = green
                else:
                    color = white
                x = col * size_block + (col + 1)*margin
                y = row * size_block + (row + 1) * margin
                pygame.draw.rect(screen, color, (x, y, size_block, size_block))
                if color == red:
                    pygame.draw.line(screen, black, (x + 5, y + 5), (x + size_block - 5, y + size_block - 5,), 3)
                    pygame.draw.line(screen, black, (x + size_block - 5, y + 5), (x + 5, y + size_block - 5,), 3)
                elif color == green:
                    pygame.draw.circle(screen, black, (x + size_block//2, y + size_block//2), size_block//2 - 3, 3)
        if (queri - 1) % 2 == 0:
           game_over = check_win(mas, 'X')
        else:
           game_over = check_win(mas, 'O')

        if game_over:
            screen.fill(black)
            font = pygame.font.SysFont('stxingkay', 80)
            text1 = font.render(game_over, True, white)
            text_rect = text1.get_rect()
            text_x = screen.get_width() / 2 - text_rect.width /2
            text_y = screen.get_height() / 2 - text_rect.height /2
            screen.blit(text1, [text_x, text_y])
        pygame.display.update()