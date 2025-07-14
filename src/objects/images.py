import pygame


class ImageObject:
    def __init__(self, surface, x=0, y=0, depth=0):
        self.original_surface = surface

        self.surface = surface
        self.x = x
        self.y = y
        self.depth = depth
        self.scene_index = 0
        self.scale_x = 1
        self.scale_y = 1
        self.rect = None

    def set_scale(self, *args):
        if len(args) == 1:
            self.scale_x = self.scale_y = args[0]
        elif len(args) == 2:
            self.scale_x, self.scale_y = args

        width = int(self.original_surface.get_width() * self.scale_x)
        height = int(self.original_surface.get_height() * self.scale_y)

        self.surface = pygame.transform.scale(
            self.original_surface, (width, height))

    def chroma_key(self, r, g, b):
        self.surface.set_colorkey((r, g, b))
