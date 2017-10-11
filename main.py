import pygame
import tools

pygame.init()
SCREENWIDTH = 1280
SCREENHEIGHT = 720
SCREEN = pygame.display.set_mode((SCREENWIDTH, SCREENHEIGHT))
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)

drawingArea = pygame.Rect(SCREENWIDTH/4, 0, SCREENWIDTH/4 * 3, SCREENHEIGHT)

toolbox = tools.Box((SCREENWIDTH/4, SCREENHEIGHT))

color = GREEN
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
            pygame.draw.circle(SCREEN, color, mouse_pos, 5)
        for button in toolbox.buttons:
            if button.rect.collidepoint(mouse_pos):
                if button.name == "green":
                    color = GREEN
                elif button.name == "eraser":
                    color = BLACK
    pygame.display.update()
