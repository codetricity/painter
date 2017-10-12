import pygame
import tools

pygame.init()
SCREENWIDTH = 1280
SCREENHEIGHT = 720
SCREEN = pygame.display.set_mode((SCREENWIDTH, SCREENHEIGHT))
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

drawingArea = pygame.Rect(SCREENWIDTH/4, 0, SCREENWIDTH/4 * 3, SCREENHEIGHT)

toolbox = tools.Box((SCREENWIDTH/4, SCREENHEIGHT))

panda = pygame.image.load("img/panda.png")

brushColor = GREEN
brushSize = 5
stamp = False
mousedown = False

gameOn = True

while gameOn:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameOn = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            mousedown = True
        elif event.type == pygame.MOUSEBUTTONUP:
            mousedown = False
        mouse_pos = pygame.mouse.get_pos()
    SCREEN.blit(toolbox.mainPanel, (0, 0))

    if mousedown:
        if drawingArea.collidepoint(mouse_pos):
            if not stamp:
                pygame.draw.circle(SCREEN, brushColor, mouse_pos, brushSize)
            else:
                SCREEN.blit(panda, mouse_pos)

        for button in toolbox.buttons:
            if button.rect.collidepoint(mouse_pos):
                if button.type == "stamp":
                    stamp = True
                else:
                    stamp = False
                if button.name == "green":
                    brushColor = GREEN
                elif button.name == "white":
                    brushColor = WHITE
                elif button.name == "eraser":
                    brushColor = BLACK
                elif button.name == "small":
                    brushSize = 5
                elif button.name == "medium":
                    brushSize = 12
                elif button.name == "large":
                    brushSize = 20

    pygame.display.update()
