import pygame
from src.core.base_scene import BaseScene
from ..core.settings import BASE_DIR
from src.components.entities.player import Player
import os
from src.components.camera import Camera
from src.components.collider import Collider 


class GameScene(BaseScene):
    def __init__(self, game):
        self.mario = None
        super().__init__(game)
        self.mario = Player(60, 0, self)

    def handle_events(self, event):
        # implementação concreta
        pass

    def create(self):
        # self.camera.apply(self.mario)
        self.gravity = 1.1
        self.speed_y = 0
        self.max_speed_y = 10
        
        self.terrain = Collider(0, 640, 1080, 200, 'topleft')
        self.terrains.append(self.terrain)



        self.map = self.add_image('yoshis_island2', 0, -512)
        self.map.set_scale(3)

        self.music = self.add_sound('overworld_theme')
        self.music.play(-1)

    def render(self):
        super().render()
 

    def update(self):

        if self.mario:
            self.mario.update()
            # self.camera.update(self.mario)
