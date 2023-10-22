import sys
import pygame
import random


def crown(n, screen, circlist):
    circ = circlist[n]
    center = circ[1]
    centerX = center[0]
    centerY = center[1]
    r = circ[2]
    pygame.draw.polygon(screen, (255, 255, 0), [(centerX - r, centerY - (r * 0.75)), 
                                                (centerX - r, centerY - (r * 1.5)), 
                                                (centerX - (r * 0.5), centerY - r), 
                                                (centerX, centerY - (r  * 1.5)), 
                                                (centerX + (r * 0.5), centerY - r), 
                                                (centerX + r, centerY - (r * 1.5)), 
                                                (centerX + r, centerY - (r * 0.75))])


pygame.init()



screen = pygame.display.set_mode((640, 480))
rect = pygame.Rect(40, 40, 120, 120)
startbutton = pygame.Rect(560, 440, 70, 30)
speed  = 20
ismoving = False
circs = [[[255, 100, 0], [40, 40 + 80 * i], 25] for i in range(5)]
speeds = [random.randint(5, 20) for i in range(5)]
for i in range(5):
    pygame.draw.circle(screen, circs[i][0], circs[i][1], circs[i][2])


while True:
    pygame.time.delay(30)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if (event.type == pygame.MOUSEBUTTONUP and event.button == 1 and
            (startbutton[0] <= event.pos[0] <= startbutton[0] + startbutton[2])
            and (startbutton[1] <= event.pos[1] <= startbutton[1] + startbutton[3])):
            ismoving = True
    if ismoving and rect[0] <= 500:
        rect[0] += speed
        screen.fill((0, 0, 0))
    pygame.draw.rect(screen, (0, 0, 150), startbutton, 0)
    pygame.draw.rect(screen, (255, 0, 0), rect, 0)
    pygame.display.flip()