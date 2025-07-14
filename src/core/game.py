import pygame
from src.core.scenes import SceneManager, BaseScene
from src.scenes.game_scene import GameScene
from src.scenes.teste_scene import TesteScene
from src.scenes.loading import LoadingScene


class Game:
    def __init__(self, width=800, height=600, fps=60):
        pygame.init()
        pygame.display.set_caption("Mario From Scratch")
        self.screen = pygame.display.set_mode((width, height))

        self.clock = pygame.time.Clock()
        self.fps = fps
        self.running = True

        self.scene_manager = SceneManager(self)
        self.scene_manager.register('loading', LoadingScene)
        self.scene_manager.register('game_scene', GameScene)
        self.scene_manager.register('teste_scene', TesteScene)
        self.scene_manager.run('loading')

    def run(self):
        while self.running:
            self.clock.tick(self.fps)
            scenes = self.scene_manager.active_scenes

            # eventos: apenas a cena do topo recebe eventos
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                elif scenes:
                    scenes[-1].handle_events(event)

            # update: todas as cenas são atualizadas
            for scene in scenes:
                scene.update()

            # render: todas as cenas são desenhadas em ordem
            self.screen.fill((0, 0, 0))  # Limpa tela
            for scene in scenes:
                scene.render()

            pygame.display.flip()

        pygame.quit()
