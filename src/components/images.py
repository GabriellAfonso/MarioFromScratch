import pygame
from src.core.settings import ASSETS


class ImageObject:
    def __init__(self, texture, x=0, y=0, anchor='topleft', depth=0):
        self.original_texture = texture
        self.texture = texture
        self.width = texture.get_width()
        self.height = texture.get_height()
        self.x = x
        print(self.x)
        self.y = y
        self.depth = depth
        self.scene_index = 0
        self.scale_x = 1
        self.scale_y = 1
        self.anchor = anchor
        self.rect = self.set_rect()

    def set_rect(self):
        rect = self.texture.get_rect(topleft=(self.x, self.y))
        # setattr(rect, self.anchor, (self.x, self.y))
        print(rect.x, rect.y)
        return rect

    def set_scale(self, *args):
        if len(args) == 1:
            self.scale_x = self.scale_y = args[0]
        elif len(args) == 2:
            self.scale_x, self.scale_y = args

        width = int(self.original_texture.get_width() * self.scale_x)
        height = int(self.original_texture.get_height() * self.scale_y)

        self.texture = pygame.transform.scale(
            self.original_texture, (width, height))
        if self.rect:
            self.rect.size = (self.rect.width * self.scale_x,
                              self.rect.height * self.scale_y)

    def chroma_key(self, r, g, b):
        self.texture.set_colorkey((r, g, b))

    def set_texture(self, key):
        self.original_texture = ASSETS['images'][key]
        self.texture = ASSETS['images'][key]
        self.chroma_key(0, 116, 116)
        self.rect = self.set_rect()
        self.set_scale(self.scale_x, self.scale_y)
