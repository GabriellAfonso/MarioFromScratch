from src.core.scenes import BaseScene


class TesteScene(BaseScene):
    def __init__(self, game):
        super().__init__(game)
        self.name = 'TesteScene'

    def create(self):
        print('TesteScene created')
        self.add_image('yoshis_island2', 0, 0)
        # self.game.scene_manager.stop('loading')

    def handle_events(self, event):
        # implementação concreta
        pass

    def update(self):
        # implementação concreta
        pass
