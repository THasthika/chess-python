class Piece:

    TYPE_PAWN = 0
    TYPE_ROOK = 1
    TYPE_KNIGHT = 2
    TYPE_BISHOP = 3
    TYPE_QUEEN = 4
    TYPE_KING = 5

    COLOR_WHITE = 0
    COLOR_BLACK = 1

    def __init__(self, pType, pColor):
        self.pType = pType
        self.pColor = pColor

    def __str__(self):
        if self.pColor == Piece.COLOR_WHITE:
            if self.pType == Piece.TYPE_PAWN:
                return 'P'
            elif self.pType == Piece.TYPE_ROOK:
                return 'R'
            elif self.pType == Piece.TYPE_KNIGHT:
                return 'N'
            elif self.pType == Piece.TYPE_BISHOP:
                return 'B'
            elif self.pType == Piece.TYPE_QUEEN:
                return 'Q'
            elif self.pType == Piece.TYPE_KING:
                return 'K'
        elif self.pColor == Piece.COLOR_BLACK:
            if self.pType == Piece.TYPE_PAWN:
                return 'p'
            elif self.pType == Piece.TYPE_ROOK:
                return 'r'
            elif self.pType == Piece.TYPE_KNIGHT:
                return 'n'
            elif self.pType == Piece.TYPE_BISHOP:
                return 'b'
            elif self.pType == Piece.TYPE_QUEEN:
                return 'q'
            elif self.pType == Piece.TYPE_KING:
                return 'k'
        raise Exception("invalid piece")


class ChessBoard:

    def __init__(self):
        self.__init_board()
        
    def __init_board(self):

        self.board = [
            {'piece': None, 'color': 'w' if x % 2 == 0 else 'b'} for x in range(0, 8 * 8)
        ]

        for i in range(8):
            if i % 2 == 1:
                self.board[i*8:(i+1)*8] = reversed(self.board[i*8:(i+1)*8])

        for i in range(8):
            ## place white pieces
            self.board[1 * 8 + i]['piece'] = Piece(Piece.TYPE_PAWN, Piece.COLOR_WHITE)

            ## place black pieces
            self.board[6 * 8 + i]['piece'] = Piece(Piece.TYPE_PAWN, Piece.COLOR_BLACK)

            pType = Piece.TYPE_ROOK
            if i == 0 or i == 7:
                pType = Piece.TYPE_ROOK
            elif i == 1 or i == 6:
                pType = Piece.TYPE_KNIGHT
            elif i == 2 or i == 5:
                pType = Piece.TYPE_BISHOP
            elif i == 3:
                pType = Piece.TYPE_QUEEN
            elif i == 4:
                pType = Piece.TYPE_KING
            

            self.board[i]['piece'] = Piece(pType, Piece.COLOR_WHITE)

            self.board[7 * 8 + i]['piece'] = Piece(pType, Piece.COLOR_BLACK)

    def map_location(self, l, n):
        assert l in [chr(x+ord('a')) for x in range(0, 8)]
        assert n >= 1 and n <= 8

        x = ord(l) - ord('a')
        y = n - 1



        print(x, y)

    def __str__(self):
        ret = ''
        for x in range(0, 8):
            ret += ' '.join(map(lambda x: '-' if x['piece'] == None else str(x['piece']), self.board[x*8:(x+1)*8])) + '\n'
        return ret