import pygame

GRAY = (30, 30, 30)
LIGHTGRAY = (60, 60, 60)
GREEN = (10, 200, 10)
WHITE = (255, 255, 255)

SIZE = 128


class Box:
    def __init__(self, size):
        self.mainPanel = pygame.Surface(size)
        self.mainPanel.fill(GRAY)
        self.width = size[0]
        self.height = size[1]
        self.buttons = pygame.sprite.Group()
        self.eraser()
        self.green()
        self.white()
        self.small()
        self.medium()
        self.large()
        self.panda()
        self.buttons.draw(self.mainPanel)
                
    def eraser(self):
        button = Button()
        button.image = pygame.image.load("img/eraser.png")
        button.rect.x = 30
        button.rect.top = 30
        button.name = "eraser"
        self.buttons.add(button)

    def large(self):
        button = Button()
        pygame.draw.circle(button.image, WHITE, (40, 40), 20)
        button.rect.x = 170
        button.rect.top = 30
        button.name = "large"
        self.buttons.add(button)

    def small(self):
        button = Button()
        pygame.draw.circle(button.image, WHITE, (40, 40), 5)
        button.rect.x = 30
        button.rect.top = 158
        button.name = "small"
        self.buttons.add(button)

    def medium(self):
        button = Button()
        pygame.draw.circle(button.image, WHITE, (40, 40), 12)
        button.rect.x = 170
        button.rect.top = 158
        button.name = "medium"
        self.buttons.add(button)

    def green(self):
        button = Button()
        button.image.fill(GREEN)
        button.rect.x = 170
        button.rect.top = 286
        button.name = "green"
        self.buttons.add(button)

    def white(self):
        button = Button()
        button.image.fill(WHITE)
        button.rect.x = 30
        button.rect.top = 286
        button.name = "white"
        self.buttons.add(button)

    def panda(self):
        button = Button()
        button.image = pygame.image.load("img/panda.png")
        button.rect.x = 30
        button.rect.top = 414
        button.type = "stamp"
        button.name = "panda"
        self.buttons.add(button)


class Button(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((80, 80))
        self.image.fill(GRAY)
        self.rect = self.image.get_rect()
        self.type = ""
        self.name = ""
        