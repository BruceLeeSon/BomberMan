import arcade
import animate
import constants


class BomberMan(animate.Animate):
    def __init__(self, window, speed, bombs_count, power):
        super().__init__("Bomberman/Front/Bman_F_f00.png", 0.5)
        self.direction = 4
        self.motion = 0

        self.speed = speed
        self.bombs_count = bombs_count
        self.window = window
        self.power = power

        self.walk_down_frames = []
        self.walk_up_frames = []
        self.walk_left_frames = []
        self.walk_right_frames = []

        for i in range(8):
            self.walk_right_frames.append(
                arcade.load_texture(f"Bomberman/Side/Bman_S_f0{i}.png", flipped_horizontally=False))
            self.walk_down_frames.append(arcade.load_texture(f"Bomberman/Front/Bman_F_f0{i}.png"))
            self.walk_up_frames.append(arcade.load_texture(f"Bomberman/Back/Bman_B_f0{i}.png"))
            self.walk_left_frames.append(
                arcade.load_texture(f"Bomberman/Side/Bman_S_f0{i}.png", flipped_horizontally=True))

    def change_costume(self):
        if self.direction == 1:
            self.textures = self.walk_left_frames
        elif self.direction == 2:
            self.textures = self.walk_right_frames
        elif self.direction == 3:
            self.textures = self.walk_up_frames
        elif self.direction == 4:
            self.textures = self.walk_down_frames

    def update(self):
        self.center_x += self.change_x
        self.center_y += self.change_y

        if self.left < 0:
            self.left = 0

        if self.right > constants.SCREEN_WIDTH:
            self.right = constants.SCREEN_WIDTH

        if self.bottom < 0:
            self.bottom = 0

        if self.top > constants.SCREEN_HEIGHT:
            self.top = constants.SCREEN_HEIGHT

        self.collisions(self.window.solid_blocks)
        self.collisions(self.window.explodable_blocks)


    def collisions(self, sprite_list):
        block_hit = arcade.check_for_collision_with_list(self, sprite_list)
        for block in block_hit:
            if self.left < block.right and self.direction == 1:
                self.left = block.right

            if self.right > block.left and self.direction == 2:
                self.right = block.left

            if self.top > block.bottom and self.direction == 3:
                self.top = block.bottom

            if self.bottom < block.top and self.direction == 4:
                self.bottom = block.top

    def to_up(self):
        if not self.motion:
            self.motion = 1
            self.direction = 3
            self.change_y = self.speed

    def to_left(self):
        if not self.motion:
            self.motion = 1
            self.direction = 1
            self.change_x = -self.speed

    def to_right(self):
        if not self.motion:
            self.motion = 1
            self.change_x = self.speed
            self.direction = 2

    def to_down(self):
        if not self.motion:
            self.motion = 1
            self.direction = 4
            self.change_y = -self.speed

    def to_stop(self):
        self.motion = 0
        self.change_x = 0
        self.change_y = 0
