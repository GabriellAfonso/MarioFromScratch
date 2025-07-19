import pygame
from abc import ABC, abstractmethod
from src.core.asset_manager import AssetManager
from src.components.images import ImageObject
from src.components.camera import Camera


class BaseScene(ABC):
    def __init__(self, game):
        self.name = None
        self.game = game
        self.main_camera = Camera(self.game.width, self.game.height)
        self.assets = game.assets
        self.screen = game.screen
        self.insertion_index = 0
        self.render_list = []
        self.terrains = []
        self.entities = []
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
                draw_rect = obj.rect.copy()
                setattr(draw_rect, obj.anchor, (draw_x, draw_y))

                self.screen.blit(obj.texture, draw_rect)

                # ver rect das imagens criadas
                pygame.draw.rect(self.screen, (250, 0, 0),
                                 draw_rect, width=1)
            # ver rect dos terrenos
        for terrain in self.terrains:
            ter_x = terrain.x - self.main_camera.offset.x
            ter_y = terrain.y - self.main_camera.offset.y
            area = terrain.area.copy()
            setattr(area, terrain.anchor, (ter_x, ter_y))
            pygame.draw.rect(self.screen, (0, 0, 250), area, width=10)

        for entity in self.entities:
            hitbox = entity.hitbox
            ent_x = hitbox.x - self.main_camera.offset.x
            ent_y = hitbox.y - self.main_camera.offset.y
            area = hitbox.area.copy()
            setattr(area, hitbox.anchor, (ent_x, ent_y))
            pygame.draw.rect(self.screen, (0, 250, 0), area, width=1)

    def add_sound(self, key):
        sound = self.assets.get_sound(key)
        return sound

    def add_image(self, key, x, y, anchor='topleft'):
        surface = self.assets.get_image(key)
        image = ImageObject(self, surface, x, y, anchor)
        self.insertion_index += 1
        image.scene_index = self.insertion_index
        self.render_list.append(image)
        self.main_camera.add_object(image)
        return image

    # TODO: Implementar a adição de hitboxes
    def add_hitbox(self, x, y, width, height):
        hitbox = pygame.Rect(x, y, width, height)
        self.main_camera.add_object(hitbox)
        return hitbox
