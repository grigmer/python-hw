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
startbutton = pygame.Rect(560, 440, 70, 30)
speed  = 20
ismoving = False
circs = [[[255, 100, 0], [40, 40 + 80 * i], 25] for i in range(5)]
speeds = [random.randint(5, 20) for i in range(5)]
winner = None

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
    if ismoving:
        ismoving = False
        for i in range(5):
            if circs[i][1][0] + speeds[i] <= 525:
                circs[i][1][0] += speeds[i]
                ismoving = True
            else:
                circs[i][1][0] = 525
                if winner == None:
                    winner = i
    screen.fill((255, 255, 255))    
    
    pygame.draw.rect(screen, (0, 0, 150), startbutton, 0)
    pygame.draw.rect(screen, (0, 0, 0), (480, 10, 20, 401))
    for i in range(40):
        a = i % 2
        pygame.draw.rect(screen, (255, 255, 255), (481 + a * 9, 11 + i * 10, 9, 9))
    for i in range(5):
        pygame.draw.circle(screen, circs[i][0], circs[i][1], circs[i][2])
    
    if ismoving == False and winner is not None:
        crown(winner, screen, circs)

    pygame.display.flip()