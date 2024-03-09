import pygame
from MapObject import MapObject


class BoxObject(MapObject):
  def __init__(self, pos, width, height):
    self.pos = pos
    self.width = width
    self.height = height

  def render(self, screen, camera_view, p_pos):
    if camera_view == 'top':
      pygame.draw.rect(screen, (0, 0, 255), [self.pos.x - p_pos.x, self.pos.y - p_pos.y, self.width, self.height])
    else:
      pygame.draw.rect(screen, (0, 0, 255), [self.pos.x - p_pos.x, self.pos.z, self.width, self.height])
