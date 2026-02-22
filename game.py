import arcade
import constants
import random
from bomberman import BomberMan

class ExplodableBlock(arcade.Sprite):
    def __init__(self):
        super().__init__("Blocks/ExplodableBlock.png", 1)


class SolidBlock(arcade.Sprite):
    def __init__(self):
        super().__init__("Blocks/SolidBlock.png", 1)


class Game(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title)
        self.bg_tile = arcade.load_texture("Blocks/BackgroundTile.png")
        self.solid_blocks = arcade.SpriteList()
        self.explodable_blocks = arcade.SpriteList()
        self.player1 = BomberMan()

    def setup(self):
        for y in range(constants.ROW_COUNT):
            for x in range(constants.COLUMN_COUNT):
                if x % 2 == 1 and y % 2 == 1:
                    solid_block = SolidBlock()
                    solid_block.center_x = x * constants.CELL_WIDTH + constants.CELL_WIDTH / 2
                    solid_block.center_y = y * constants.CELL_HEIGHT + constants.CELL_HEIGHT / 2
                    self.solid_blocks.append(solid_block)

                elif random.randint(1, 2) == 1:
                    if not (x == 0 and y <= 2) and not (y == 0 and x <= 2) and not (x >= 8 and y == 10) and not (
                            x == 10 and y >= 8):
                        explodable_block = ExplodableBlock()
                        explodable_block.center_x = x * constants.CELL_WIDTH + constants.CELL_WIDTH / 2
                        explodable_block.center_y = y * constants.CELL_HEIGHT + constants.CELL_HEIGHT / 2
                        self.explodable_blocks.append(explodable_block)

        x = constants.SCREEN_WIDTH / constants.COLUMN_COUNT - constants.CELL_WIDTH / 2
        y = constants.SCREEN_HEIGHT / constants.ROW_COUNT - constants.CELL_HEIGHT / 2
        self.player1.set_position(x, y)

    def draw_background(self):
        for y in range(constants.ROW_COUNT):
            for x in range(constants.COLUMN_COUNT):
                arcade.draw_texture_rectangle(
                    x * constants.CELL_WIDTH + constants.CELL_WIDTH / 2,
                    y * constants.CELL_HEIGHT + constants.CELL_HEIGHT / 2,
                    constants.CELL_WIDTH,
                    constants.CELL_HEIGHT,
                    self.bg_tile

                )

    def on_draw(self):
        self.clear((255, 255, 255))
        self.draw_background()
        self.solid_blocks.draw()
        self.explodable_blocks.draw()
        self.player1.draw()

    def update(self, delta_time: float):
        self.player1.update_animation(delta_time)

    def on_key_press(self, symbol: int, modifiers: int):
        if symbol == arcade.key.LEFT:
            self.player1.direction = 1
        elif symbol == arcade.key.RIGHT:
            self.player1.direction = 2
        elif symbol == arcade.key.UP:
            self.player1.direction = 3
        elif symbol == arcade.key.DOWN:
            self.player1.direction = 4

        self.player1.change_costume()

    def on_key_release(self, symbol: int, modifiers: int):
        pass
