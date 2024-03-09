import pygame
from Map import Map
from Player import Player
from time import time

class Game:
  def __init__(self, screen):
    self.camera_view = 'top'
    self.player = Player(screen)
    self.map = Map()
    self.tab_last_pressed = 0
  
  def render(self, screen):
    self.map.render(screen, self.camera_view, self.player.position)
    self.player.render(screen, self.camera_view)

  def toggleCameraView(self):
    self.camera_view = 'side' if self.camera_view == 'top' else 'top'

  def update(self, keys, screen):
    self.handleKeys(keys)
    self.player.update(keys, self.camera_view, screen, self.map)

  def handleKeys(self, keys):
    if keys[pygame.K_TAB] and time() - self.tab_last_pressed > 0.5:
      self.tab_last_pressed = time()
      self.toggleCameraView()

<<<<<<< HEAD
=======
  def detectPlayerCollision(self):
    if (self.camera_view == 'top'):
      for object in self.map.objects:
        if not object.hasTopView():
          continue
        if (self.player.top_rect.colliderect(object.top_rect)):
          object.top_surf.fill((0, 255, 0))
        else:
          object.top_surf.fill(object.color)
          #print("Boom!")
    elif (self.camera_view == 'side'):
      for object in self.map.objects:
        if (self.player.side_rect.colliderect(object.side_rect)):
          object.side_surf.fill((0, 255, 0))
          #print("Boom!")
          pass
        else:
          if hasattr(object, 'color'):
            object.side_surf.fill(object.color)
>>>>>>> cb9df0b48973ae7da1b97be1835d0b03e222b478
