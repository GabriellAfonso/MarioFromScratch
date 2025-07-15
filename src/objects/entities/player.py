import pygame


class Player(pygame.sprite.Sprite):
    def __init__(self, x, y, scene):
        super().__init__()
        self.scene = scene
        self.sprite = scene.add_image('mario_idle', x, y)
        self.rect = self.sprite.set_rect()
        self.vx = 5
        self.facing_right = True
        self.sprite.set_scale(3)
        self.original_image = self.sprite.texture
        self.sprite.chroma_key(0, 116, 116)
        self.state = 'idle'
        self.move_disable = False

    def move(self):

        keys = pygame.key.get_pressed()
        
        if keys[pygame.K_w] and not self.state == 'looking_up':
            self.state = 'looking_up'
            self.move_disable = True
            self.sprite.set_texture('mario_look_up')
            print('apertei')
        elif self.state == 'looking_up' and not keys[pygame.K_w]:
            self.state = 'idle'
            self.move_disable = False
            self.sprite.set_texture('mario_idle')
        
        if keys[pygame.K_a] and not self.move_disable:
            self.sprite.rect.x -= self.vx
            self.sprite.x -= self.vx
            if not self.facing_right:
                self.sprite.texture = self.original_image
                self.facing_right = True


        if keys[pygame.K_d] and not self.move_disable:
            self.sprite.rect.x += self.vx
            self.sprite.x += self.vx
            if self.facing_right:
                self.sprite.texture = pygame.transform.flip(self.sprite.texture, True, False)
                self.facing_right = False


        if keys[pygame.K_s]:
            self.sprite.set_texture('mario_duck')
            self.state = 'ducked'
            self.move_disable = True
        elif self.state == 'ducked':
            self.state = 'idle'
            self.move_disable = False
            self.sprite.set_texture('mario_idle')            


    def update(self):

        if not self.check_collision(self.scene.square):
            self.scene.speed_y = min(self.scene.speed_y + self.scene.gravity, self.scene.max_speed_y)
            self.sprite.rect.y += self.scene.speed_y
            self.sprite.y += self.scene.speed_y
        else:
            self.scene.speed_y = 0

        self.move()  
       
        # self.draw(self.scene.screen)
        
    def draw(self, screen):
        screen.blit(self.sprite.texture, (self.sprite.rect.x, self.sprite.rect.y))

    def check_collision(self, rect):
        return self.sprite.rect.colliderect(rect)
    
