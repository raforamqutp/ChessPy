from core.pieces import *

class Board:
    def __init__(self):
        self.grid = [[None for _ in range(8)] for _ in range(8)]
        self.setup_pieces()
    
    def setup_pieces(self):
        # Peones
        for i in range(8):
            self.grid[1][i] = Pawn("b", (1, i))
            self.grid[6][i] = Pawn("w", (6, i))
        
        # Piezas negras
        self.grid[0][0] = Rook("b", (0, 0))
        self.grid[0][1] = Knight("b", (0, 1))
        self.grid[0][2] = Bishop("b", (0, 2))
        self.grid[0][3] = Queen("b", (0, 3))
        self.grid[0][4] = King("b", (0, 4))
        self.grid[0][5] = Bishop("b", (0, 5))
        self.grid[0][6] = Knight("b", (0, 6))
        self.grid[0][7] = Rook("b", (0, 7))
        
        # Piezas blancas
        self.grid[7][0] = Rook("w", (7, 0))
        self.grid[7][1] = Knight("w", (7, 1))
        self.grid[7][2] = Bishop("w", (7, 2))
        self.grid[7][3] = Queen("w", (7, 3))
        self.grid[7][4] = King("w", (7, 4))
        self.grid[7][5] = Bishop("w", (7, 5))
        self.grid[7][6] = Knight("w", (7, 6))
        self.grid[7][7] = Rook("w", (7, 7))
