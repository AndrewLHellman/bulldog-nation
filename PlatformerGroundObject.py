import pygame
from MapObject import MapObject
from Vector3 import Vector3

class PlatformerGroundObject(MapObject):
  def __init__(self):
    self.pos = Vector3(-5000,0,-800)
    self.width = 10000
    self.depth = 0
    self.height = 500
    #self.top_surf = pygame.surface.Surface((width, depth))
    #self.top_surf.fill((0, 0, 255))
    self.side_surf = pygame.surface.Surface((self.width, self.height))
    self.side_surf.fill((0, 0, 0))
    #self.top_rect = self.top_surf.get_rect(center=(self.pos.x+self.width/2, self.pos.y + self.depth/2))
    self.side_rect = self.side_surf.get_rect(center=(self.pos.x, self.pos.z))

  def render(self, screen, camera_view, p_pos):
    if camera_view == 'side':
      render_pos = [self.pos.x - p_pos.x + screen.get_width()/2, -self.pos.z, self.width, self.height]
      # pygame.draw.rect(screen, (0, 0, 255), [self.pos.x - p_pos.x, self.pos.z, self.width, self.height])
      screen.blit(self.side_surf, render_pos)
      print(self.pos.x, self.pos.z)

  def hasTopView(self):
    return False

