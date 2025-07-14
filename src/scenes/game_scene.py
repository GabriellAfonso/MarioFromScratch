import pygame
from ..core.scenes import BaseScene
from ..core.entity import Entity
from ..core.settings import BASE_DIR
import os


class GameScene(BaseScene):
    def __init__(self, game):
        print('AAAAAAQUI', os.getcwd())
        super().__init__(game)
        self.font = pygame.font.SysFont(None, 48)
        personagem_img = pygame.image.load(
            'assets/sprites/characters/mario/idle.png').convert()

        original_size = personagem_img.get_size()

        scale_factor = 4
        new_size = (int(original_size[0] * scale_factor),
                    int(original_size[1] * scale_factor))
        scaled_image = pygame.transform.scale(personagem_img, new_size)

        self.char = Entity(250, 400, scaled_image)

    def handle_events(self, event):
        # implementação concreta
        pass

    def create(self):
        pass

    def update(self):
        self.char.update()

    def render(self):
        self.screen.fill((0, 0, 0))

        self.char.draw(self.screen)
