import pygame


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
