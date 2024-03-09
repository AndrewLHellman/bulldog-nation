import pygame
from MapObject import MapObject


class BoxObject(MapObject):
  def __init__(self, pos, width, depth, height):
    self.pos = pos
    self.width = width
    self.depth = depth
    self.height = height
    self.top_surf = pygame.surface.Surface((width, depth))
    self.top_surf.fill((0, 0, 255))
    self.side_surf = pygame.surface.Surface((width, height))
    self.side_surf.fill((0, 0, 255))
    self.top_rect = self.top_surf.get_rect(center=(self.pos.x+self.width/2, self.pos.y + self.depth/2))
    self.side_rect = self.side_surf.get_rect(center=(self.pos.x, self.pos.z))

  def render(self, screen, camera_view, p_pos):
    if camera_view == 'top':
      render_pos = [self.pos.x - p_pos.x + screen.get_width()/2, self.pos.y - p_pos.y + screen.get_height()/2, self.width, self.depth]
      # pygame.draw.rect(screen, (0, 0, 255), [self.pos.x - p_pos.x, self.pos.y - p_pos.y, self.width, self.height])
      screen.blit(self.top_surf, render_pos)

    else:
      render_pos = [self.pos.x - p_pos.x, self.pos.z, self.width, self.height]
      # pygame.draw.rect(screen, (0, 0, 255), [self.pos.x - p_pos.x, self.pos.z, self.width, self.height])
      screen.blit(self.side_surf, render_pos)
      print(self.pos.x, self.pos.z)
