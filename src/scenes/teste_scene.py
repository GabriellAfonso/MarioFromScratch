import pygame
from src.core.base_scene import BaseScene
from src.components.entities.teste_player import TestePlayer
from src.components.collider import Collider


class TesteScene(BaseScene):
    def __init__(self, game):
        super().__init__(game)
        self.name = 'TesteScene'

    def create(self):

        self.gravity = 1200
        self.square = Collider(0, 720, 720, 140, 'bottomleft', is_solid=True)
        self.terrains.append(self.square)

        print('TesteScene created')
        self.map = self.add_image('yoshis_island2', 0, 720, 'bottomleft')
        self.map.set_scale(3)
        self.mario = TestePlayer(30, 40, self)
        self.entities.append(self.mario)
        self.main_camera.add_object(self.square)

        # self.music = self.add_audio('overworld_theme')
        # self.music.play(-1)

    def handle_events(self, event):
        pass

    def render(self):
        super().render()
        # pygame.draw.rect(self.screen, (0, 0, 250),
        #                  self.mario.hitbox.area, width=1)

    def update(self):
        self.mario.update()
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.main_camera.scroll_x -= 5
        if keys[pygame.K_RIGHT]:
            self.main_camera.scroll_x += 5

        pass
