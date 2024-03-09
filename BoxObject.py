import pygame
from MapObject import MapObject


class BoxObject(MapObject):
  def __init__(self, x, y, width, height):
    self.x = x
    self.y = y
    self.width = width
    self.height = height

  def render(self, screen, px, py):
    pygame.draw.rect(screen, (0, 0, 255), [self.x - px, self.y - py, self.width, self.height])
