import pygame
from src.core.scenes import SceneManager, BaseScene
from src.scenes.game_scene import GameScene


class Game:
    def __init__(self, width=800, height=600, fps=60):
        pygame.init()
        self.screen = pygame.display.set_mode((width, height))
        pygame.display.set_caption("Mario From Scratch")
        self.clock = pygame.time.Clock()
        self.fps = fps
        self.running = True

        self.scene_manager = SceneManager()
        self.scene_manager.go_to(GameScene(self, self.screen))  # Inicia com a cena do jogo

    def run(self):
        while self.running:
            self.clock.tick(self.fps)

            # Eventos
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                else:
                    self.scene_manager.scene.handle_events(event)

            # Atualização
            self.scene_manager.scene.update()

            # Renderização
            self.scene_manager.scene.render(self.screen)

            pygame.display.flip()

        pygame.quit()
