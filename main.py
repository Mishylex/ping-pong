import pygame
from pygame import mixer
WIN_H = 800
WIN_W = 600
MAIN_WINDOW = WIN_H, WIN_W
FPS = 60

pygame.font.init()
mixer.init()

main_window = pygame.display.set_mode(MAIN_WINDOW)
pygame.display.set_caption("ping-pong")
background = pygame.image.load("tennis_field.jpg")
background = pygame.transform.scale(background, MAIN_WINDOW)
main_window.blit(background, (0, 0))
clock = pygame.time.Clock()

class GameSprite(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height, speed, image_filename):
        super().__init__()
        self.image = pygame.image.load(image_filename)
        self.image = pygame.transform.scale(self.image, (width, height))
        self.speed = speed
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def reset(self, surface):
        surface.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def __init__(self, x, y, width, height, speed, image_filename):
        super().__init__(x, y, width, height, speed, image_filename)

    def set_control(self, move_up, move_down):
        self.keys = {
            "UP": move_up,
            "DOWN": move_down
        }

    def update(self):
        pressed_keys = pygame.key.get_pressed()
        if pressed_keys[self.keys["UP"]] and self.rect.y > 0:
            self.rect.y -= self.speed
        if pressed_keys[self.keys["DOWN"]] and self.rect.y < WIN_H - self.rect.height:
            self.rect.y += self.speed

class Ball(GameSprite):
    def __init__(self, pos_x, pos_y, sprite_weight, sprite_height, step_size, sprite_image_file):
        super().__init__(self, pos_x, pos_y, sprite_weight, sprite_height, step_size, sprite_image_file)
        self.x_start = None
        self.y_start = None
        self.speed_x = step_size
        self.speed_y = step_size

    def update(self):
        self.rect.x += self.speed_x
        self.rect.y += self.speed_y

        if self.rect.x <= 0 or self.rect.x >= WIN_W: 
            self.speed_x = self.speed_x * -1
        if self.rect.y <= 0 or self.rect.y >= WIN_H:
            self.speed_y = self.speed_y * -1



class Label():
    def __init__(self, x, y, text_color=(255, 255, 255), font_name="Arial", font_size = 20):
        self.x = x
        self.y = y
        self.color = text_color
        self.font = pygame.font.SysFont(font_name, font_size)
        self.font_size = font_size
        self.font_name = font_name
        self.text = None
        self.image = None

    def set_font_style(self, font_name, text_color, font_size):
        self.font = pygame.font.SysFont(font_name, font_size)
        self.font_size = font_size
        self.font_name = font_name
        self.color = text_color

    def set_text(self, text):
        self.text = text
        self.image = self.font.render(self.text, True, self.color)

    def draw(self,surface):
        surface.blit(self.image, (self.x, self.y))

player1 = Player(123, 250, 150, 150, 5, "platform.png")
player1.set_control(pygame.K_w, pygame.K_s)
player2 = Player(552, 250, 150, 150, 5, "platform.png")
player2.set_control(pygame.K_t, pygame.K_g)

points_label1 = Label(50, 10, text_color=(255, 255, 255))
points_label1.set_text("Очки 1 игрока: 0")
points_label2 = Label(50, 40, text_color=(255, 255, 255))
points_label2.set_text("Очки 2 игрока: 0")




is_running = True
while is_running:
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            is_running = False
    main_window.blit(background, (0, 0))
    
    player1.reset(main_window)
    player1.update
    player2.reset(main_window)
    player2.update
    points_label1.draw(main_window)
    points_label2.draw(main_window)

    pygame.display.update()
    clock.tick(FPS)
