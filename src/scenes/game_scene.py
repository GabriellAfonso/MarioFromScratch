import pygame
from ..core.scenes import BaseScene
from ..core.settings import BASE_DIR
from src.objects.entities.player import Player
import os


class GameScene(BaseScene):
    def __init__(self, game):
        self.mario = None
        super().__init__(game)
        self.mario = Player(0, 0, self)

    def handle_events(self, event):
        # implementação concreta
        pass

    def create(self):
        self.gravity = 1.1
        self.speed_y = 0
        self.max_speed_y = 10
        self.square = pygame.Rect(0, 640, 1080, 5)


        self.map = self.add_image('yoshis_island2', 0, -512)
        self.map.set_scale(3)

        self.music = self.add_audio('overworld_theme')
        self.music.play(-1)

    def render(self):
        super().render()

    def update(self):

        if self.mario:
            self.mario.update()
