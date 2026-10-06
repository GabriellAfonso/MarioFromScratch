import pygame
from .scene_manager import SceneManager
from .asset_manager import AssetManager
from pygame._sdl2 import Window


class Core:
    def __init__(self, config):
        self.config = config
        pygame.init()
        pygame.mixer.init()
        pygame.display.set_caption(config.title)
        self.assets = AssetManager()
        self.screen = pygame.display.set_mode(
            (config.width, config.height), pygame.SRCALPHA | pygame.HWSURFACE | pygame.DOUBLEBUF | pygame.SCALED | pygame.RESIZABLE)

        self.clock = pygame.time.Clock()
        self.fps = config.fps
        self.running = True

        self.scene_manager = self.set_scene_manager(config.scenes)
        self.start_first_scene()

    def set_scene_manager(self, scenes):
        scene_manager = SceneManager(self)
        for key, scene in scenes.items():
            scene_manager.register(key, scene)
        return scene_manager

    def start_first_scene(self):
        scenes = self.scene_manager.scenes
        first = next(iter(scenes))
        self.scene_manager.run(first)

    def run(self):
        while self.running:
            self.delta_time = self.clock.tick(self.fps) / 1000.0

            scenes = self.scene_manager.active_scenes

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
