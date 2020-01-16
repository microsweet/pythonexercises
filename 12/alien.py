import pygame
from pygame.sprite import Sprite


class Alien(Sprite):
    def __init__(self, ai_settings, screen):
        super(Alien, self).__init__()
        self.screen = screen
        self.settings = ai_settings

        #加载图像，设置rect
        self.image = pygame.transform.scale(
            pygame.image.load('image/alien.bmp'), (40, 40))
        self.rect = self.image.get_rect()

        #初始位置
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        #保存准确位置
        self.x = float(self.rect.x)

    def blitme(self):
        self.screen.blit(self.image, self.rect)
