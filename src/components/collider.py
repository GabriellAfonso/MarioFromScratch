import pygame


class Collider:
    def __init__(self, x, y, width, height, anchor='midbottom'):
        self.area = pygame.Rect(0, 0, width, height)
        setattr(self.area, anchor, (x, y))
        self.anchor = anchor

    @property
    def x(self):
        return getattr(self.area, self.anchor)[0]

    @property
    def y(self):
        return getattr(self.area, self.anchor)[1]

    @x.setter
    def x(self, value):
        _, y = getattr(self.area, self.anchor)
        setattr(self.area, self.anchor, (value, y))

    @y.setter
    def y(self, value):
        x, _ = getattr(self.area, self.anchor)
        setattr(self.area, self.anchor, (x, value))

        # def collides_with(self, other_collider):
        #     return self.area.colliderect(other_collider.rect)

        # def draw_debug(self, surface, color=(0, 255, 0)):
        #     print(
        #         f'Drawing collider at {self.area.topleft} with size {self.area.size}')
        #     pygame.draw.rect(surface, color, self.area, 1)
