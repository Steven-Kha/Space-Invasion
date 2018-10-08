import pygame
from pygame.sprite import Sprite
import time
class Ship(Sprite):

    def __init__(self, ai_settings, screen):
        """Initialize the ship and set its starting position."""
        super(Ship, self).__init__()

        self.screen = screen
        self.ai_settings = ai_settings
        # Load the ship image and get its rect.
        self.explode = ["images/Ship Full.gif","images/ShipExplode01.png", "images/ShipExplode02.png",
                   "images/ShipExplode03.png", "images/ShipExplode04.png", "images/ShipExplode05.png",
                   "images/ShipExplode06.png", "images/ShipExplode07.png",
                   "images/ShipExplode08.png", "images/ShipExplode09.png"]
        self.image = pygame.image.load(self.explode[0])
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        # Start each new ship at the bottom center of the screen.
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        # Store a decimal value for the ship's center.
        # Let us update it with finer control when using decimals
        # Also convert the value of self.rect.centerx to a decimal and
        # store this value in self.center.
        self.center = float(self.rect.centerx)

        # Movement flag
        self.moving_right = False
        self.moving_left = False
        self.animate = 0
        self.hit = False


    def center_ship(self):
        """Center the ship on the screen."""
        self.center = self.screen_rect.centerx

    def explosion(self):
        self.hit = True

    def endExplosion(self):
        self.hit = False

    def update(self, clock):
        """Update the ship's position based on the movement flag."""
        # Update the ship's center value, not the rect.
        # Now prevent the ship from going out of the game window

        # self.cur = time.time()
        # self.sec = self.cur % 60
        # clock.get_time()
        time = pygame.time.get_ticks()
        print ("get ticks: " + str(time))

        if self.hit == True:
            print("hit == true")
            if self.animate == 0 and time % 55 == 0:
                self.image = pygame.image.load(self.explode[1])
                self.animate += 1
                print ("animate " + str(self.animate))
                print (str(time))

            elif self.animate == 1 and time % 55 == 1:
                self.image = pygame.image.load(self.explode[2])
                self.animate += 1
                print("animate " + str(self.animate))

            elif self.animate == 2 and time % 55 == 0:
                self.image = pygame.image.load(self.explode[3])
                self.animate += 1
                print("animate " + str(self.animate))

            elif self.animate == 3 and time % 55 == 1:
                self.image = pygame.image.load(self.explode[4])
                self.animate += 1
                print("animate " + str(self.animate))

            elif self.animate == 4 and time% 55 == 0:
                self.image = pygame.image.load(self.explode[5])
                self.animate += 1
                print("animate " + str(self.animate))

            elif self.animate == 5 and time% 55 == 1:
                self.image = pygame.image.load(self.explode[6])
                self.animate += 1
                print("animate " + str(self.animate))

            elif self.animate == 6 and time% 55 == 0:
                self.image = pygame.image.load(self.explode[7])
                self.animate += 1
                print("animate " + str(self.animate))

            elif self.animate == 7 and time% 55 == 1:
                self.image = pygame.image.load(self.explode[8])
                self.animate += 1
                print("animate " + str(self.animate))

            elif self.animate == 8 and time% 55 == 0:
                self.image = pygame.image.load(self.explode[9])
                self.animate += 1
                print("animate " + str(self.animate))

            elif self.animate == 9 and time% 55 == 1:
                self.image = pygame.image.load('images/Ship Full.gif')
                print("animate " + str(self.animate))
                self.animate = 0
                self.hit = False

        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.center += self.ai_settings.ship_speed_factor
        if self.moving_left and self.rect.left > 0:
            self.center -= self.ai_settings.ship_speed_factor

        # Update rect object from self.center.
        self.rect.centerx = self.center



    def blitme(self):
        """Draw the ship at its current location."""
        self.screen.blit(self.image, self.rect)
