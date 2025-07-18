import pygame
from abc import ABC, abstractmethod
from src.core.settings import ASSETS
from src.components.images import ImageObject
from src.components.camera import Camera


class BaseScene(ABC):
    def __init__(self, game):
        self.name = None
        self.game = game
        self.main_camera = Camera(self.game.width, self.game.height)
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
        self.render_list.sort(key=lambda obj: (obj.depth, obj.scene_index))
        for obj in self.render_list:
            draw_x = obj.x - self.main_camera.offset.x
            draw_y = obj.y - self.main_camera.offset.y

            if obj.rect:
                # print(obj.rect.x, draw_x)
                draw_rect = obj.rect.copy()

                setattr(draw_rect, obj.anchor, (draw_x, draw_y))
                # draw_rect.topleft = ((draw_x), draw_y)
                self.screen.blit(obj.texture, draw_rect)
                # pygame.draw.rect(self.screen, (255, 0, 0), draw_rect,)
                # print('object tem rect')
            else:
                print(f"Object {obj} has no rect defined.")
                # print(f"Object {obj} has no rect defined.")
                self.screen.blit(obj.texture, (draw_x, draw_y))

    def load_audio(self, key, path):
        sound = pygame.mixer.Sound(path)
        ASSETS['audio'][key] = sound

    def add_audio(self, key):
        sound = ASSETS['audio'][key]
        return sound

    def load_image(self, key, path):
        surface = pygame.image.load(path).convert()
        ASSETS['images'][key] = surface

    def add_image(self, key, x, y, anchor='topleft'):
        print(key)
        surface = ASSETS['images'][key]
        image = ImageObject(surface, x, y, anchor)
        self.insertion_index += 1
        image.scene_index = self.insertion_index
        self.render_list.append(image)
        # print(self.render_list)
        # self.render()
        self.main_camera.add_object(image)
        return image

    # TODO: Implementar a adição de hitboxes
    def add_hitbox(self, x, y, width, height):
        hitbox = pygame.Rect(x, y, width, height)
        self.main_camera.add_object(hitbox)
        return hitbox
