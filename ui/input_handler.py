from config import SQUARE_SIZE, BOARD_SIZE

def get_board_position(mouse_pos):
    """Convierte posición del mouse a coordenadas de tablero"""
    x, y = mouse_pos
    row = y // SQUARE_SIZE
    col = x // SQUARE_SIZE
    return row, col

class GameInput:
    def __init__(self, board):
        self.board = board
        self.selected_piece = None
        self.valid_moves = []
        self.current_player = "w"  # Comienza blanco
    
    def handle_click(self, mouse_pos):
        row, col = get_board_position(mouse_pos)
        piece = self.board.grid[row][col]
        
        # Seleccionar pieza del jugador actual
        if not self.selected_piece and piece and piece.color == self.current_player:
            self.selected_piece = piece
            self.valid_moves = piece.get_valid_moves(self.board)
            return "piece_selected"
        
        # Mover pieza seleccionada
        elif self.selected_piece:
            if (row, col) in self.valid_moves:
                self._move_piece(self.selected_piece, (row, col))
                self.selected_piece = None
                self.valid_moves = []
                self.current_player = "b" if self.current_player == "w" else "w"
                return "move_made"
            else:
                self.selected_piece = None
                self.valid_moves = []
                return "selection_cleared"
    
    def _move_piece(self, piece, new_pos):
        # Actualiza estado del tablero
        old_row, old_col = piece.pos
        new_row, new_col = new_pos
        
        # Actualiza posición de la pieza
        self.board.grid[old_row][old_col] = None
        self.board.grid[new_row][new_col] = piece
        piece.pos = (new_row, new_col)
        piece.has_moved = True