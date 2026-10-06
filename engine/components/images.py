import pygame


class ImageObject:
    def __init__(self, scene, texture, x=0, y=0, anchor='topleft', depth=0):
        self.scene = scene
        self.original_texture = texture
        self.texture = texture
        self.depth = depth
        self.scene_index = 0
        self.scale_x = 1
        self.scale_y = 1
        self.anchor = anchor
        self.rect = self.texture.get_rect()
        setattr(self.rect, self.anchor, (x, y))

        # self.x = x
        # self.y = y

    @property
    def width(self):
        return self.texture.get_width()

    @property
    def height(self):
        return self.texture.get_height()

    @property
    def x(self):
        return getattr(self.rect, self.anchor)[0]

    @x.setter
    def x(self, value):
        _, y = getattr(self.rect, self.anchor)
        setattr(self.rect, self.anchor, (value, y))

    @property
    def y(self):
        return getattr(self.rect, self.anchor)[1]

    @y.setter
    def y(self, value):
        x, _ = getattr(self.rect, self.anchor)
        setattr(self.rect, self.anchor, (x, value))

    def set_scale(self, *args):
        if len(args) == 1:
            self.scale_x = self.scale_y = args[0]
        elif len(args) == 2:
            self.scale_x, self.scale_y = args

        anchor_pos = getattr(self.rect, self.anchor)

        width = int(self.original_texture.get_width() * self.scale_x)
        height = int(self.original_texture.get_height() * self.scale_y)

        self.texture = pygame.transform.scale(
            self.original_texture, (width, height))

        # Recriar o rect com nova textura
        self.rect = self.texture.get_rect()

        # Reaplicar a posição antiga com base no anchor
        setattr(self.rect, self.anchor, anchor_pos)

    def chroma_key(self, r, g, b):
        self.texture.set_colorkey((r, g, b))

    def set_texture(self, key):
        self.original_texture = self.scene.assets.get_image(key)
        self.texture = self.scene.assets.get_image(key)
        self.chroma_key(0, 116, 116)
        self.set_scale(self.scale_x, self.scale_y)
