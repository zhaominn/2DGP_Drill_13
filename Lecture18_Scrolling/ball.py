from pico2d import *

import game_world
import play_mode
import server
import random


class Ball:
    image = None

    def __init__(self, x=None, y=None):
        if Ball.image == None:
            Ball.image = load_image('ball21x21.png')
        self.x = x if x else random.randint(200, 1637)
        self.y = y if y else random.randint(200, 909)
        self.cw = get_canvas_width()
        self.ch = get_canvas_height()
        self.bb = self.x - 10, self.y - 10, self.x + 10, self.y + 10

    def draw(self):
        self.image.draw(self.x-self.window_left, self.y-self.window_bottom)
        draw_rectangle(*self.get_bb())

    def update(self):
        self.window_left = clamp(
            0,
            int(server.boy.x) - self.cw // 2,
            play_mode.server.background.w - self.cw - 1
        )
        self.window_bottom = clamp(
            0,
            int(server.boy.y) - self.ch // 2,
            play_mode.server.background.h - self.ch - 1
        )
        self.bb = self.x-self.window_left - 10, self.y-self.window_bottom-10, self.x-self.window_left + 10, self.y-self.window_bottom + 10

    def get_bb(self):
        return self.bb

    def handle_collision(self, group, other):
        if group == 'boy:balls':
            game_world.remove_object(self)
