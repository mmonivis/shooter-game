import pygame
import sys

def check_events(the_player):
    # The escape hatch (from while)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            # The user clicked the red x. Get out of loop & kill game
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == 273:
                the_player.should_move("up", True)
            elif event.key == 274:
                the_player.should_move("down", True)
            elif event.key == 276:
                the_player.should_move("left", True)
            elif event.key == 275:
                the_player.should_move("right", True)
        elif event.type == pygame.KEYUP:
            if event.key == 273:
                the_player.should_move("up", False)
            elif event.key == 274:
                the_player.should_move("down", False)
            elif event.key == 276:
                the_player.should_move("left", False)
            elif event.key == 275:
                the_player.should_move("right", False)