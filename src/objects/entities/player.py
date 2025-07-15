import pygame


class Player(pygame.sprite.Sprite):
    def __init__(self, x, y, scene):
        super().__init__()
        self.scene = scene
        self.sprite = scene.add_image('mario_idle', x, y)
        self.rect = self.sprite.set_rect()
        self.vx = 5
        self.direction_facing = 'left'
        self.sprite.set_scale(3)
        self.original_image = self.sprite.texture
        self.sprite.chroma_key(0, 116, 116)
        self.state = 'idle'
        self.move_disable = False



    def char_command(self):
        keys = pygame.key.get_pressed()

        try_look_up = keys[pygame.K_w]
        try_duck    = keys[pygame.K_s]
        try_walk      = keys[pygame.K_a] or keys[pygame.K_d]

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

                    self.sprite.rect.x -= self.vx
                    self.sprite.x -= self.vx
            if keys[pygame.K_d]:

                    self.sprite.rect.x += self.vx
                    self.sprite.x += self.vx
        
        elif self.state == 'ducked':
            self.sprite.set_texture('mario_duck')

        if self.direction_facing == 'right':
            self.sprite.texture = pygame.transform.flip(self.sprite.texture, True, False)
        elif self.direction_facing == 'left':
            self.sprite.texture = pygame.transform.flip(self.sprite.texture, True, False)
            self.sprite.texture = pygame.transform.flip(self.sprite.texture, True, False)



    def update(self):

        if not self.check_collision(self.scene.square):
            self.scene.speed_y = min(self.scene.speed_y + self.scene.gravity, self.scene.max_speed_y)
            self.sprite.rect.y += self.scene.speed_y
            self.sprite.y += self.scene.speed_y
        else:
            self.scene.speed_y = 0

        self.char_command()  
        self.char_states()
       
        # self.draw(self.scene.screen)
        
    def draw(self, screen):
        screen.blit(self.sprite.texture, (self.sprite.rect.x, self.sprite.rect.y))

    def check_collision(self, rect):
        return self.sprite.rect.colliderect(rect)
    
