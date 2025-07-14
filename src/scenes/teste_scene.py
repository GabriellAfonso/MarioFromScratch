from src.core.scenes import BaseScene
from src.core.entity import Entity


class TesteScene(BaseScene):
    def __init__(self, game):
        super().__init__(game)
        self.name = 'TesteScene'

    def create(self):
        print('TesteScene created')
        self.map = self.add_image('yoshis_island2', 0, 80)
        self.mario = self.add_image('mario_idle', 0, 0)
        self.map.set_scale(1.5)
        self.mario.set_scale(2.5)

        self.music = self.add_audio('overworld_theme')
        self.music.play(-1)

    def handle_events(self, event):
        pass

    def update(self):

        pass
