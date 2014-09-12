import pygame

class SpriteSheet:
    def __init__(self, filename, rect, countX = 1, countY = 1):
        self._sheet = pygame.image.load(filename)
        self._frames = []
        self._rect = rect
        for x in range(countX):
            for y in range(countY):
                _rect = rect.move(x * rect.width, y * rect.height)
                self._frames.append(self._sheet.subsurface(_rect))


    def get_rect(self):
        return self._rect

    def frame(self, at):
        return self._frames[at]

class SpriteAnimation:
    def __init__(self, frames, loop = False):
        self._frames = frames
        self._running = False
        self._loop = loop

    def start(self):
        self._currentFrame = 0
        self._shown = pygame.time.get_ticks()
        self._running = True

    def stop(self):
        self._running = False

    def image(self):
        return self._frames[self._currentFrame][0]

    def advance_frame(self):
        self._currentFrame += 1
        self._shown = pygame.time.get_ticks()
        if self._currentFrame >= len(self._frames):
            if self._loop:
                self._currentFrame = 0
            else:
                self._currentFrame -= 1
                self._running = False

    def is_running(self):
        return self._running

    def update(self):
        if self._running:
            _frame = self._frames[self._currentFrame]
            _frameDuration = _frame[1]
            _elapsed = pygame.time.get_ticks() - self._shown
            if (_elapsed >= _frameDuration):
                self.advance_frame()
