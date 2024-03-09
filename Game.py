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
    self.player.update(keys, self.camera_view, screen)

  def handleKeys(self, keys):
    if keys[pygame.K_TAB] and time() - self.tab_last_pressed > 0.5:
      self.tab_last_pressed = time()
      self.toggleCameraView()

  def detectPlayerCollision(self):
    if (self.camera_view == 'top'):
      for object in self.map.objects:
        if (self.player.top_rect.colliderect(object.topRect)):
          object.topSurf.fill((0, 255, 0))
        else:
          object.topSurf.fill((0, 0, 255))
          #print("Boom!")
    elif (self.camera_view == 'side'):
      for object in self.map.objects:
        if (self.player.side_rect.colliderect(object.sideRect)):
          object.sideSurf.fill((0, 255, 0))
          #print("Boom!")
