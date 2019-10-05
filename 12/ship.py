import pygame

class Ship():
    def __init__(self, screen):
        self.screen = screen

        self.image = pygame.image.load('/home/ms/pythonexercises/12/image/ship.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        self.rect.centerx = self.screen_rect.centerx
        self.rect.centery = self.screen_rect.centery
        self.rect.bottom = self.screen_rect.bottom

        self.centerx = float(self.rect.centerx)
        self.centery = float(self.rect.centery)

        self.move_right = False
        self.move_left = False
        self.move_top = False
        self.move_bottom = False

        self.speed = 1.5

    def blitme(self):
        self.screen.blit(self.image, self.rect);

    def update(self):
        if self.move_right and self.rect.right<self.screen_rect.right:
            self.centerx += self.speed
        if self.move_left and self.rect.left>self.screen_rect.left:
            self.centerx -= self.speed
        if self.move_top and self.rect.top>self.screen_rect.top:
            self.centery -= self.speed
        if self.move_bottom and self.rect.bottom<self.screen_rect.bottom:
            self.centery += self.speed

        self.rect.centerx = self.centerx
        self.rect.centery = self.centery

