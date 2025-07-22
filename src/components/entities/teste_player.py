import pygame
from src.components.collider import Collider
from pygame.math import Vector2


class TestePlayer():
    def __init__(self, x, y, scene):
        self._x = x
        self._y = y
        self.scene = scene
        self.sprite = scene.add_image('mario_idle', x, y, 'midbottom')
        self.position = Vector2(x, y)
        self.velocity = Vector2(0, 0)
        self.direction = Vector2(0, 0)
        self.move_speed = 120  # px/s
        self.is_on_ground = False
        print(self.sprite.height)
        self.hitbox = Collider(x, y, self.sprite.width,
                               self.sprite.height, anchor='midbottom')
        self.jump_force = -210

        self.sprite.chroma_key(0, 116, 116)
        self.state = 'idle'
        self.move_disable = False

        self.jump_time = 0
        self.min_jump_time = 0.1
        self.max_jump_time = 0.25  # em segundos
        self.is_jumping = False

        self.direction_facing = 'left'
        self.face_side = {
            1: self._face_right,
            -1: self._face_left,
        }

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

    def handle_input(self):
        keys = pygame.key.get_pressed()
        left = keys[pygame.K_LEFT] or keys[pygame.K_a]
        right = keys[pygame.K_RIGHT] or keys[pygame.K_d]

        # Cancelamento mútuo
        if left and right:
            self.direction.x = 0
        elif left:
            self.direction.x = -1
        elif right:
            self.direction.x = 1
        else:
            self.direction.x = 0

        if keys[pygame.K_SPACE] and self.is_on_ground:
            self.is_jumping = True
            self.jump_time = 0
            self.velocity.y = self.jump_force

    def apply_physics(self):
        dt = self.scene.game.delta_time
        acceleration = 600  # px/s²
        deceleration = 800  # px/s²
        max_speed = self.move_speed

        # Pulo variável: enquanto segurando e dentro do tempo máximo
        if self.is_jumping:
            self.jump_time += dt
            if self.jump_time >= self.max_jump_time:
                self.is_jumping = False
            elif not pygame.key.get_pressed()[pygame.K_SPACE] and self.jump_time >= self.min_jump_time:
                self.is_jumping = False
            else:
                # Aplica gravidade reduzida (opcional)
                self.velocity.y += self.scene.gravity * 0.2 * dt
        else:
            if not self.is_on_ground:
                self.velocity.y += self.scene.gravity * dt

         # Movimento horizontal com aceleração e desaceleração
        if self.direction.x != 0:
            self.velocity.x += self.direction.x * acceleration * dt
            if abs(self.velocity.x) > max_speed:
                self.velocity.x = max_speed * self.direction.x
        else:
            if self.velocity.x > 0:
                self.velocity.x -= deceleration * dt
                if self.velocity.x < 0:
                    self.velocity.x = 0
            elif self.velocity.x < 0:
                self.velocity.x += deceleration * dt
                if self.velocity.x > 0:
                    self.velocity.x = 0

    def _face_right(self):
        if self.direction_facing != 'right':
            self.direction_facing = 'right'
            self.sprite.texture = pygame.transform.flip(
                self.sprite.texture, True, False)

    def _face_left(self):
        if self.direction_facing != 'left':
            self.direction_facing = 'left'
            self.sprite.texture = self.sprite.texture = pygame.transform.flip(
                self.sprite.texture, True, False)

    def move(self):
        self.face_side.get(int(self.direction.x), lambda: None)()
        # print((int(self.direction.x)))
        dt = self.scene.game.delta_time
        # Aplicar movimento
        self.x += self.velocity.x * dt
        # self.resolve_collisions(tiles, axis='x')

        self.y += self.velocity.y * dt
        # self.resolve_collisions(tiles, axis='y')

    def update(self):
        self.handle_input()
        self.apply_physics()
        self.move()

        self.terrain_collisions()

    def terrain_collisions(self):
        self.is_on_ground = False
        for terrain in self.scene.terrains:
            side = terrain.get_collision_side(self.hitbox)
            if side == 'top' and terrain.is_solid and self.velocity.y >= 0:
                terrain.block_overlap(self.hitbox)
                self._sync_position_from_hitbox()
                self.is_on_ground = True

            if side == 'bottom' and terrain.is_solid and self.velocity.y <= 0:
                terrain.block_overlap(self.hitbox)
                self._sync_position_from_hitbox()
                self.is_jumping = False

                # print('ta no chao')

                # print(side)

    def _sync_position_from_hitbox(self):
        self.x = self.hitbox.x
        self.y = self.hitbox.y
