import pygame
from ..core.scenes import BaseScene


class GameScene(BaseScene):
    def __init__(self, game):
        super().__init__(game)
        self.font = pygame.font.SysFont(None, 48)

    def handle_events(self, event):
        # implementação concreta
        pass

    def update(self):
        # implementação concreta
        pass

    def render(self, screen):
        screen.fill((0, 0, 0))  # Fundo preto
        text = self.font.render(
            "Mario Clone - Em desenvolvimento", True, (255, 255, 255))
        screen.blit(text, (50, 100))
