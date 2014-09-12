import os
import pygame
import util.sprite

class Player(pygame.sprite.Sprite):

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)

        # Player sprite sheet: 8x12px 7 frames
        playerSpriteSheet = util.sprite.SpriteSheet(os.path.join('sprites', 'player.png'), pygame.Rect(0,0,8,12), 7)

        self._playerAnim = util.sprite.SpriteAnimation((
            (playerSpriteSheet.frame(0), 3000),
            (playerSpriteSheet.frame(1), 100),
            (playerSpriteSheet.frame(2), 100),
            (playerSpriteSheet.frame(3), 100),
            (playerSpriteSheet.frame(1), 100),
            (playerSpriteSheet.frame(2), 100),
            (playerSpriteSheet.frame(3), 100),
            (playerSpriteSheet.frame(1), 100),
            (playerSpriteSheet.frame(2), 100),
            (playerSpriteSheet.frame(3), 100),
        ), True)

        self._playerWalkAnim = util.sprite.SpriteAnimation((
            (playerSpriteSheet.frame(4), 200),
            (playerSpriteSheet.frame(5), 200)
        ), True)

        self._playerJumpAnim = util.sprite.SpriteAnimation((
            (playerSpriteSheet.frame(6), 200),
            (playerSpriteSheet.frame(0), 0)
        ))

        self.image = playerSpriteSheet.frame(0)
        self.rect = playerSpriteSheet.get_rect()

        self._animation = self._playerAnim
        self._animation.start()

        self._walk = 0

    def jump(self):
        self._animation = self._playerJumpAnim
        self._animation.start()

    def start_walking(self, direction):
        self._animation = self._playerWalkAnim
        self._animation.start()
        self._walk = direction

    def stop_walking(self):
        if self._animation: self._animation.stop()
        self._walk = 0

    def update(self, *args):
        if self._animation and self._animation.is_running():
            self._animation.update()
            self.image = self._animation.image()
        else:
            self._animation = self._playerAnim
            self._animation.start()