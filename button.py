import pygame.font
class Button():
    def __init__(self, ai_settings, screen, msg):
        """Initialize button attributes."""
        self.screen = screen
        self.screen_rect = screen.get_rect()

        # Set the dimensions and properties of the button.
        self.width, self.height = 200, 50
        self.button_color = (0, 255, 0)
        self.text_color = (255, 255, 255)
        self.font = pygame.font.SysFont(None, 48)

        # Build the button's rect object and center it.
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.center = self.screen_rect.center
        self.rect.centery = self.screen_rect.centery + 200

        # The button message needs to be prepped only once.
        self.prep_msg(msg)
        # self.prep_high_label()

    def prep_msg(self, msg):
        """Turn msg into a rendered image and center text on the button."""

        self.msg_image = self.font.render(msg, True, self.text_color,
            self.button_color)

        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center

    def prep_high_label(self):
        high_str = "Hi Score:"
        self.high_str_image = self.font.render(high_str, True,
                   self.text_color, self.button_color)

        self.high_str_rect = self.high_str_image.get_rect()
        self.high_str_rect.centerx = self.screen_rect.centerx
        self.high_str_rect.centery = self.screen_rect.bottom - 60


    def draw_button(self):
        # Draw blank button and then draw message.
        self.screen.fill(self.button_color, self.rect)
        self.screen.blit(self.msg_image, self.msg_image_rect)
        # self.screen.blit(self.high_str_image, self.high_str_rect)

class Button2():
    def __init__(self, ai_settings, screen):
        """Initialize button attributes."""
        self.screen = screen
        self.screen_rect = screen.get_rect()

        # Set the dimensions and properties of the button.
        self.width, self.height = 200, 50
        self.button_color = (0, 255, 0)
        self.text_color = (255, 255, 255)
        self.font = pygame.font.SysFont(None, 48)

        # Build the button's rect object and center it.
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.center = self.screen_rect.center
        self.rect.centery = self.screen_rect.bottom - 70

        # The button message needs to be prepped only once.
        # self.prep_msg(msg)
        self.prep_high_label()

    def prep_high_label(self):
        high_str = "Hi Score:"
        self.high_str_image = self.font.render(high_str, True,
                   self.text_color, self.button_color)

        self.high_str_rect = self.high_str_image.get_rect()
        self.high_str_rect.centerx = self.screen_rect.centerx
        self.high_str_rect.centery = self.screen_rect.bottom - 70


    def draw_button(self):
        # Draw blank button and then draw message.
        self.screen.fill(self.button_color, self.rect)
        # self.screen.blit(self.msg_image, self.msg_image_rect)
        self.screen.blit(self.high_str_image, self.high_str_rect)