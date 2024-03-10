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
    if not self.map.canPlayerMoveToPosition(self.player.position, self.player, self.camera_view):
      print('INSIDE BLOCK')
      self.map.correctPosition(self.player, self.camera_view)
    if self.camera_view == 'side':
      self.map.fallToNearestObject(self.player, self.camera_view)

  def update(self, keys, screen):
    self.handleKeys(keys)
    self.player.update(keys, self.camera_view, screen, self.map)
    if self.camera_view == 'side':
      self.map.correctPosition(self.player, self.camera_view)

  def handleKeys(self, keys):
    if keys[pygame.K_TAB] and time() - self.tab_last_pressed > 0.5:
      self.tab_last_pressed = time()
      self.toggleCameraView()

