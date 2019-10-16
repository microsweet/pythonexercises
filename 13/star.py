import pygame
from pygame.sprite import Sprite

class Star(Sprite):
    def __init__(self, screen):
        super.__init__()
        self.image = pygame.transform.scale(pygame.image.load(), (30, 30))
        self.screen = screen
        self.rect = self.image.get_rect()

        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        self.x = float(self.rect.x)

    def blitme(self):
        self.screen.blit(self.image, self.rect)
        
