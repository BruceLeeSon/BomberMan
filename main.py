import arcade

from game import Game
import constants

window = Game(constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT, constants.SCREEN_TITLE)
window.setup()

arcade.run()