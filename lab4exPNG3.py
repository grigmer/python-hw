import pygame
from pygame.draw import *

pygame.init()

FPS = 30
screen = pygame.display.set_mode((1032, 768))

rect(screen, (150, 240, 255), (0, 0, 1032, 350))
rect(screen, (0, 250, 100), (0, 350, 1032, 418))
ellipse(screen, (100, 100, 255), (300, 250, 124, 300))
polygon(screen, (255, 0, 200), [(650, 250), (730, 550), (570, 550)])
circle(screen, (255, 223, 196), (362, 230), 55)
circle(screen, (255, 223, 196), (650, 230), 55)
lines(screen, (0, 0, 0), False, [(340, 540), (280, 730), (250, 732)])
lines(screen, (0, 0, 0), False, [(384, 540), (420, 730), (450, 731)])
lines(screen, (0, 0, 0), False, [(620, 550), (620, 730), (590, 730)])
lines(screen, (0, 0, 0), False, [(680, 550), (680, 730), (710, 730)])
line(screen, (0, 0, 0), (315, 315), (200, 450))
lines(screen, (0, 0, 0), False, [(409, 315), (514, 450), (635, 315)])
lines(screen, (0, 0, 0), False, [(665, 315), (735, 390), (830, 320)])
line(screen, (0, 0, 0), (825, 335), (850, 200))
polygon(screen, (255, 0, 0), [(850, 200), (830, 130), (890, 140)])
circle(screen, (255, 0, 0), (848, 115), 25)
circle(screen, (255, 0, 0), (877, 120), 25)
polygon(screen, (255, 255, 0), [(205,455), (162, 417), (206, 396)])
circle(screen, (255, 0, 0), (195, 395), 15)
circle(screen, (100, 0, 0), (169, 408), 14.5)
circle(screen, (255, 255, 255), (175, 383), 15)
 


pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()