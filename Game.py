import pygame
from Map import Map
from Player import Player
from time import time

class Game:
  def __init__(self):
    self.camera_view = 'top'
    self.player = Player()
    self.map = Map()
    self.tab_last_pressed = 0
  
  def render(self, screen):
    self.map.render(screen, self.camera_view, self.player.position)
    self.player.render(screen, self.camera_view)

  def toggleCameraView(self):
    self.camera_view = 'side' if self.camera_view == 'top' else 'top'

  def handleKeys(self, keys):
    self.player.handleKeys(keys, self.camera_view)
    if keys[pygame.K_TAB] and time() - self.tab_last_pressed > 0.5:
      self.tab_last_pressed = time()
      self.toggleCameraView()
