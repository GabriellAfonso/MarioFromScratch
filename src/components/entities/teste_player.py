import pygame
from src.components.collider import Collider


class TestePlayer():
    def __init__(self, x, y, scene):
        self._x = x
        self._y = y
        self.scene = scene
        self.sprite = scene.add_image('mario_idle', x, y, 'midbottom')

        self.vel_x = 5
        self.vel_y = 5
        self.gravity = 100
        self.direction_facing = 'left'
        self.sprite.set_scale(3)
        self.hitbox = Collider(x, y, self.sprite.width,
                               self.sprite.height, anchor='midbottom')
        self.original_image = self.sprite.texture
        self.sprite.chroma_key(0, 116, 116)
        self.state = 'idle'
        self.move_disable = False
        print(f'Player created at ({x}, {y}) with sprite {self.sprite}')

    @property
    def x(self):
        return self._x

    @property
    def y(self):
        return self._y

    @x.setter
    def x(self, value):
        self._x = value
        self.sprite.x = value
        self.hitbox.x = value

    @y.setter
    def y(self, value):
        self._y = value
        self.sprite.y = value
        self.hitbox.y = value

    def char_command(self):
        keys = pygame.key.get_pressed()

        try_look_up = keys[pygame.K_w]
        try_duck = keys[pygame.K_s]
        try_walk = keys[pygame.K_a] or keys[pygame.K_d]

        # 🧍‍♂️ Sai do estado de olhar pra cima se soltou W
        if self.state == 'looking_up' and not try_look_up:
            self.move_disable = False
            if try_walk:
                self.state = 'walking'
            else:
                self.state = 'idle'

        # 🧎 Sai do estado de agachado se soltou S
        elif self.state == 'ducked' and not try_duck:
            self.move_disable = False
            if try_walk:
                self.state = 'walking'
            else:
                self.state = 'idle'

        # 🧎‍♂️ Agachar tem prioridade
        elif try_duck:
            self.state = 'ducked'
            self.move_disable = True

        # 👆 Olhar cima vem depois
        elif try_look_up:
            self.state = 'looking_up'
            self.move_disable = True

        # 🚶 Andar, só se não estiver travado
        elif try_walk and not self.move_disable:
            self.state = 'walking'

        # 💤 Ninguém tá fazendo nada
        else:
            self.state = 'idle'
            self.move_disable = False

    def char_states(self):

        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]:
            self.direction_facing = 'left'
        if keys[pygame.K_d]:
            self.direction_facing = 'right'

        if self.state == 'idle':
            self.sprite.set_texture('mario_idle')

        elif self.state == 'looking_up':
            self.sprite.set_texture('mario_look_up')

        elif self.state == 'walking':
            self.sprite.set_texture('mario_walking')
            if keys[pygame.K_a]:
                self.x -= self.vel_x
            if keys[pygame.K_d]:
                self.x += self.vel_x

        elif self.state == 'ducked':
            self.sprite.set_texture('mario_duck')

        if keys[pygame.K_LEFT]:
            self.scene.main_camera.scroll_x -= self.vel_x
        if keys[pygame.K_RIGHT]:
            self.scene.main_camera.scroll_x += self.vel_x

        if self.direction_facing == 'right':
            self.sprite.texture = pygame.transform.flip(
                self.sprite.texture, True, False)
        elif self.direction_facing == 'left':
            self.sprite.texture = pygame.transform.flip(
                self.sprite.texture, False, False)

        if keys[pygame.K_w]:
            self.y -= self.vel_y
        if keys[pygame.K_s]:
            self.y += self.vel_y

    def update(self):

        # if not self.check_collision(self.scene.square.area):
        #     # Considera que self.sprite.y representa a base (pés)
        #     if self.sprite.y < self.scene.square.area.y:
        #         diff = self.scene.square.area.y - self.sprite.y
        #         v = min(self.vel_y, diff)
        #         self.sprite.y += v
        #         self.hitbox.area.bottom = round(self.sprite.y)

        self.char_command()
        self.char_states()
        # self.terrain_collisions()

    def terrain_collisions(self):
        pass

    def check_collision(self, rect):
        return self.hitbox.area.colliderect(rect)
