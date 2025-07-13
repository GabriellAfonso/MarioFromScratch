from abc import ABC, abstractmethod



class BaseScene(ABC):
    def __init__(self, game, screen):
        self.game = game
        self.screen = screen

    @abstractmethod
    def handle_events(self, event):
        pass

    @abstractmethod
    def update(self):
        pass

    @abstractmethod
    def render(self, screen):
        pass


class SceneManager:
    def __init__(self):
        self.scene = None

    def go_to(self, scene):
        self.scene = scene
