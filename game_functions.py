import sys
from time import sleep
from alien import Alien
import pygame
import time
import random
from bullet import Alien_Bullet
from bullet import Bullet
from alien import Blue
from alien import Green
from alien import Red

def update_high_score(stats, sb):
    if stats.score > stats.high_score:
        # sb.prep_high_score()
        oldfirst = stats.high_score
        oldsecond = stats.high_score2

        # stats.high_score2 = stats.score

        stats.high_score2 = oldfirst
        stats.high_score3 = oldsecond
        stats.high_score = stats.score


        hi_score = str(stats.high_score)
        hi_score2 = str(stats.high_score2)
        hi_score3 = str(stats.high_score3)


        foo = open("foo.txt", "w")
        foo.write(hi_score + '\n' + hi_score2 + '\n' +
                  hi_score3)
        foo.close()

    elif stats.score > stats.high_score2:
        temp = stats.high_score2

        stats.high_score2 = stats.score
        stats.high_score3 = temp

        hi_score = str(stats.high_score)
        hi_score2 = str(stats.high_score2)
        hi_score3 = str(stats.high_score3)

        foo = open("foo.txt", "w")
        foo.write(hi_score + '\n' + hi_score2 + '\n' +
                  hi_score3)
        foo.close()
    elif stats.score > stats.high_score3:
        stats.high_score3 = stats.score

        hi_score = str(stats.high_score)
        hi_score2 = str(stats.high_score2)
        hi_score3 = str(stats.high_score3)

        foo = open("foo.txt", "w")
        foo.write(hi_score + '\n' + hi_score2 + '\n' +
                  hi_score3)
        foo.close()


def check_high_score(stats, sb):
    """Check to see if there's a new high score."""
    if stats.score > stats.high_score:
        stats.high_score = stats.score
        sb.prep_high_score()


def ship_hit(ai_settings, screen, stats, sb, ship, aliens, bullets, alien_bullets):
    """Respond to ship being hit by alien."""

    # if stats.ships_left > 0:
    #     # Decrement ships_left.
    #     stats.ships_left -= 1
    #
    #     # Update scoreboard.
    #     sb.prep_ships()
    #
    #     # Empty the list of aliens and bullets.
    #     aliens.empty()
    #     bullets.empty()
    #
    #     # Create a new fleet and center the ship.
    #     create_fleet(ai_settings, screen, ship, aliens, alien_bullets)
    #     ship.center_ship()
    #
    #     # Pause.
    #     sleep(0.5)
    print("Do nothing")
    # else:
    #     stats.game_active = False
    #     pygame.mouse.set_visible(True)

def check_aliens_bottom(ai_settings, screen, stats, sb, ship, aliens,
        bullets, alien_bullets):
    """Check if any aliens have reached the bottom of the screen."""
    screen_rect = screen.get_rect()
    for alien in aliens.sprites():
        if alien.rect.bottom >= screen_rect.bottom:
            # Treat this the same as if the ship got hit.
            ship_hit(ai_settings, screen, stats, sb, ship, aliens, bullets, alien_bullets)
            break

def update_aliens(ai_settings, screen, stats, sb, ship, aliens,
          bullets, alien_bullets):
    """Update the postions of all aliens in the fleet."""
    """
    Check if the fleet is at an edge,
    and then update the postions of all aliens in the fleet.
    """
    check_fleet_edges(ai_settings, aliens)
    aliens.update()
    # blue_aliens.update()


    # Look for alien-ship collisions.
    if pygame.sprite.spritecollideany(ship, aliens):
        ship_hit(ai_settings, screen, stats, sb, ship, aliens, bullets, alien_bullets)

    # Look for aliens hitting the bottom of the screen.
    check_aliens_bottom(ai_settings, screen, stats, sb, ship, aliens, bullets, alien_bullets)

def get_number_rows(ai_settings, ship_height, alien_height):
    """Determine the number of rows of aliens that fit on the screen."""
    available_space_y = (ai_settings.screen_height -
                            (3 * alien_height) - ship_height)
    number_rows = int(available_space_y / (2 * alien_height))
    return number_rows

def get_number_aliens_x(ai_settings, alien_width):
    """Determine the number of aliens that fit in a row."""
    available_space_x = ai_settings.screen_width - 2 * alien_width
    number_aliens_x = int(available_space_x / (2 * alien_width))
    #  number_aliens_x = int(available_space_x / (alien_width))
    return number_aliens_x

def create_alien(ai_settings, screen, aliens, alien_number, row_number, alien_bullets):
    """Create an alien and place it in the row."""
    # if row_number == 0:
    #     alien = Blue(ai_settings, screen)
    #     alien_width = alien.rect.width
    #     # alien.x = alien_width + alien_width * alien_number
    #     alien.x = alien_width + 2 * alien_width * alien_number
    #     alien.rect.x = alien.x
    #     alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_number
    #     aliens.add(alien)
    if row_number == 0:
        blue = Blue(ai_settings, screen)
        blue_width = blue.rect.width
        blue.x = blue_width + 2 * blue_width * alien_number
        blue.rect.x = blue.x
        blue.rect.y = blue.rect.height + 2 * blue.rect.height * row_number
        aliens.add(blue)
    elif row_number == 1:
        green = Green(ai_settings, screen)
        green_width = green.rect.width
        green.x = green_width + 2 * green_width * alien_number
        green.rect.x = green.x
        green.rect.y = green.rect.height + 2 * green.rect.height * row_number
        aliens.add(green)
    elif row_number == 2:
        red = Red(ai_settings, screen)
        red_width = red.rect.width
        red.x = red_width + 2 * red_width * alien_number
        red.rect.x = red.x
        red.rect.y = red.rect.height + 2 * red.rect.height * row_number
        aliens.add(red)


def create_fleet(ai_settings, screen, ship, aliens, alien_bullets):
    """Create a full fleet of aliens."""
    # Create an alien and find the number of aliens in a row.
    # Spacing between each alien is equal to one alien width.
    alien = Alien(ai_settings, screen)
    number_aliens_x = get_number_aliens_x(ai_settings, alien.rect.width)
    number_rows = get_number_rows(ai_settings, ship.rect.height,
                                  alien.rect.height)

    # Create the first row of aliens.
    for row_number in range(number_rows):
        for alien_number in range(number_aliens_x):
            create_alien(ai_settings, screen, aliens, alien_number,
                            row_number, alien_bullets)



def check_fleet_edges(ai_settings, aliens):
    """Respond appropriately if any aliens have reached an edge."""
    # Page 278 for more info
    for alien in aliens.sprites():
        if alien.check_edges():
            change_fleet_direction(ai_settings, aliens)
            break

def change_fleet_direction(ai_settings, aliens):
    """Drop the entire fleet and change the fleet's direction."""
    # Page 279 for more info
    # for alien in aliens.sprites():
    #     alien.rect.y += ai_settings.fleet_drop_speed
    ai_settings.fleet_direction *= -1



def update_bullets(ai_settings, screen, stats, sb, ship, aliens, bullets,
           alien_bullets):
    """Update position of bullets and get rid of old bullets."""
    # Update bullet positions.
    bullets.update()
    alien_bullets.update()

    # Get rid of bullets that have disappeared.
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)

    # Check for any bullets that have hit aliens.
    # If so, get rid of the bullet and the alien.
    check_bullet_alien_collisions(ai_settings, screen, stats, sb, ship,
        aliens, bullets, alien_bullets)

    # that’s able to travel to the top of the screen, destroying every alien in its
    # path, you could set the first Boolean argument to False and keep the second
    # Boolean argument set to True. The aliens hit would disappear, but all bullets
    # would stay active until they disappeared off the top of the screen.

    for alien_bullet in alien_bullets.copy():
        if alien_bullet.rect.bottom >= 1200:
            alien_bullets.remove(alien_bullet)

    randx = random.randint(1, 10)
    # randtime = random.randint(1995, 2005)
    # preven shooting every time
    alien_atk = random.randint(0, len(aliens))

    time = pygame.time.get_ticks()
    x = 0

    if time % 500 == 0 and len(alien_bullets) < ai_settings.a_bullets_allowed and len(aliens) > 0:
        for alien in aliens.sprites():
            x += 1
            if x == alien_atk or x*ai_settings.alien_atk == alien_atk:
                new_alien_bullet = Alien_Bullet(ai_settings, screen, alien)
                alien_bullets.add(new_alien_bullet)



    check_bullet_ship_collisions(ai_settings, screen, stats, sb, ship,
        aliens, bullets, alien_bullets)

    # ship.endExplosion()

def check_bullet_ship_collisions(ai_settings, screen, stats, sb, ship,
        aliens, bullets, alien_bullets):

    for alien_bullet in alien_bullets.copy():
        if alien_bullet.rect.colliderect(ship):
            if stats.ships_left > 0:
                alien_bullets.empty()
                bullets.empty()
                ship.explosion()
                # ship.center_ship()
                pygame.time.delay(500)
                stats.ships_left -= 1
                sb.prep_ships()

            else:
                update_high_score(stats, sb)
                stats.game_active = False
                pygame.mouse.set_visible(True)



#this function changes the bullet, ship, and alien speed for each level
def check_bullet_alien_collisions(ai_settings, screen, stats, sb, ship,
            aliens, bullets, alien_bullets):
    """Respond to bullet-alien collisions."""
    # Remove any bullets and aliens that have collided.
    # collisions = pygame.sprite.groupcollide(bullets, aliens, True, True)
    #
    # if collisions:
    #     for aliens in collisions.values():
    #         stats.score += ai_settings.alien_points * len(aliens)
    #         sb.prep_score()
    #     check_high_score(stats, sb)
    time = pygame.time.get_ticks()
    for bullet in bullets.copy():
        for alien in aliens.copy():
            if bullet.rect.colliderect(alien):
                bullets.remove(bullet)
                alien.explosion()
                stats.score += ai_settings.alien_points * len(aliens)
                print ("aliens: " + str(len(aliens)))
                print("destroyed: " + str(ai_settings.destroyed))
                sb.prep_score()

                # aliens.remove(alien)
            check_high_score(stats, sb)

    # if collisions:
    #     for aliens in collisions.values():
    #             stats.score += ai_settings.alien_points * len(aliens)
    #             sb.prep_score()
    #         check_high_score(stats, sb)
    speed_up = True
    if ai_settings.destroyed == int(len(aliens)* 7/10) and speed_up:
        pygame.mixer.music.load('music\doxent_-_Haze_Speedup.wav')
        pygame.mixer.music.play()
        speed_up = False

    if len(aliens) == ai_settings.destroyed:
        pygame.mixer.music.load('music\doxent_-_Haze.mp3')
        pygame.mixer.music.play()
        pygame.time.delay(500)
        ai_settings.destroyed = 0
        print("destroyed: " + str(ai_settings.destroyed))
        # If the entire fleet is destroyed, start a new level.
        # for alien in aliens.copy():
        #     alien.animate()
        aliens.empty()
        bullets.empty()
        alien_bullets.empty()
        ai_settings.increase_speed()
        if ai_settings.a_bullets_allowed < 10:
            ai_settings.a_bullets_allowed += 1
        # Increase level.
        stats.level += 1
        if stats.level % 3 == 0:
            ai_settings.a_bullet_height += (1/5)*ai_settings.a_bullet_height
            ai_settings.a_bullet_width += (1/5)*ai_settings.a_bullet_width
            ai_settings.alien_atk -= 1

        if stats.level % 2 == 0:
            ai_settings.a_bullet_speed += (2/5)*ai_settings.a_bullet_speed

        sb.prep_level()

        create_fleet(ai_settings, screen, ship, aliens, alien_bullets)

def check_keydown_events(event, ai_settings, screen, ship, bullets):
    """Respond to keypresses."""
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True
    elif event.key == pygame.K_SPACE:
        # Create a new bullet and add it to the bullets group.
        if len(bullets) < ai_settings.bullets_allowed:
            new_bullet = Bullet(ai_settings, screen, ship)
            bullets.add(new_bullet)

def check_keyup_events(event, ship):
    """Respond to key releases."""
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False

def check_events(ai_settings, screen, stats, sb, play_button, hi_button, ship, aliens,
        bullets, alien_bullets):
    """Respond to keypresses and mouse events."""


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            check_play_button(ai_settings, screen, stats, sb, play_button,
                              ship, aliens, bullets, alien_bullets, mouse_x, mouse_y)

            check_hiscore_button(hi_button, ai_settings, screen,
                                 stats, sb, mouse_x, mouse_y)

        elif event.type == pygame.KEYDOWN:
            #new function to make this function easier to add code
            check_keydown_events(event, ai_settings, screen, ship, bullets)

        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)

def check_hiscore_button(hi_button, ai_settings, screen,
                         stats, sb, mouse_x, mouse_y):
    button_clicked = hi_button.rect.collidepoint(mouse_x, mouse_y)
    if button_clicked and not stats.game_active:
        stats.hiscore_active = True
        print("TOASTY")


def check_play_button(ai_settings, screen, stats, sb, play_button, ship,
        aliens, bullets, alien_bullets, mouse_x, mouse_y):
    """Start a new game when the player clicks Play."""
    button_clicked = play_button.rect.collidepoint(mouse_x, mouse_y)
    if button_clicked and not stats.game_active:
        # Reset the game settings.
        pygame.mixer.init()
        pygame.mixer.music.load('Music\doxent_-_Haze.mp3')
        pygame.mixer.music.play(-1)
        ai_settings.initialize_dynamic_settings()

        stats.reset_stats()
        stats.game_active = True
        stats.hiscore_active = False

        # Hide the mouse cursor
        pygame.mouse.set_visible(False)

        # Reset the scoreboard images.
        sb.prep_score()
        sb.prep_high_score()
        sb.prep_level()
        sb.prep_ships()

        ai_settings.a_bullets_allowed = 5
        ai_settings.a_bullet_height = 30
        ai_settings.a_bullet_width = 9
        ai_settings.a_bullet_speed = .3
        ai_settings.ship_speed_factor = 1.5
        ai_settings.bullet_speed_factor = 3
        ai_settings.alien_speed_factor = .8
        ai_settings.destroyed = 0

        # Empty the list of aliens and bullets.
        aliens.empty()
        bullets.empty()
        alien_bullets.empty()

        # Create a new fleet and center the ship.
        create_fleet(ai_settings, screen, ship, aliens, alien_bullets)
        ship.center_ship()

def update_screen(ai_settings, screen, stats, sb, ship, aliens, title, bullets,
                alien_bullets, play_button, hi_buttton):
    """Update images on the screen and flip to the new screen."""
    # Redraw the screen during each pass through the loop.
    screen.fill(ai_settings.bg_color)

    # Redraw all bullets behind ship and aliens.
    for bullet in bullets.sprites():
        bullet.draw_bullet()

    for alien_bullet in alien_bullets.sprites():
        alien_bullet.draw_bullet()

    ship.blitme()
    aliens.draw(screen)

    # Draw the score information.
    sb.show_score()

    # Draw the play button if the game is inactive.
    if not stats.game_active:

        screen.fill(ai_settings.start_color)
        title.prep_title("SPACE")
        title.prep_rules("INVADERS")
        if stats.hiscore_active == False:
            title.prep_blue_msg("30 PTS")
            title.prep_red_msg("10 PTS")
            title.prep_green_msg("20 PTS")
            title.prep_high_label("")

        else:
            print("TOASTY")
            title.prep_high_label("Hi Score:")
            title.prep_blue_msg(str(stats.high_score))
            title.prep_red_msg(str(stats.high_score3))
            title.prep_green_msg(str(stats.high_score2))
        title.prep_high_score(str(stats.high_score))

        title.draw_button()
        hi_buttton.draw_button()
        play_button.draw_button()

    # Make the most recently drawn screen visible.
    pygame.display.flip()

