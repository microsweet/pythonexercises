import sys
import pygame
from bullet import Bullet

#监听键盘鼠标事件
def check_event(ship, ai_settings, screen, bullets):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            key_down(event, ship, ai_settings, screen, bullets)
        elif event.type == pygame.KEYUP:
            key_up(event, ship)

#刷新屏幕
def update_screen(ai_settings, screen, ship, bullets):
    screen.fill(ai_settings.bg_color)

    for bullet in bullets.sprites():
        bullet.draw_bullet()

    ship.blitme()
    pygame.display.flip()

#键盘按下
def key_down(event, ship, ai_settings, screen, bullets):
    #print(event.key)
    if event.key == pygame.K_q:
        sys.exit()
    elif event.key == pygame.K_RIGHT:
        ship.move_right = True
    elif event.key == pygame.K_LEFT:
        ship.move_left = True
    elif event.key == pygame.K_UP:
        ship.move_top = True
    elif event.key == pygame.K_DOWN:
        ship.move_bottom = True
    elif event.key == pygame.K_SPACE:
        fire_bullet(ai_settings, screen, ship, bullets)

#键盘抬起
def key_up(event, ship):
    if event.key == pygame.K_RIGHT:
        ship.move_right = False
    elif event.key == pygame.K_LEFT:
        ship.move_left = False
    elif event.key == pygame.K_UP:
        ship.move_top = False
    elif event.key == pygame.K_DOWN:
        ship.move_bottom = False

def update_bullets(bullets):
    bullets.update()

    #删除消失的子弹
    for bullet in bullets.copy():
        if bullet.rect.bottom<=0:
            bullets.remove(bullet)

def fire_bullet(ai_settings, screen, ship, bullets):
    if len(bullets) < ai_settings.bullet_allowed:
        new_bullet = Bullet(ai_settings, screen, ship)
        bullets.add(new_bullet)
