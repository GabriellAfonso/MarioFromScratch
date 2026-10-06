from engine.base_scene import BaseScene


class LoadingScene(BaseScene):
    def __init__(self, core):

        self.characters_path = 'mario/assets/sprites/characters/'
        self.phases_path = 'mario/assets/sprites/phases/'
        super().__init__(core)
        self.name = 'LoadingScene'

    def preload(self):
        print('Loading assets...')
        self.assets.load_image('yoshis_island2',
                               f'{self.phases_path}yoshis_island_2.png')
        self.assets.load_image(
            'mario_idle', f'{self.characters_path}mario/idle.png')
        self.assets.load_image(
            'mario_duck', f'{self.characters_path}mario/duck.png')
        self.assets.load_image('mario_look_up',
                               f'{self.characters_path}mario/look_up.png')
        self.assets.load_image('mario_walking',
                               f'{self.characters_path}mario/walk1.png')
        self.assets.load_sound('overworld_theme',
                               'mario/assets/musics/overworld_theme.ogg')

    def create(self):
        print('LoadingScene created')
        # self.core.scene_manager.next_scene = 'teste_scene'
        self.core.scene_manager.run('teste_scene')
        pass

    def update(self):
        return super().update()
