import sys
import pygame
from pygame.sprite import Group
from star import Star

def update_screen(screen, stars):
    screen.fill('#000')
    starts.draw(screen)

def get_number_x(star_width):
    avaliable_space_x = 800 - star_width
    number_starts_x = int(avaliable_space_x/(2 * star_width))
    return number_starts_x

def get_rows(star_height):
    avaliable_space_y = 600 - 2 * star_height
    number_rows = avaliable_space_y / (2 * star_height)
    return number_rows

def create_star(screen, starts, stars_number, row_number):
    star = Star(screen)
    star_width = star.rect.width
    star.x = star_width + 2 * star_width * stars_number
    star.rect.x = start.x
    star.rect.y = star.rect.height + 2 * star.rect.height * row_number
    stars.add(star)

def run():
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    stars = Group()

    while True:


run()
