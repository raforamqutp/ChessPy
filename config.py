import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

BOARD_SIZE = 8
SQUARE_SIZE = 150
SCREEN_WIDTH = BOARD_SIZE * SQUARE_SIZE
SCREEN_HEIGHT = SCREEN_WIDTH

ASSETS_DIR = os.path.join(BASE_DIR, "assets", "sprites")
PIECE_PATH = os.path.join(ASSETS_DIR, "piezas")
BOARD_IMAGE = os.path.join(ASSETS_DIR, "tablero.png")
