import pygame
from src.components.collider import Collider


class TestePlayer():
    def __init__(self, x, y, scene):
        self._x = x
        self._y = y
        self.scene = scene
        self.sprite = scene.add_image('mario_idle', x, y, 'midbottom')

        self.vel_x = 5
        self.vel_y = 0
        self.gravity = False
        self.direction_facing = 'left'
        self.sprite.set_scale(3)
        self.hitbox = Collider(x, y, self.sprite.width,
                               self.sprite.height, anchor='midbottom')
        self.original_image = self.sprite.texture
        self.sprite.chroma_key(0, 116, 116)
        self.state = 'idle'
        self.move_disable = False
        self.is_on_ground = False

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
        try_jump = keys[pygame.K_SPACE]
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

        elif try_jump and not self.move_disable and not self.state == 'air':
            self.state = 'jumping'

        # 💤 Ninguém tá fazendo nada
        # else:
        #     self.state = 'idle'
        #     self.move_disable = False

    def char_states(self):

        keys = pygame.key.get_pressed()
        if self.state == 'air':
            return

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

        elif self.state == 'jumping':
            self.state = 'air'
            if keys[pygame.K_SPACE] and self.is_on_ground:

                self.sprite.set_texture('mario_idle')

                self.vel_y = - 733

        if keys[pygame.K_w]:
            self.y -= 10
        if keys[pygame.K_s]:
            self.y += 10

        if self.direction_facing == 'right':
            print('flipou pra direita')
            self.sprite.texture = pygame.transform.flip(
                self.sprite.texture, True, False)
        elif self.direction_facing == 'left':
            print('flipou pra esquerda')
            self.sprite.texture = pygame.transform.flip(
                self.sprite.texture, False, False)

    def update(self):
        print(self.state)
        if not self.is_on_ground:
            self.vel_y += self.scene.gravity * self.scene.game.delta_time

        self.y += self.vel_y * self.scene.game.delta_time

        self.char_command()
        self.char_states()
        self.terrain_collisions()

    def terrain_collisions(self):
        self.is_on_ground = False
        for terrain in self.scene.terrains:
            if terrain.get_collision_side(self.hitbox):
                if terrain.is_solid:
                    side = terrain.get_collision_side(self.hitbox)
                    terrain.block_overlap(self.hitbox)
                    self._sync_position_from_hitbox()
                    if side == 'top':
                        self.is_on_ground = True
                        # print('ta no chao')

                    # print(side)

    def _sync_position_from_hitbox(self):
        self.x = self.hitbox.x
        self.y = self.hitbox.y

    # def is_on_ground(self):
    #     for terrain in self.scene.terrains:
    #         print(terrain.get_collision_side(self.hitbox))
    #         if terrain.get_collision_side(self.hitbox) == 'top':
    #             return True
    #     return False
