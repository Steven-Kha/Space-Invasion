import pygame
from pygame.sprite import Sprite

class UFO(Sprite):
    """A class to represent a single alien in the fleet."""

    def __init__(self, ai_settings, screen):
        """Initialize the alien and set its starting position."""
        super(UFO, self).__init__()
        self.screen = screen
        self.ai_settings = ai_settings

        # Load the alien image and set its rect attribute.
        self.UFO = ['images/UFO.gif', 'images/PTS.png']
        self.image = pygame.image.load(self.UFO[0])
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        # Start each new alien near the top left of the screen.
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # self.rect.centerx = self.screen_rect.centerx
        # self.rect.bottom = self.screen_rect.bottom

        self.rect.x = self.screen_rect.left
        self.rect.y = self.screen_rect.top

        # Store the alien's exact position.
        self.x = float(self.rect.x)
        self.hit = False

    # def check_edges(self):
    #     """Return True if alien is at edge of screen."""
    #     screen_rect = self.screen.get_rect()
    #     if self.rect.right >= screen_rect.right:
    #         return True
    #     elif self.rect.left <= 0:
    #         return True

    def explosion(self):
        self.hit = True
        print("Yellow destroyed")

    def animate(self):
        self.animate = 0

    def update(self):
        """Move the alien right or left."""
        if self.hit == True:
            self.image = pygame.image.load(self.UFO[1])
            self.hit == False

        self.x += (self.ai_settings.alien_speed_factor *
                        self.ai_settings.fleet_direction)
        self.rect.x = self.x


    def blitme(self):
        """Draw the alien at its current location."""
        self.screen.blit(self.image, self.rect)