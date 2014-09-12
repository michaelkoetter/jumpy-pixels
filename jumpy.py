import sys, os, math
import pygame
import led.sim

import game.player

from pygame.locals import *

size = (90, 20)

pygame.init()

simDisplay = led.sim.SimDisplay(size)
screen = pygame.Surface(size)
fpsClock = pygame.time.Clock()

def main():

    player = game.player.Player()
    player.rect.bottom = screen.get_height() - 1
    player.rect.left = 3

    stage = pygame.sprite.Group()
    stage.add(player)

    hposition = 0
    vposition = 0
    jumpHeight = 10

    backgroundTile = pygame.image.load(os.path.join('sprites', 'background.png'))
    hmove = 0
    vmove = 0

    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == KEYDOWN:
                if event.key == K_LEFT:
                    player.start_walking(-1)
                    hmove = -1
                elif event.key == K_RIGHT:
                    player.start_walking(1)
                    hmove = 1
                elif event.key == K_SPACE:
                    player.jump()
                    vmove = 1
            elif event.type == KEYUP:
                if event.key == K_LEFT or event.key == K_RIGHT:
                    player.stop_walking()
                    hmove = 0

        # draw background

        # handle movement
        vposition += vmove
        if vposition >= jumpHeight:
            vmove = vmove * -1
            vposition = jumpHeight
        elif vposition <= 0:
            vmove = 0
            vposition = 0

        hposition += hmove

        hoffset = - (hposition % backgroundTile.get_width())
        voffset = vposition % backgroundTile.get_height() - 10

        while (hoffset < screen.get_width()):
            screen.blit(backgroundTile, (hoffset, voffset))
            hoffset += backgroundTile.get_width()

        stage.update()
        stage.draw(screen)
        simDisplay.update(screen)
        fpsClock.tick(30)

main()