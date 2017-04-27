import pygame
import sys

def check_events():
    # The escape hatch (from while)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            # The user clicked the red x. Get out of loop & kill game
            sys.exit()