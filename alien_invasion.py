#alien 267

import pygame
from pygame.sprite import Group
from settings import Settings
from game_stats import GameStats
from scoreboard import Scoreboard
from button import Button
from ship import Ship
import game_functions as gf

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

    # Create an instance to store game statistics.
    stats = GameStats(ai_settings)
    # Create an instance to store game statistics and create a scoreboard.
    sb = Scoreboard(ai_settings, screen, stats)

    # Make a ship, a group of bullets, and a group of aliens.

    ship = Ship(ai_settings, screen)

    # Make a group to store bullets in.
    bullets = Group()
    alien_bullets = Group()
    aliens = Group()
    blue_aliens = Group()

    # Create the fleet of aliens.
    gf.create_fleet(ai_settings, screen, ship, aliens, alien_bullets)

    # Start the main loop for the game.
    while True:
        gf.check_events(ai_settings, screen, stats, sb, play_button, ship,
            aliens, bullets, alien_bullets)

        if stats.game_active:
            ship.update()
            # We update the aliens’ positions after the bullets have been updated,
            # because we’ll soon be checking to see whether any bullets hit any aliens.
            gf.update_bullets(ai_settings, screen, stats, sb, ship, aliens,
                bullets, alien_bullets)
            # print(len(bullets))
            gf.update_aliens(ai_settings, screen, stats, sb, ship, aliens, blue_aliens,
                bullets, alien_bullets)

        gf.update_screen(ai_settings, screen, stats, sb, ship, aliens,
                             bullets, alien_bullets, play_button)

run_game()
