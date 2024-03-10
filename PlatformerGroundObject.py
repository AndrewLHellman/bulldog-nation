import pygame
from MapObject import MapObject
from Vector3 import Vector3
from random import randint

class PlatformerGroundObject(MapObject):
  def __init__(self, x, y, floortexture):
    self.pos = Vector3(x , y,200)
    self.width = 256
    self.depth = 256
    self.height = 500
    self.top_surf = pygame.surface.Surface((self.width, self.depth))
    img = pygame.image.load(f'./source/sprites/TopDownFloor-{floortexture}.png').convert()
    self.top_surf.blit(pygame.transform.scale(img, (self.width, self.depth)), (0 , 0))
    #self.top_surf.fill(self.color)
    self.side_surf = pygame.surface.Surface((self.width, self.height))
    # self.side_surf.fill(self.color)
    self.top_rect = None
    img = pygame.image.load('./source/sprites/BackgroundFloorFinal.png').convert()
    self.side_surf.blit(pygame.transform.scale(img, (self.width, 300)), (0, 0))
    self.side_rect = self.side_surf.get_rect(center=(self.pos.x + self.width/2, self.pos.z + self.height/2 + 10))

  def render(self, screen, camera_view, p_pos):
    if camera_view == 'top':
      render_pos = [self.pos.x - p_pos.x + screen.get_width()/2, self.pos.y  + screen.get_height()/2, self.width, self.depth]
      screen.blit(self.top_surf, render_pos)
    if camera_view == 'side':
      render_pos = [self.pos.x - p_pos.x + screen.get_width()/2, screen.get_height()/2 + self.pos.z, self.width, self.height]
      # pygame.draw.rect(screen, (0, 0, 255), [self.pos.x - p_pos.x, self.pos.z, self.width, self.height])
      screen.blit(self.side_surf, render_pos)
      # print(self.pos.x, self.pos.z)

  def hasTopView(self):
    return False

