import pygame


class AssetManager:
    def __init__(self):
        self.images = {}
        self.sounds = {}

    def load_image(self, key, path):
        surface = pygame.image.load(path).convert()
        self.images[key] = surface

    def get_image(self, key):
        return self.images.get(key)

    def load_sound(self, key, path):
        sound = pygame.mixer.Sound(path)
        self.sounds[key] = sound

    def get_sound(self, key):
        return self.sounds.get(key)
