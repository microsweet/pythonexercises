import pygame
import time
from pygame.sprite import Group
from settings import Settings
from ship import Ship
import game_function as gf

def run_game():
    
    #初始化游戏
    pygame.init()
    #游戏设置类
    ai_settings = Settings()
    #设置游戏屏幕大小
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")
    #初始化飞船类
    ship = Ship(screen)
    #创建存储子弹编组
    bullets = Group()

    #游戏主循环
    while True:
        #监听鼠标键盘方法
        gf.check_event(ship, ai_settings, screen, bullets)
        #更新飞船位置
        ship.update()
        #更新子弹位置
        gf.update_bullets(bullets)
        #刷新屏幕
        gf.update_screen(ai_settings, screen, ship, bullets)
        time.sleep(0.005)

run_game()
