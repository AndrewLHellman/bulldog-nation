import pygame
from MapObject import MapObject


class BoxObject(MapObject, pygame.sprite.Sprite):
  def __init__(self, pos, dims, color = (0, 0, 0), collectable = False, top_image = '', side_image = '', transparent = False):
    super(BoxObject, self).__init__()
    self.pos = pos
    self.width = dims.x
    self.depth = dims.y
    self.height = dims.z
    self.color = (color)
    self.collectable = collectable
    self.top_surf = pygame.surface.Surface((self.width, self.depth))
    if not top_image:
      self.top_surf.fill(self.color)
    else:
      img = pygame.image.load(f'{top_image}').convert()
      img.set_colorkey((0,0,0))
      self.top_surf = pygame.transform.scale(img, (self.width, self.depth))
    self.side_surf = pygame.surface.Surface((self.width, self.height))
    if not side_image:
      self.side_surf.fill(self.color)
    else:
      img = pygame.image.load(f'{side_image}').convert()
      img.set_colorkey((0,0,0))
      self.side_surf = pygame.transform.scale(img, (self.width, self.height))
    if transparent:
      self.side_surf.set_colorkey(color)
      self.top_surf.set_colorkey(color)
    self.top_rect = self.top_surf.get_rect(center=(self.pos.x + self.width/2, self.pos.y + self.depth/2))
    self.side_rect = self.side_surf.get_rect(center=(self.pos.x + self.width/2, self.pos.z + self.height/2))

  def render(self, screen, camera_view, p_pos):
    if camera_view == 'top':
      render_pos = [self.pos.x - p_pos.x + screen.get_width()/2, self.pos.y + screen.get_height()/2, self.width, self.depth]
      # pygame.draw.rect(screen, (0, 0, 255), [self.pos.x - p_pos.x, self.pos.y - p_pos.y, self.width, self.height])
      screen.blit(self.top_surf, render_pos)

    else:
      render_pos = [self.pos.x - p_pos.x + screen.get_width()/2, screen.get_height()/2 + self.pos.z, self.width, self.height]
      # pygame.draw.rect(screen, (0, 0, 255), [self.pos.x - p_pos.x, self.pos.z, self.width, self.height])
      screen.blit(self.side_surf, render_pos)
      # print(self.pos.x, self.pos.z)
