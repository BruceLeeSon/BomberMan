import arcade
import animate

class BomberMan(animate.Animate):
    def __init__(self):
        super().__init__("Bomberman/Front/Bman_F_f00.png", 0.5)
        self.direction = 4

        self.walk_down_frames = []
        self.walk_up_frames = []
        self.walk_left_frames = []
        self.walk_right_frames = []

        for i in range(8):
            self.walk_right_frames.append(arcade.load_texture(f"Bomberman/Side/Bman_S_f0{i}.png", flipped_horizontally=False))
            self.walk_down_frames.append(arcade.load_texture(f"Bomberman/Front/Bman_F_f0{i}.png"))
            self.walk_up_frames.append(arcade.load_texture(f"Bomberman/Back/Bman_B_f0{i}.png"))
            self.walk_left_frames.append(arcade.load_texture(f"Bomberman/Side/Bman_S_f0{i}.png", flipped_horizontally=True))

    def change_costume(self):
        if self.direction == 1:
            self.textures = self.walk_left_frames
        elif self.direction == 2:
            self.textures = self.walk_right_frames
        elif self.direction == 3:
            self.textures = self.walk_up_frames
        elif self.direction == 4:
            self.textures = self.walk_down_frames