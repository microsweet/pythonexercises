#飞船类
import pygame


class Ship():
    def __init__(self, ai_settings, screen):
        self.screen = screen

        #读取飞船图片
        #self.image = pygame.image.load('image/ship.bmp')
        self.image = pygame.transform.scale(
            pygame.image.load('image/ship.bmp'), (50, 50))
        #获取飞船图片矩形
        self.rect = self.image.get_rect()
        #获取屏幕矩形
        self.screen_rect = screen.get_rect()

        #设置飞船初始化位置
        self.rect.centerx = self.screen_rect.centerx
        self.rect.centery = self.screen_rect.centery
        self.rect.bottom = self.screen_rect.bottom

        #存储移动飞船时的x、y坐标
        self.centerx = float(self.rect.centerx)
        self.centery = float(self.rect.centery)

        #是否移动标识
        self.move_right = False
        self.move_left = False
        self.move_top = False
        self.move_bottom = False

        #飞船移动速度
        self.speed = ai_settings.ship_speed

    #指定位置绘制飞船
    def blitme(self):
        #设置图片大小
        #image = pygame.transform.scale(self.image,(50, 50))
        self.screen.blit(self.image, self.rect)

    #更新飞船位置属性
    def update(self):
        if self.move_right and self.rect.right < self.screen_rect.right:
            self.centerx += self.speed
        if self.move_left and self.rect.left > self.screen_rect.left:
            self.centerx -= self.speed
        if self.move_top and self.rect.top > self.screen_rect.top:
            self.centery -= self.speed
        if self.move_bottom and self.rect.bottom < self.screen_rect.bottom:
            self.centery += self.speed

        self.rect.centerx = self.centerx
        self.rect.centery = self.centery
