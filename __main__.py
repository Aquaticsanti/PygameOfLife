# Example file showing a basic pygame "game loop"
import pygame
import numpy as np


# pygame setup
pygame.init()
pygame.font.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True
defaultFontBig = pygame.font.Font(size=70)
defaultFontSmol = pygame.font.Font(size=30)

class Cell:
    def __init__(self, state="dead", flip=False):
        self.state = state
        self.flip = flip
    def flipThis():
        """Flips the cell and sets self.flip back to false.
        """
        if self.flip:
            if self.state == "dead":
                self.state == "alive"
            else:
                self.state = "dead"
            self.flip = False
    def queueFlip():
        """Sets self.flip to True. Kinda unnecessary but it makes the code a bit more readable.
        """
        self.flip = True

grid = np.full((10, 10), Cell())

# Source - https://stackoverflow.com/a/61007670
# Posted by theshubhagrwl, modified by community & me (Aquaticsanti). See post 'Timeline' for change history
# Retrieved 2026-11-07, License - CC BY-SA 4.0
def drawGrid():
    xStart = 440
    yStart = 120
    blockSize = 40 # Set the size of the grid block
    for x in range(xStart, 400+xStart, blockSize):
        for y in range(yStart, 400+yStart, blockSize):
            rect = pygame.Rect(x, y, blockSize, blockSize)
            pygame.draw.rect(screen, "white", rect, 1)



while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    # fill the screen with a color to wipe away anything from last frame
    screen.fill("black")
    drawGrid()
    screen.blit(defaultFontBig.render("Pygame of Life", antialias=True ,color="white"), (465, 30))
    screen.blit(defaultFontSmol.render("Made by @Aquaticsanti", antialias=True ,color="white"), (515, 85))
    # RENDER YOUR GAME HERE


    # flip() the display to put your work on screen
    pygame.display.flip()
    clock.tick(60)  # limits FPS to 60

pygame.quit()