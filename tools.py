import pygame

GRAY = (30, 30, 30)
LIGHTGRAY = (60, 60, 60)
GREEN = (10, 200, 10)
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
        self.buttons.draw(self.mainPanel)
                
    def eraser(self):
        button = Button(pygame.image.load("img/eraser.png"))
        button.rect.x = 30
        button.rect.top = 30
        button.name = "eraser"
        self.buttons.add(button)

    def green(self):
        buttonSurface = pygame.Surface((80, 80))
        buttonSurface.fill(GREEN)
        button = Button(buttonSurface)
        button.rect.x = 170
        button.rect.top = 30
        button.name = "green"
        self.buttons.add(button)
    

class Button(pygame.sprite.Sprite):
    def __init__(self, image):
        pygame.sprite.Sprite.__init__(self)
        self.image = image
        self.rect = self.image.get_rect()
        