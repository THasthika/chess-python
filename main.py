import sys, pygame
pygame.init()

from chessboard import ChessBoard, Piece

size = width, height = 640, 640
speed = [5, 5]
black = 0, 0, 0
white = 255, 255, 255

screen = pygame.display.set_mode(size)

ball = pygame.image.load("intro_ball.gif")
ballrect = ball.get_rect()

clock = pygame.time.Clock()

#Size of squares
cellSize = int(min(size) / 10)

#Left pad from screen
leftPad = 20
#Top pad from screen
topPad = 20

#board length, must be even
boardLength = 8

board = ChessBoard()

while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()

    screen.fill(white)

    cnt = 0
    ## draw board
    for i in range(0, 8 * 8):
        x = i % 8
        y = i // 8
        c = white if board.board[i]['color'] == 'w' else black
        pygame.draw.rect(screen, c, [
            leftPad + cellSize * x,
            topPad + cellSize * y,
            cellSize,
            cellSize
        ])
        piece = board.board[i]['piece']
        if piece == None:
            continue
        
        

        # pygame.draw.

    #Add a nice boarder
    pygame.draw.rect(screen, black, [
        leftPad,
        topPad,
        boardLength*cellSize,
        boardLength*cellSize
    ], 1)

    pygame.display.update()