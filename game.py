import pygame
# Import Player class from Player
from player import Player
from game_functions import check_events
from enemy import Enemy
from pygame.sprite import Group, groupcollide

# Core game functionality/loop
def run_game():
    # Init all the pygame stuff
    pygame.init()
    # Set up tuple for screen size
    screen_size = (1000,800)
    # Set up a tuple for the bg color
    background_color = (82,111,53)

    # Create a pygame screen to use
    screen = pygame.display.set_mode(screen_size)
    # Set a caption on the terminal
    pygame.display.set_caption("A heroic third person shooter game")

    the_player = Player(screen,"./images/Hero.png",100,100)
    the_player_group = Group()
    the_player_group.add(the_player)
    bad_guy = Enemy(screen,"./images/2.png",900,400)
    enemies = Group()
    enemies.add(bad_guy)

    # Main game loop. Run forever... (or until break)
    while 1: # 1/True does exact same thing. 1 for simpler codes, True for more complex
        screen.fill(background_color)

        check_events(the_player)

        # Draw player
        for player in the_player_group:
            the_player.draw_me()

        # Draw Bad Guy
        bad_guy.update_me(the_player)
        bad_guy.draw_me()

        # Check for collisions...
        hero_died = groupcollide(the_player_group, enemies, True, False)

        # Clear the screen for the next time through the loop
        pygame.display.flip()

# Start the game!
run_game()