import arcade
from arcade import check_for_collision_with_list

import animate
import constants
import random
from bomberman import BomberMan
import time



def justify_x(position_x):
    for x in range(constants.COLUMN_COUNT):
        cell_center_x = x * constants.CELL_WIDTH + constants.CELL_WIDTH / 2
        if position_x - cell_center_x <= constants.CELL_WIDTH / 2:
            return cell_center_x

def justify_y(position_y):
    for y in range(constants.ROW_COUNT):
        cell_center_y = y * constants.CELL_HEIGHT + constants.CELL_HEIGHT / 2
        if position_y - cell_center_y <= constants.CELL_HEIGHT / 2:
            return cell_center_y



class Bomb(animate.Animate):
    def __init__(self, window, power = 3):
        super().__init__("Bomb/Bomb_f00.png", 0.7)
        for i in range(3):
            self.append_texture(arcade.load_texture(f"Bomb/Bomb_f0{i}.png"))
        self.spawn_time = time.time()
        self.window = window
        self.power = power

    def update(self):
        if time.time() - self.spawn_time > 3:
            exp = Explosion(self.window)
            exp.center_x = self.center_x
            exp.center_y = self.center_y
            self.window.explosions.append(exp)

            left = True
            right = True
            up = True
            down = True

            for i in range(1, self.power):
                if left == True:
                    exp1 = Explosion(self.window)
                    exp1.center_x = self.center_x - constants.CELL_WIDTH * i
                    exp1.center_y = self.center_y
                    self.window.explosions.append(exp1)
                    if exp1.check() == True:
                        left = False

                if right == True:
                    exp2 = Explosion(self.window)
                    exp2.center_x = self.center_x + constants.CELL_WIDTH * i
                    exp2.center_y = self.center_y
                    self.window.explosions.append(exp2)
                    if exp2.check() == True:
                        right = False

                if up == True:
                    exp3 = Explosion(self.window)
                    exp3.center_x = self.center_x
                    exp3.center_y = self.center_y + constants.CELL_HEIGHT * i
                    self.window.explosions.append(exp3)
                    if exp3.check() == True:
                        up = False

                if down == True:
                    exp4 = Explosion(self.window)
                    exp4.center_x = self.center_x
                    exp4.center_y = self.center_y - constants.CELL_HEIGHT * i
                    self.window.explosions.append(exp4)
                    if exp4.check() == True:
                        down = False

            self.kill()



class ExplodableBlock(arcade.Sprite):
    def __init__(self):
        super().__init__("Blocks/ExplodableBlock.png", 1)


class SolidBlock(arcade.Sprite):
    def __init__(self):
        super().__init__("Blocks/SolidBlock.png", 1)

class Explosion(animate.Animate):
    def __init__(self, window):
        super().__init__("Flame/Flame_f00.png", 0.7)
        for i in range(5):
            self.append_texture(arcade.load_texture(f"Flame/Flame_f0{i}.png"))

        self.spawn_time = time.time()
        self.window = window

    def update(self):
        if time.time() - self.spawn_time > 3:
            self.kill()

    def check(self):
        hits = check_for_collision_with_list(self, self.window.solid_blocks)
        """ if len(hits) > 0:
            return True
        else:
            return False
        """
        return len(hits) > 0


class Game(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title)
        self.bg_tile = arcade.load_texture("Blocks/BackgroundTile.png")
        self.win1 = arcade.load_texture("win/win1.png")
        self.win2 = arcade.load_texture("win/win2.png")
        self.draw = arcade.load_texture("win/DRAW.png")

        self.solid_blocks = arcade.SpriteList()
        self.explodable_blocks = arcade.SpriteList()
        self.explosions = arcade.SpriteList()

        self.player1 = BomberMan(self, constants.PLAYER1_SPEED, constants.PLAYER1_BOMB_COUNT, constants.PLAYER1_POWER)
        self.player2 = BomberMan(self, constants.PLAYER2_SPEED, constants.PLAYER2_BOMB_COUNT, constants.PLAYER2_POWER)

        self.player1_bombs = arcade.SpriteList()
        self.player2_bombs = arcade.SpriteList()

        self.game = True

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

        x2 = constants.SCREEN_WIDTH - x
        y2 = constants.SCREEN_HEIGHT - y
        self.player2.set_position(x2, y2)

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
        self.explosions.draw()

        self.player1.draw()
        self.player2.draw()

        self.player1_bombs.draw()
        self.player2_bombs.draw()

        if self.player1.win == True and self.player2.win == True:
            arcade.draw_texture_rectangle(
                constants.SCREEN_WIDTH / 2,
                constants.SCREEN_HEIGHT / 2,
                constants.SCREEN_WIDTH,
                constants.SCREEN_HEIGHT,
                self.draw
            )
            self.game = False
        elif self.player1.win == True:
            arcade.draw_texture_rectangle(
                constants.SCREEN_WIDTH / 2,
                constants.SCREEN_HEIGHT / 2,
                constants.SCREEN_WIDTH,
                constants.SCREEN_HEIGHT,
                self.win1
            )
            self.game = False
        elif self.player2.win == True:
            arcade.draw_texture_rectangle(
                constants.SCREEN_WIDTH / 2,
                constants.SCREEN_HEIGHT / 2,
                constants.SCREEN_WIDTH,
                constants.SCREEN_HEIGHT,
                self.win2
            )
            self.game = False





    def update(self, delta_time: float):
        if self.game == True:
            self.player1.update_animation(delta_time)
            self.player1.update()

            self.player2.update_animation(delta_time)
            self.player2.update()

            self.player1_bombs.update()
            self.player1_bombs.update_animation(delta_time)

            self.player2_bombs.update()
            self.player2_bombs.update_animation(delta_time)

            self.explosions.update()
            self.explosions.update_animation(delta_time)

            for flame in self.explosions:
                touched_exp_blocks = arcade.check_for_collision_with_list(flame, self.explodable_blocks)
                if len(touched_exp_blocks) > 0:
                    for block in touched_exp_blocks:
                        block.kill()

                touched_solid_blocks = arcade.check_for_collision_with_list(flame, self.solid_blocks)
                if len(touched_solid_blocks) > 0:
                    flame.kill()

                if arcade.check_for_collision(flame, self.player1):
                    self.player1.color = (0,0,0)
                    self.player2.win = True

                if arcade.check_for_collision(flame, self.player2):
                    self.player2.color = (0,0,0)
                    self.player1.win = True

    def on_key_press(self, symbol: int, modifiers: int):
        if self.game == True:
            # PLAYER 1
            if symbol == arcade.key.LEFT:
                self.player1.to_left()
            elif symbol == arcade.key.RIGHT:
                self.player1.to_right()
            elif symbol == arcade.key.UP:
                self.player1.to_up()
            elif symbol == arcade.key.DOWN:
                self.player1.to_down()

            if symbol == arcade.key.C:
                if len(self.player1_bombs) < self.player1.bombs_count:
                    bomb = Bomb(self, self.player1.power)
                    bomb.center_x = justify_x(self.player1.center_x)
                    bomb.center_y = justify_y(self.player1.center_y)
                    self.player1_bombs.append(bomb)


            self.player1.change_costume()

            # Player 2
            if symbol == arcade.key.A:
                self.player2.to_left()
            elif symbol == arcade.key.D:
                self.player2.to_right()
            elif symbol == arcade.key.W:
                self.player2.to_up()
            elif symbol == arcade.key.S:
                self.player2.to_down()


            if symbol == arcade.key.RSHIFT:
                if len(self.player2_bombs) < self.player2.bombs_count:
                    bomb = Bomb(self, self.player2.power)
                    bomb.center_x = justify_x(self.player2.center_x)
                    bomb.center_y = justify_y(self.player2.center_y)
                    self.player2_bombs.append(bomb)

                    self.player2.change_costume()


    def on_key_release(self, symbol: int, modifiers: int):
        if symbol == arcade.key.LEFT or arcade.key.RIGHT or arcade.key.DOWN or arcade.key.UP:
            self.player1.to_stop()

        if symbol == arcade.key.A or arcade.key.D or arcade.key.S or arcade.key.W:
            self.player2.to_stop()
