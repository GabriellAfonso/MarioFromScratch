import pygame


class Collider:
    def __init__(self, x, y, width, height, anchor='midbottom', is_solid=False):
        self.area = pygame.Rect(0, 0, width, height)
        setattr(self.area, anchor, (x, y))
        self.anchor = anchor
        self.is_solid = is_solid

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

    def get_collision_side(self, other):
        if not self.area.colliderect(other.area):
            return None

        # Calcula as diferenças entre os lados
        dx_left = abs(self.area.right - other.area.left)
        dx_right = abs(self.area.left - other.area.right)
        dy_top = abs(self.area.bottom - other.area.top)
        dy_bottom = abs(self.area.top - other.area.bottom)

        # Encontra a menor penetração
        min_dx = min(dx_left, dx_right)
        min_dy = min(dy_top, dy_bottom)

        if min_dx < min_dy:
            return 'right' if dx_left < dx_right else 'left'
        else:
            return 'bottom' if dy_top < dy_bottom else 'top'

    def block_overlap(self, other):
        if not self.area.colliderect(other.area):
            return

        side = self.get_collision_side(other)

        if side == 'left':
            other.area.right = self.area.left
        elif side == 'right':
            other.area.left = self.area.right
        elif side == 'top':
            other.area.bottom = self.area.top
        elif side == 'bottom':
            other.area.top = self.area.bottom
