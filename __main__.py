# Example file showing a basic pygame "game loop"
import pygame
import numpy as np


# pygame setup
pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True

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


while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    # fill the screen with a color to wipe away anything from last frame
    screen.fill("black")


    # RENDER YOUR GAME HERE


    # flip() the display to put your work on screen
    pygame.display.flip()
    clock.tick(60)  # limits FPS to 60

pygame.quit()