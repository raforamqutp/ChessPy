import pygame
from config import *
from core.board import Board
from ui.render import draw_board, draw_pieces, load_piece_images, draw_selection
from ui.input_handler import GameInput

pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Ajedrez")
clock = pygame.time.Clock()

board_img = pygame.image.load(BOARD_IMAGE)
board_img = pygame.transform.scale(board_img, (SCREEN_WIDTH, SCREEN_HEIGHT))

board = Board()
piece_images = load_piece_images()
game_input = GameInput(board)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        elif event.type == pygame.MOUSEBUTTONDOWN:
            game_input.handle_click(event.pos)

    draw_board(screen, board_img)
    
    # Dibuja selecciones y movimientos válidos
    draw_selection(screen, game_input.selected_piece, game_input.valid_moves)
    
    draw_pieces(screen, board, piece_images)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
