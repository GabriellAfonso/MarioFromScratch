import pygame


class Camera:
    def __init__(self, width, height):
        self.offset = pygame.Vector2(0, 0)
        self.width = width
        self.height = height
        self.objects = []

    def add_object(self, obj):
        self.objects.append(obj)
        print(f"Object added to camera: {obj}")

    @property
    def scroll_x(self):
        return self.offset.x

    @scroll_x.setter
    def scroll_x(self, value):
        self.offset.x = value

    @property
    def scroll_y(self):
        return self.offset.y

    @scroll_y.setter
    def scroll_y(self, value):
        self.offset.y = value
