#alien 267

import pygame
from pygame.sprite import Group
from settings import Settings
from game_stats import GameStats
from scoreboard import Scoreboard
from button import Button
from button import Button2
from ship import Ship
from title import Title
import game_functions as gf
# from alien import Blue
# from alien import Green
# from alien import Red
clock = pygame.time.Clock()
clock.tick(10)
print("running ticks: " + str(clock.tick(60)))
clock.get_fps()
print("Running get fps" + str(clock.get_fps()))


def run_game():

    # Initialize game and create a screen object.
    pygame.init()
    ai_settings = Settings()

    screen = pygame.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_height))

    screen = pygame.display.set_mode((1200, 800))
    pygame.display.set_caption("Alien Invasion")

    # Make the Play button.
    play_button = Button(ai_settings, screen, "Play")

    hi_button =  Button2(ai_settings, screen)

    # Create an instance to store game statistics.
    stats = GameStats(ai_settings)
    # foo = open("foo.txt", "w")
    # foo.write("0")
    # foo.close()
    fo = open("foo.txt", "r+")
    stats.high_score = int(fo.readline())
    stats.high_score2 = int(fo.readline())
    stats.high_score3 = int(fo.readline())
    fo.close()
    print("hiscore: " + str(stats.high_score))


    # Create an instance to store game statistics and create a scoreboard.
    sb = Scoreboard(ai_settings, screen, stats)
    title = Title(ai_settings, screen, "", stats)


    # Make a ship, a group of bullets, and a group of aliens.

    ship = Ship(ai_settings, screen)

    # Make a group to store bullets in.
    # blue = Blue(ai_settings, screen)
    # red = Red(ai_settings, screen)
    # green = Green(ai_settings, screen)
    bullets = Group()
    alien_bullets = Group()
    aliens = Group()

    # Create the fleet of aliens.
    gf.create_fleet(ai_settings, screen, ship, aliens, alien_bullets)

    # Start the main loop for the game.
    while True:
        title.prep_title("")
        title.prep_rules("")
        title.prep_blue_msg("")
        title.prep_red_msg("")
        title.prep_green_msg("")
        gf.check_events(ai_settings, screen, stats, sb, play_button, hi_button, ship,
            aliens, bullets, alien_bullets)

        if stats.game_active:
            ship.update(clock)
            # ship.explode(hit)
            # if hit == True and ship.image == 'images/Ship Full.gif':
            #     ship.center_ship()
            # We update the aliens’ positions after the bullets have been updated,
            # because we’ll soon be checking to see whether any bullets hit any aliens.
            gf.update_bullets(ai_settings, screen, stats, sb, ship, aliens,
                bullets, alien_bullets)
            # print(len(bullets))
            gf.update_aliens(ai_settings, screen, stats, sb, ship, aliens,
                bullets, alien_bullets)

        gf.update_screen(ai_settings, screen, stats, sb, ship, aliens,
                         title, bullets, alien_bullets, play_button,
                         hi_button)

run_game()
