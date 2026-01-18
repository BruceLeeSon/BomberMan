import arcade

from game import Game

SCREEN_WIDTH = 660
SCREEN_HEIGHT = 660
SCREEN_TITLE = 'BombasticMan'

window = Game(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
window.setup()

arcade.run()