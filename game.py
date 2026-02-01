import arcade
import constants


class SolidBlock(arcade.Sprite):
    def __init__(self):
        super().__init__("Blocks/SolidBlock.png", 1)



class Game(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title)
        self.bg_tile = arcade.load_texture("Blocks/BackgroundTile.png")
        self.solid_blocks = arcade.SpriteList()

    def setup(self):
        for y in range(constants.ROW_COUNT):
            for x in range(constants.COLUMN_COUNT):
                if x % 2 == 1 and y % 2 == 1:
                    solid_block = SolidBlock()
                    solid_block.center_x = x * constants.CELL_WIDTH
                    solid_block.center_y = y * constants.CELL_HEIGHT
                    self.solid_blocks.append(solid_block)

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

    def update(self, delta_time: float):
        pass

    def on_key_press(self, symbol: int, modifiers: int):
        pass

    def on_key_release(self, symbol: int, modifiers: int):
        pass
