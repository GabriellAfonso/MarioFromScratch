import pygame
from src.components.collider import Collider 


class Player(pygame.sprite.Sprite):
    def __init__(self, x, y, scene):
        self._x = x
        self._y = y
        self.scene = scene
        self.sprite = scene.add_image('mario_idle', 0, 60, 'midbottom')

        self.moving = False
        self.start_time = None

        self.vel_x = 5
        self.vel_y = 5
        self.gravity = 100

        self.direction_facing = 'left'
        self.sprite.set_scale(3)

        self.hitbox = Collider(x, y, self.sprite.width, self.sprite.height, anchor='midbottom')
        
        self.sprite.chroma_key(0, 116, 116)
        self.state = 'idle'
        self.move_disable = False

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

       
        if self.state == 'looking_up' and not try_look_up:
            self.move_disable = False
            if try_walk:
                self.state = 'walking'
            else:
                self.state = 'idle'

        elif self.state == 'ducked' and not try_duck:
            self.move_disable = False
            if try_walk:
                self.state = 'walking'
            else:
                self.state = 'idle'

        elif try_duck:
            self.state = 'ducked'
            self.move_disable = True

        elif try_look_up and not try_walk:
            self.state = 'looking_up'
            self.move_disable = False

        elif  try_walk and not self.move_disable:
            self.state = 'walking'

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
            self.moving = False
            self.sprite.set_texture('mario_idle')

        elif self.state == 'looking_up':
            self.sprite.set_texture('mario_look_up')

        elif self.state == 'walking':
            self.sprite.set_texture('mario_walking')
            if keys[pygame.K_a]:
                self.x -= self.acceleration(0.5, 5, 2)
            if keys[pygame.K_d]:
                self.x += self.acceleration(0.5, 5, 2)
            
        elif self.state == 'ducked':
            self.sprite.set_texture('mario_duck')

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

        
        if keys[pygame.K_LEFT]:
            self.scene.main_camera.scroll_x -= self.vel_x
        if keys[pygame.K_RIGHT]:
            self.scene.main_camera.scroll_x += self.vel_x

    def check_terrain_collision(self):
        for terrain in self.scene.terrains:
            if self.hitbox.y == terrain.y and self.check_collision(terrain.area):
                print('colidido')
                self.vel_y = 0
            else:
                print('Descoliddo')
                self.vel_y = 5

    def acceleration(self, power, max_sp, min_sp=0, timing=100):
        if not self.moving:
            self.vel = min_sp
            self.moving = True
            self.start_time = pygame.time.get_ticks()
        time_diff = pygame.time.get_ticks() - self.start_time
        if time_diff >= timing:
            self.vel += power
        if self.vel >= max_sp:
            self.vel = max_sp
        return self.vel



    def update(self): 

        #if not self.check_collision(self.scene.square):
            # Considera que self.sprite.y representa a base (pés)
         #   if self.sprite.y < self.scene.square.y:
          #      diff = self.scene.square.y - self.sprite.y
           #     v = min(self.vel_y, diff)
            #    self.sprite.y += v
             #   self.sprite.rect.bottom = round(self.sprite.y)

        self.char_command()
        self.char_states()
        self.check_terrain_collision()
    def draw(self, screen):
        screen.blit(self.sprite.texture,
                    (self.sprite.rect.x, self.sprite.rect.y))

    def check_collision(self, rect):
        return self.hitbox.area.colliderect(rect)
