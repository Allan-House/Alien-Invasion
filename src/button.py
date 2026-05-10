import pygame.font

class Button:
    def __init__(self, game, message):
        """Initialize button attributes."""
        self.screen = game.screen
        self.screen_rect = game.screen.get_rect()

        self.width, self.height = 200, 50
        self.button_colour = (0, 135, 0)
        self.text_colour = (255, 255, 255)
        self.font = pygame.font.SysFont(None, 48)

        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.center = self.screen_rect.center

        self._prep_message(message)

    def draw_button(self):
        """Draw blank button and then draw message."""
        self.screen.fill(self.button_colour, self.rect)
        self.screen.blit(self.message_image, self.message_image_rect)
    
    def _prep_message(self, message):
        """Turn message into a rendered image and center text on the button."""
        self.message_image = self.font.render(message, True, self.text_colour, 
                                              self.button_colour)
        self.message_image_rect = self.message_image.get_rect()
        self.message_image_rect.center = self.rect.center