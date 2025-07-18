import pygame


class Collider:
    def __init__(self, x, y, width, height, anchor='midbottom'):
        self.area = pygame.Rect(0, 0, width, height)
        setattr(self.area, anchor, (x, y))

    def collides_with(self, other_collider):
        return self.area.colliderect(other_collider.rect)

    def draw_debug(self, surface, color=(0, 255, 0)):
        print(
            f'Drawing collider at {self.area.topleft} with size {self.area.size}')
        pygame.draw.rect(surface, color, self.area, 1)
