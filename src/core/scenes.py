import pygame
from abc import ABC, abstractmethod
from src.core.settings import ASSETS
from src.objects.images import ImageObject


class BaseScene(ABC):
    def __init__(self, game):
        self.name = None
        self.game = game
        self.screen = game.screen
        self.insertion_index = 0
        self.render_list = []
        self.preload()
        self.create()

    def preload(self):
        pass

    def handle_events(self, event):
        pass

    @abstractmethod
    def create(self):
        pass

    @abstractmethod
    def update(self):
        pass

    def render(self):
        # print(self.name, self.render_list)

        self.render_list.sort(key=lambda obj: (obj.depth, obj.scene_index))
        for obj in self.render_list:
            if obj.rect:
                self.screen.blit(obj.texture, obj.rect)
                continue
            self.screen.blit(obj.texture, (obj.x, obj.y))
        pass

    def load_audio(self, key, path):
        sound = pygame.mixer.Sound(path)
        ASSETS['audio'][key] = sound

    def add_audio(self, key):
        sound = ASSETS['audio'][key]
        return sound

    def load_image(self, key, path):
        surface = pygame.image.load(path).convert()
        ASSETS['images'][key] = surface

    def add_image(self, key, x, y):
        
        surface = ASSETS['images'][key]
        image = ImageObject(surface, x, y)
        self.insertion_index += 1
        image.scene_index = self.insertion_index
        self.render_list.append(image)
        print(self.render_list)
        self.render()
        return image


class SceneManager:
    def __init__(self, game):
        self.game = game
        self.scenes = {}  # Registro: key -> classe
        self.active_scenes = []
        self.next_scene = None

    def register(self, key, scene_cls):
        self.scenes[key] = scene_cls

    def start(self, key):
        # Troca a cena atual por uma nova
        self.active_scenes = [self.scenes[key](self.game)]
        if self.next_scene:
            self.active_scenes = [self.scenes[self.next_scene](self.game)]

    def run(self, key):
        # Adiciona nova cena ao topo (como overlay)
        scene = self.scenes[key](self.game)
        self.active_scenes.append(scene)

    def stop(self, key):
        self.active_scenes = [
            s for s in self.active_scenes if s.__class__.__name__ != key
        ]

    def current(self):
        if self.active_scenes:
            return self.active_scenes[-1]
        return None
