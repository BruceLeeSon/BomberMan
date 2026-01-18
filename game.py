import arcade


class Game(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title)

    def setup(self):
        pass

    def on_draw(self):
        pass

    def update(self, delta_time: float):
        pass

    def on_key_press(self, symbol: int, modifiers: int):
        pass

    def on_key_release(self, symbol: int, modifiers: int):
        pass
