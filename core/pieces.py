class Piece:
    def __init__(self, name, color, pos):
        self.name = name
        self.color = color
        self.pos = pos
        self.has_moved = False  # Importante para enroque y peones

    def get_image_name(self):
        return f"{self.color}_{self.name}.png"

    # Función genérica de movimientos (sobrescrita en subclases)
    def get_valid_moves(self, board):
        return []
    
    # Función de orden superior para filtrar movimientos
    def filter_valid_moves(self, moves, board):
        return [move for move in moves if self._is_move_valid(move, board)]
    
    def _is_move_valid(self, move, board):
        # Lógica básica: dentro del tablero y no captura propia
        row, col = move
        return 0 <= row < 8 and 0 <= col < 8 and (
            not board.grid[row][col] or board.grid[row][col].color != self.color
        )
    
    def _get_diagonal_moves(self, board):
        row, col = self.pos
        moves = []
        directions = [(-1, -1), (-1, 1), (1, -1), (1, 1)]
        
        for dr, dc in directions:
            for i in range(1, 8):
                r, c = row + i*dr, col + i*dc
                if not (0 <= r < 8 and 0 <= c < 8):
                    break
                
                target = board.grid[r][c]
                if not target:
                    moves.append((r, c))
                elif target.color != self.color:
                    moves.append((r, c))
                    break
                else:
                    break
        
        return moves
    
    def _get_straight_moves(self, board):
        row, col = self.pos
        moves = []
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        
        for dr, dc in directions:
            for i in range(1, 8):
                r, c = row + i*dr, col + i*dc
                if not (0 <= r < 8 and 0 <= c < 8):
                    break
                
                target = board.grid[r][c]
                if not target:
                    moves.append((r, c))
                elif target.color != self.color:
                    moves.append((r, c))
                    break
                else:
                    break
        
        return moves


class Pawn(Piece):
    def __init__(self, color, pos):
        super().__init__("pawn", color, pos)
        self.direction = -1 if color == "w" else 1  # Blancos suben, negros bajan

    def get_valid_moves(self, board):
        row, col = self.pos
        moves = []
        
        # Movimiento hacia adelante
        if not board.grid[row + self.direction][col]:
            moves.append((row + self.direction, col))
            
            # Doble movimiento inicial
            start_row = 6 if self.color == "w" else 1
            if row == start_row and not board.grid[row + 2*self.direction][col]:
                moves.append((row + 2*self.direction, col))
        
        # Capturas diagonales
        for offset in [-1, 1]:
            if 0 <= col + offset < 8 and board.grid[row + self.direction][col + offset]:
                if board.grid[row + self.direction][col + offset].color != self.color:
                    moves.append((row + self.direction, col + offset))
        
        return self.filter_valid_moves(moves, board)


class Knight(Piece):
    def __init__(self, color, pos):
        super().__init__("knight", color, pos)

    def get_valid_moves(self, board):
        row, col = self.pos
        knight_moves = [
            (row-2, col-1), (row-2, col+1),
            (row-1, col-2), (row-1, col+2),
            (row+1, col-2), (row+1, col+2),
            (row+2, col-1), (row+2, col+1)
        ]
        return self.filter_valid_moves(knight_moves, board)


class Bishop(Piece):
    def __init__(self, color, pos):
        super().__init__("bishop", color, pos)

    def get_valid_moves(self, board):
        moves = self._get_diagonal_moves(board)
        return self.filter_valid_moves(moves, board)


class Rook(Piece):
    def __init__(self, color, pos):
        super().__init__("rook", color, pos)

    def get_valid_moves(self, board):
        moves = self._get_straight_moves(board)
        return self.filter_valid_moves(moves, board)


class Queen(Piece):
    def __init__(self, color, pos):
        super().__init__("queen", color, pos)

    def get_valid_moves(self, board):
        diagonal = self._get_diagonal_moves(board)
        straight = self._get_straight_moves(board)
        moves = diagonal + straight
        return self.filter_valid_moves(moves, board)


class King(Piece):
    def __init__(self, color, pos):
        super().__init__("king", color, pos)

    def get_valid_moves(self, board):
        row, col = self.pos
        king_moves = [
            (row-1, col-1), (row-1, col), (row-1, col+1),
            (row, col-1), (row, col+1),
            (row+1, col-1), (row+1, col), (row+1, col+1)
        ]
        return self.filter_valid_moves(king_moves, board)