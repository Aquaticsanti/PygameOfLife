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
size = 10
class Cell:
    def __init__(self, state="dead", flipTo=None, rect=None):
        self.state = state
        self.flipTo = flipTo
        self.rect = rect
    def flipThis(self):
        """Flips the cell and sets self.flip back to false.
        """
        if self.flipTo is not None:
            self.state = self.flipTo
            self.flipTo = None
    def queueFlip(self):
        """Sets self.flip to True. Kinda unnecessary but it makes the code a bit more readable.
        """
        self.flip = True

grid = np.empty((size, size), dtype=object)
for x in range(size):
    for y in range(size):
        grid[x, y] = Cell()

gridRect = pygame.Rect(120, 120, 400, 400)
# Source - https://stackoverflow.com/a/61007670
# Posted by theshubhagrwl, modified by community & me (Aquaticsanti). See post 'Timeline' for change history
# Retrieved 2026-11-07, License - CC BY-SA 4.0
def drawGrid(): # This function was partially AI generated.
    xStart = 120
    yStart = 120
    gridWidth = 400
    gridHeight = 400

    for x in range(size):
        for y in range(size):
            left = xStart + x * gridWidth / size
            top = yStart + y * gridHeight / size
            right = xStart + (x + 1) * gridWidth / size
            bottom = yStart + (y + 1) * gridHeight / size

            rect = pygame.Rect(
                round(left), round(top),
                round(right) - round(left),
                round(bottom) - round(top)
            )

            grid[x, y].rect = rect

            if grid[x, y].state == "alive":
                pygame.draw.rect(screen, "white", rect, 0)
            else:
                pygame.draw.rect(screen, "white", rect, 1)



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
            elif plusSizeRect.collidepoint(event.pos):
                size += 1
                grid = np.empty((size, size), dtype=object)
                for x in range(size):
                    for y in range(size):
                        grid[x, y] = Cell()
            elif minusSizeRect.collidepoint(event.pos):
                size -= 1
                if size < 1:
                    size += 1
                grid = np.empty((size, size), dtype=object)
                for x in range(size):
                    for y in range(size):
                        grid[x, y] = Cell()
            elif gridRect.collidepoint(event.pos):
                for element in grid.flat:
                    if element.rect.collidepoint(event.pos):
                        if element.state == "alive":
                            element.state = "dead"
                        else:
                            element.state = "alive"
                        break
            elif randomizeRect.collidepoint(event.pos):
                runningSim = False
                x = np.random.randint(size * size)
                grid = np.empty((size, size), dtype=object).flatten()
                for i, _ in enumerate(grid):
                    grid[i] = Cell()
                for i in range(x):
                    grid[i].state = "alive"
                np.random.shuffle(grid)
                grid = grid.reshape((size, size))
            elif clearRect.collidepoint(event.pos):
                runningSim = False
                grid = np.empty((size, size), dtype=object)
                for x in range(size):
                    for y in range(size):
                        grid[x, y] = Cell()

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("black")

    drawGrid()
    screen.blit(defaultFontBig.render("Pygame of Life", antialias=True ,color="white"), (145, 30))
    screen.blit(defaultFontSmol.render("Made by @Aquaticsanti", antialias=True ,color="white"), (202, 85))
    runningSimButtonRect = pygame.Rect(280, 540, 80, 35)
    pygame.draw.rect(screen, "white", runningSimButtonRect, 3, 15)
    if runningSim:
        for x in range(size):
            for y in range(size):
                neighbours = [(x-1, y-1), (x-1, y), (x-1, y+1),
                              (x, y-1),             (x, y+1),
                              (x+1, y-1), (x+1, y), (x+1, y+1)]
                for i, j in enumerate(neighbours):
                    if 0 <= j[0] < size and 0 <= j[1] < size:
                        pass
                    else:
                        neighbours[i] = None
                realNeighbours = [] # AKA all that aren't none
                for i in neighbours:
                    if i is not None:
                        realNeighbours.append(i)
                for i, j in enumerate(realNeighbours):
                    realNeighbours[i] = grid[*j].state
                
                # Now the conditions (from https://en.wikipedia.org/wiki/Conway%27s_Game_of_Life#Rules)
                if realNeighbours.count("alive") < 2: # Rule 1
                    grid[x, y].flipTo = "dead"
                    continue
                elif realNeighbours.count("alive") == 2: # Rule 2
                    pass
                elif realNeighbours.count("alive") > 3: # Rule 3
                    grid[x, y].flipTo = "dead"
                    continue
                elif realNeighbours.count("alive") == 3: # Rule 4
                    grid[x, y].flipTo = "alive"
                    continue
        for x in range(size):
            for y in range(size):
                grid[x, y].flipThis()
        screen.blit(defaultFontSmol.render(f"Pause", antialias=True ,color="white"), (290, 547.5))
    else:
        screen.blit(defaultFontSmol.render(f"Play", antialias=True ,color="white"), (297.5, 547.5))

    screen.blit(defaultFontSmol.render(f"FPS: {fps}", antialias=True ,color="white"), (180, 588))
    
    plusFPSrect = pygame.Rect(260, 587, 20, 20)
    pygame.draw.rect(screen, "white", plusFPSrect, 2, 5)
    screen.blit(defaultFontSmol.render(f"+", antialias=True ,color="white"), (264, 585))

    minusFPSrect = pygame.Rect(285, 587, 20, 20)
    pygame.draw.rect(screen, "white", minusFPSrect, 2, 5)
    screen.blit(defaultFontSmol.render(f"-", antialias=True ,color="white"), (291, 586))

    screen.blit(defaultFontSmol.render(f"Size: {size}", antialias=True ,color="white"), (340, 588))
        
    plusSizeRect = pygame.Rect(425, 587, 20, 20)
    pygame.draw.rect(screen, "white", plusSizeRect, 2, 5)
    screen.blit(defaultFontSmol.render(f"+", antialias=True ,color="white"), (429, 585))

    minusSizeRect = pygame.Rect(450, 587, 20, 20)
    pygame.draw.rect(screen, "white", minusSizeRect, 2, 5)
    screen.blit(defaultFontSmol.render(f"-", antialias=True ,color="white"), (456, 586))

    randomizeRect = pygame.Rect(235, 620, 175, 35)
    pygame.draw.rect(screen, "white", randomizeRect, 3, 15)
    screen.blit(defaultFontSmol.render(f"Randomize grid", antialias=True ,color="white"), (245, 627.5))

    clearRect = pygame.Rect(257, 662, 132.5, 35)
    pygame.draw.rect(screen, "white", clearRect, 3, 15)
    screen.blit(defaultFontSmol.render(f"Clear grid", antialias=True ,color="white"), (273, 670))
    # flip() the display to put your work on screen
    pygame.display.flip()
    clock.tick(fps)  # limits FPS to 60

pygame.quit()