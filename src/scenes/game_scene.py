import pygame
from ..core.scenes import BaseScene
from ..core.entity import Entity
from ..core.settings import BASE_DIR
import os

class GameScene(BaseScene):
    def __init__(self, game, screen):
        print('AAAAAAQUI', os.getcwd())
        super().__init__(game, screen)
        self.font = pygame.font.SysFont(None, 48)
        personagem_img = pygame.image.load ('assets/sprites/idle.png').convert()
        
        original_size = personagem_img.get_size()

        scale_factor = 4
        new_size = (int(original_size[0] * scale_factor), int(original_size[1] * scale_factor))
        scaled_image = pygame.transform.scale(personagem_img, new_size)

        self.char = Entity(250, 400, scaled_image)

    def handle_events(self, event):
        # implementação concreta
        pass

    def update(self):
        self.char.update()
        self.char.draw(self.screen)

    def render(self, screen):
        screen.fill((0, 0, 0))  # Fundo preto
        text = self.font.render(
            'Daniel é muito maneiro', True, (255, 255, 255))
        screen.blit(text, (50, 100))
        
        self.char.draw(screen)
        self.screen = screen