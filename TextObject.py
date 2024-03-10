from MapObject import MapObject
import pygame

font = pygame.font.SysFont('sourcecodepro', 30)
class TextObject(MapObject):
  def __init__(self, pos, text):
    self.pos = pos
    self.text = text
    self.text_surface = font.render(self.text, False, (255,255,255))
    self.top_rect = None
    self.side_rect = None

  def render(self, screen, camera_view, p_pos):
    if camera_view == 'top':
      screen.blit(self.text_surface, (self.pos.x + screen.get_width()/2 - p_pos.x, self.pos.y + screen.get_height()/2))
    else:
      screen.blit(self.text_surface, (self.pos.x + screen.get_width()/2 - p_pos.x, self.pos.z + screen.get_height()/2))
    

  def hasTopView(self):
    return True
