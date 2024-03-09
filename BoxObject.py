import pygame
from MapObject import MapObject


class BoxObject(MapObject):
  def __init__(self, pos, width, depth, height):
    self.pos = pos
    self.width = width
    self.depth = depth
    self.height = height
    self.topSurf = pygame.surface.Surface((width, depth))
    self.topSurf.fill((0, 0, 255))
    self.sideSurf = pygame.surface.Surface((width, height))
    self.sideSurf.fill((0, 0, 255))
    self.topRect = self.topSurf.get_rect(center=(self.pos.x+self.width/2, self.pos.y + self.depth/2))
    self.sideRect = self.sideSurf.get_rect(center=(self.pos.x, self.pos.z))

  def render(self, screen, camera_view, p_pos):
    if camera_view == 'top':
      render_pos = [self.pos.x - p_pos.x + screen.get_width()/2, self.pos.y - p_pos.y + screen.get_height()/2, self.width, self.depth]
      # pygame.draw.rect(screen, (0, 0, 255), [self.pos.x - p_pos.x, self.pos.y - p_pos.y, self.width, self.height])
      screen.blit(self.topSurf, render_pos)

    else:
      render_pos = [self.pos.x - p_pos.x, self.pos.z, self.width, self.height]
      # pygame.draw.rect(screen, (0, 0, 255), [self.pos.x - p_pos.x, self.pos.z, self.width, self.height])
      screen.blit(self.sideSurf, render_pos)
      print(self.pos.x, self.pos.z)
