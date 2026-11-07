# Example file showing a basic pygame "game loop"
import pygame
import numpy as np


# pygame setup
pygame.init()
pygame.font.init()
screen = pygame.display.set_mode((640, 720))
clock = pygame.time.Clock()
running = True
defaultFontBig = pygame.font.Font(size=70)
defaultFontSmol = pygame.font.Font(size=30)
runningSim = False
fps = 10
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
    xStart = 120
    yStart = 120
    blockSize = 40 # Set the size of the grid block
    i = 0
    for x in range(xStart, 400+xStart, blockSize):
        for y in range(yStart, 400+yStart, blockSize):
            i += 1
            rect = pygame.Rect(x, y, blockSize, blockSize)
            pygame.draw.rect(screen, "white", rect, 1)
            screen.blit(defaultFontSmol.render(f"{i}", antialias=True ,color="white"), (x, y))



while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if runningSimButtonRect.collidepoint(event.pos):
                if runningSim:
                    runningSim = False
                else:
                    runningSim = True
            elif plusFPSrect.collidepoint(event.pos):
                fps += 1
                if fps > 60:
                    fps -= 1
            elif minusFPSrect.collidepoint(event.pos):
                fps -= 1
                if fps < 1:
                    fps += 1
    # fill the screen with a color to wipe away anything from last frame
    screen.fill("black")

    drawGrid()
    screen.blit(defaultFontBig.render("Pygame of Life", antialias=True ,color="white"), (145, 30))
    screen.blit(defaultFontSmol.render("Made by @Aquaticsanti", antialias=True ,color="white"), (202, 85))
    runningSimButtonRect = pygame.Rect(280, 540, 80, 35)
    pygame.draw.rect(screen, "white", runningSimButtonRect, 3, 15)
    if runningSim:
        screen.blit(defaultFontSmol.render(f"Pause", antialias=True ,color="white"), (290, 547.5))
    else:
        screen.blit(defaultFontSmol.render(f"Play", antialias=True ,color="white"), (297.5, 547.5))
    screen.blit(defaultFontSmol.render(f"FPS: {fps}", antialias=True ,color="white"), (260, 588))
    
    plusFPSrect = pygame.Rect(340, 587, 20, 20)
    pygame.draw.rect(screen, "white", plusFPSrect, 2, 5)
    screen.blit(defaultFontSmol.render(f"+", antialias=True ,color="white"), (344, 585))

    minusFPSrect = pygame.Rect(365, 587, 20, 20)
    pygame.draw.rect(screen, "white", minusFPSrect, 2, 5)
    screen.blit(defaultFontSmol.render(f"-", antialias=True ,color="white"), (371, 586))
    # flip() the display to put your work on screen
    pygame.display.flip()
    clock.tick(fps)  # limits FPS to 60

pygame.quit()