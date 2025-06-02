import pygame
from config import *
from core.board import Board

def load_piece_images():
    piece_images = {}
    color_dirs = {"w": "blanco", "b": "negro"}

    for color, folder in color_dirs.items():
        for name in ["pawn", "rook", "knight", "bishop", "queen", "king"]:
            filename = f"{color}_{name}.png"
            full_path = os.path.join(PIECE_PATH, folder, filename)

            try:
                img = pygame.image.load(full_path)
                piece_images[f"{color}_{name}.png"] = img
            except FileNotFoundError:
                print(f"No se encontró la imagen de la pieza: {full_path}")

    return piece_images

def draw_board(screen, board_img):
    screen.blit(board_img, (0, 0))

def draw_pieces(screen, board, piece_images):
    for row in range(8):
        for col in range(8):
            piece = board.grid[row][col]
            if piece:
                img = piece_images[piece.get_image_name()]
                img_rect = img.get_rect()

                x = col * SQUARE_SIZE
                y = row * SQUARE_SIZE

                x += (SQUARE_SIZE - img_rect.width) // 2
                y += (SQUARE_SIZE - img_rect.height) // 2

                screen.blit(img, (x, y))


def highlight_square(screen, position, color=(255, 255, 0, 150)):
    """Resalta una casilla del tablero"""
    row, col = position
    highlight = pygame.Surface((SQUARE_SIZE, SQUARE_SIZE), pygame.SRCALPHA)
    highlight.fill(color)
    screen.blit(highlight, (col * SQUARE_SIZE, row * SQUARE_SIZE))

def draw_selection(screen, selected_piece, valid_moves):
    """Dibuja selección y movimientos válidos"""
    if selected_piece:
        # Resalta pieza seleccionada
        highlight_square(screen, selected_piece.pos, (0, 255, 0, 100))
        
        # Resalta movimientos válidos
        for move in valid_moves:
            highlight_square(screen, move, (0, 0, 255, 100))