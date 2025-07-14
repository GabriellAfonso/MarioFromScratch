import pygame


class Entity(pygame.sprite.Sprite):
    def __init__(self, x, y, image):
        super().__init__()
        image.set_colorkey((0, 116, 116))
        self.original_image = image
        self.image = image
        self.rect = self.image.get_rect(topleft=(x, y))
        self.vx = 0
        self.vy = 0
        self.alive = True
        self.facing_right = True

    def update(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]:
            self.rect.x -= 5
            if not self.facing_right:
                self.image = self.original_image
                self.facing_right = True

        if keys[pygame.K_d]:
            self.rect.x += 5
            if self.facing_right:
                self.image = pygame.transform.flip(self.image, True, False)
                self.facing_right = False

        if keys[pygame.K_s]:
            self.rect.y += 5

        if keys[pygame.K_w]:
            self.rect.y -= 5

    def draw(self, screen):
        screen.blit(self.image, self.rect)

    def check_collision(self, other):
        return self.rect.colliderect(other.rect)
