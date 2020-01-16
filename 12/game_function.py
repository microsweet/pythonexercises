import sys
import pygame
from bullet import Bullet
from alien import Alien


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
def update_screen(ai_settings, screen, ship, aliens, bullets):
    screen.fill(ai_settings.bg_color)

    for bullet in bullets.sprites():
        bullet.draw_bullet()

    ship.blitme()
    aliens.draw(screen)
    pygame.display.flip()


#键盘按下
def key_down(event, ship, ai_settings, screen, bullets):
    #print(event.key)
    if event.key == pygame.K_q:
        sys.exit()
    elif event.key == pygame.K_i:
        ship.move_top = True
    elif event.key == pygame.K_k:
        ship.move_bottom = True
    elif event.key == pygame.K_j:
        ship.move_left = True
    elif event.key == pygame.K_l:
        ship.move_right = True
    elif event.key == pygame.K_SPACE:
        fire_bullet(ai_settings, screen, ship, bullets)


#键盘抬起
def key_up(event, ship):
    if event.key == pygame.K_i:
        ship.move_top = False
    elif event.key == pygame.K_k:
        ship.move_bottom = False
    elif event.key == pygame.K_j:
        ship.move_left = False
    elif event.key == pygame.K_l:
        ship.move_right = False


def update_bullets(bullets):
    bullets.update()

    #删除消失的子弹
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)


def fire_bullet(ai_settings, screen, ship, bullets):
    if len(bullets) < ai_settings.bullet_allowed:
        new_bullet = Bullet(ai_settings, screen, ship)
        bullets.add(new_bullet)


def get_number_aliens_x(ai_settings, alien_width):
    avaliable_space_x = ai_settings.screen_width - alien_width
    number_aliens_x = int(avaliable_space_x / (2 * alien_width))
    return number_aliens_x


def get_number_rows(ai_settings, ship_height, alien_height):
    #计算可容纳多少行外星人
    avaliable_space_y = (ai_settings.screen_height - (3 * alien_height) -
                         ship_height)
    number_rows = int(avaliable_space_y / (2 * alien_height))
    return number_rows


def create_alien(ai_settings, screen, aliens, alien_number, row_number):
    #创建一个外星人并将其放在当前行
    alien = Alien(ai_settings, screen)
    alien_width = alien.rect.width
    alien.x = alien_width + 2 * alien_width * alien_number
    alien.rect.x = alien.x
    alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_number
    aliens.add(alien)


def create_fleet(ai_settings, screen, ship, aliens):
    #创建一个外星人，并计算一行可以容纳多少个外星人
    #外星人间距为外星人宽度
    alien = Alien(ai_settings, screen)
    number_aliens_x = get_number_aliens_x(ai_settings, alien.rect.width)
    number_rows = get_number_rows(ai_settings, ship.rect.height,
                                  alien.rect.height)

    for row_number in range(number_rows):
        for alien_number in range(number_aliens_x):
            create_alien(ai_settings, screen, aliens, alien_number, row_number)
