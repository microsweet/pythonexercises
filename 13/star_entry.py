import sys
import pygame
from pygame.sprite import Group
from star import Star


def update_screen(screen, stars):
    screen.fill((255, 255, 255))
    stars.draw(screen)
    pygame.display.flip()


def get_number_x(star_width):
    avaliable_space_x = 800 - star_width
    number_stars_x = int(avaliable_space_x / (2 * star_width))
    return int(number_stars_x)


def get_rows(star_height):
    avaliable_space_y = 600 - 2 * star_height
    number_rows = avaliable_space_y / (2 * star_height)
    return int(number_rows)


def create_star(screen, stars, star_number, row_number):
    star = Star(screen)
    star_width = star.rect.width
    star.x = star_width + 2 * star_width * star_number
    star.rect.x = star.x
    star.rect.y = star.rect.height + 2 * star.rect.height * row_number
    stars.add(star)


def create_stars(screen, stars):
    star = Star(screen)
    stars_number = get_number_x(star.rect.width)
    rows_number = get_rows(star.rect.height)
    for row_number in range(rows_number):
        for star_number in range(stars_number):
            create_star(screen, stars, star_number, row_number)


def run():
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    stars = Group()

    create_stars(screen, stars)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    sys.exit()
        update_screen(screen, stars)


run()
