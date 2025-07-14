from src.core.scenes import BaseScene
from src.scenes.teste_scene import TesteScene


class LoadingScene(BaseScene):
    def __init__(self, game):

        self.characters_path = 'assets/sprites/characters/'
        self.phases_path = 'assets/sprites/phases/'
        super().__init__(game)
        self.name = 'LoadingScene'

    def preload(self):
        print('Loading assets...')
        self.load_image('yoshis_island2',
                        f'{self.phases_path}yoshis_island_2.png')
        self.load_image('mario_idle', f'{self.characters_path}mario/idle.png')
        self.load_image('mario_duck', f'{self.characters_path}mario/duck.png')
        self.load_image('mario_look_up',
                        f'{self.characters_path}mario/look_up.png')

    def create(self):
        print('LoadingScene created')
        # self.game.scene_manager.next_scene = 'teste_scene'
        self.game.scene_manager.run('teste_scene')
        pass

    def update(self):
        return super().update()
