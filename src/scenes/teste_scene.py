import pygame
from src.core.base_scene import BaseScene
from src.components.entities.teste_player import TestePlayer


class TesteScene(BaseScene):
    def __init__(self, game):
        super().__init__(game)
        self.name = 'TesteScene'

    def create(self):
        print('TesteScene created')
        self.map = self.add_image('yoshis_island2', 0, 720, 'bottomleft')
        self.map.set_scale(3)
        self.mario = TestePlayer(30, 40, self)
        self.square = pygame.Rect(0, 640, 200, 5)
        self.main_camera.add_object(self.square)

        self.music = self.add_audio('overworld_theme')
        self.music.play(-1)

    def handle_events(self, event):
        pass

    def render(self):
        super().render()
        # print(self.map.rect.x)
        pygame.draw.rect(self.screen, (255, 0, 0), self.square)
        # self.screen.blit(self.map.texture, self.map.rect)
        # pygame.draw.rect(self.screen, (255, 0, 0), self.mario.sprite.rect)

    def update(self):
        self.mario.update()

        pass
