import pygame
from src.core.settings import ASSETS

class ImageObject:
    def __init__(self, texture, x=0, y=0, depth=0):
        self.original_texture = texture

        self.texture = texture
        self.x = x
        self.y = y
        self.depth = depth
        self.scene_index = 0
        self.scale_x = 1
        self.scale_y = 1
        self.rect = None

    def set_rect(self):
        #center = self.rect.center
        #print(center)
        self.rect = self.texture.get_rect(center=(self.x, self.y))
        return self.rect

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
            self.rect.size = (self.rect.width * self.scale_x, self.rect.height * self.scale_y)

    def chroma_key(self, r, g, b):
        self.texture.set_colorkey((r, g, b))

    def set_texture(self, key):
        self.original_texture = ASSETS['images'][key]
        self.texture = ASSETS['images'][key]
        self.chroma_key(0, 116, 116)
        self.rect = None
        self.set_scale(self.scale_x, self.scale_y)
        self.set_rect()
    