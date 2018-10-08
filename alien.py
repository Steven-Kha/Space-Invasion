import pygame
from pygame.sprite import Sprite
import time

class Alien(Sprite):
    """A class to represent a single alien in the fleet."""

    def __init__(self, ai_settings, screen):
        """Initialize the alien and set its starting position."""
        super(Alien, self).__init__()
        self.screen = screen
        self.ai_settings = ai_settings


        # Load the alien image and set its rect attribute.
        self.image = pygame.image.load('images/UFO.gif')
        self.rect = self.image.get_rect()

        # Start each new alien near the top left of the screen.
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # Store the alien's exact position.
        self.x = float(self.rect.x)
        self.hit = False

    def check_edges(self):
        """Return True if alien is at edge of screen."""
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right:
            return True
        elif self.rect.left <= 0:
            return True

    def explosion(self):
        print("Yellow destroyed")

    def update(self, clock):
        """Move the alien right or left."""
        if self.hit == True:
            self.image = pygame.image.load('images/delete.png')
            self.rect = self.rect = pygame.Rect(0, 0, 0, 0)

        self.x += (self.ai_settings.alien_speed_factor *
                        self.ai_settings.fleet_direction)
        self.rect.x = self.x

    def blitme(self):
        """Draw the alien at its current location."""
        self.screen.blit(self.image, self.rect)


class Blue(Alien):
    # inheritance
    def __init__(self, ai_settings, screen):
        """Initialize the alien and set its starting position."""
        super(Alien, self).__init__()
        self.screen = screen
        self.ai_settings = ai_settings

        # Load the alien image and set its rect attribute.
        self.blue = ['images/Blue.gif', 'images/Blue2.gif']

        self.boom = ['images/blueEx1.png', 'images/blueEx2.png',
                     'images/blueEx3.png']

        self.image = pygame.image.load(self.blue[0])
        self.rect = self.image.get_rect()

        # Start each new alien near the top left of the screen.
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # Store the alien's exact position.
        self.x = float(self.rect.x)
        self.animate = 0
        self.hit = False

    def explosion(self):
        self.hit = True

    def update(self, clock):
        time = pygame.time.get_ticks()

        if self.hit == True:
            if self.animate == 0 and time % 125 == 0:
                self.image = pygame.image.load(self.boom[0])
                print("Blue explode 1")
                self.animate = 1
            if self.animate == 1 and time % 125 == 1:
                self.image = pygame.image.load(self.boom[1])
                print("Blue explode 2")
                self.animate = 2
            if self.animate == 2 and time % 125 == 0:
                self.image = pygame.image.load(self.boom[2])
                print("Blue explode 3")
                self.animate = 3
            if self.animate == 3 and time % 125 == 1:
                self.image = pygame.image.load('images/delete.png')
                self.rect = pygame.Rect(0, 0, 0, 0)
                self.hit = False

        else:
            if self.animate == 0 and time % 250 == 0:
                self.image = pygame.image.load(self.blue[1])
                print("Blue closes legs")
                self.animate = 1

            elif self.animate == 1 and time % 250 == 1:
                self.image = pygame.image.load(self.blue[0])
                print("Blue opens legs")
                self.animate = 0


        self.x += (self.ai_settings.alien_speed_factor *
                   self.ai_settings.fleet_direction)
        self.rect.x = self.x


class Green(Alien):
    def __init__(self, ai_settings, screen):
        """Initialize the alien and set its starting position."""
        super(Alien, self).__init__()
        self.screen = screen
        self.ai_settings = ai_settings

        # Load the alien image and set its rect attribute.
        self.green = ['images/Green.gif', 'images/Green2.gif']
        self.boomG = ['images/GreenEx_3.png', 'images/GreenEx_4.png',
                     'images/GreenEx_5.png']
        self.image = pygame.image.load(self.green[0])
        self.rect = self.image.get_rect()

        # Start each new alien near the top left of the screen.
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # Store the alien's exact position.
        self.x = float(self.rect.x)
        self.animate = 0
        self.hit = False

    def explosion(self):
        self.hit = True

    def update(self, clock):
        time = pygame.time.get_ticks()

        if self.hit == True:
            if self.animate == 0 and time % 125 == 0:
                self.image = pygame.image.load(self.boomG[0])
                self.animate = 1
            if self.animate == 1 and time % 125 == 1:
                self.image = pygame.image.load(self.boomG[1])
                self.animate = 2
            if self.animate == 2 and time % 125 == 0:
                self.image = pygame.image.load(self.boomG[2])
                self.animate = 3
            if self.animate == 3 and time % 125 == 1:
                self.image = pygame.image.load('images/delete.png')
                self.rect = pygame.Rect(0, 0, 0, 0)

                self.hit = False
        else:
            if self.animate == 0 and time % 250 == 0:
                self.image = pygame.image.load(self.green[1])
                # print("Blue closes legs")
                # print(str(self.cur))
                # print(str(inttime))
                self.animate = 1
            elif self.animate == 1 and time % 250 == 1:
                self.image = pygame.image.load(self.green[0])
                # print("Blue opens legs")
                # print(str(self.cur))
                # print(str(inttime))
                self.animate = 0

        self.x += (self.ai_settings.alien_speed_factor *
                   self.ai_settings.fleet_direction)
        self.rect.x = self.x

class Red(Alien):
    def __init__(self, ai_settings, screen):
        """Initialize the alien and set its starting position."""
        super(Alien, self).__init__()
        self.screen = screen
        self.ai_settings = ai_settings

        # Load the alien image and set its rect attribute.
        self.red = ['images/Red.gif', 'images/Red2.gif']
        self.boomR = ['images/RedEx_3.png', 'images/RedEx_4.png',
                     'images/RedEx_5.png']

        self.image = pygame.image.load(self.red[0])
        self.rect = self.image.get_rect()

        # Start each new alien near the top left of the screen.
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # Store the alien's exact position.
        self.x = float(self.rect.x)
        self.animate = 0
        self.hit = False

    def explosion(self):
        self.hit = True

    def update(self, clock):
        time = pygame.time.get_ticks()

        if self.hit == True:
            if self.animate == 0 and time % 125 == 0:
                self.image = pygame.image.load(self.boomR[0])
                self.animate = 1
            if self.animate == 1 and time % 125 == 1:
                self.image = pygame.image.load(self.boomR[1])
                self.animate = 2
            if self.animate == 2 and time % 125 == 0:
                self.image = pygame.image.load(self.boomR[2])
                self.animate = 3
            if self.animate == 3 and time % 125 == 1:
                self.image = pygame.image.load('images/delete.png')
                self.rect = pygame.Rect(0, 0, 0, 0)

                self.hit = False
        else:
            if self.animate == 0 and time % 250 == 0:
                self.image = pygame.image.load(self.red[1])
                # print("Blue closes legs")
                # print(str(self.cur))
                # print(str(inttime))
                self.animate = 1
            elif self.animate == 1 and time % 250 == 1:
                self.image = pygame.image.load(self.red[0])
                # print("Blue opens legs")
                # print(str(self.cur))
                # print(str(inttime))
                self.animate = 0

        self.x += (self.ai_settings.alien_speed_factor *
                   self.ai_settings.fleet_direction)
        self.rect.x = self.x
