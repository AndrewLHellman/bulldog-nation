import pygame
from Map import Map
from Player import Player
from time import time

pygame.font.init()
font = pygame.font.SysFont('sourcecodepro', 42)
class Game:
  def __init__(self, screen):
    self.camera_view = 'top'
    self.player = Player(screen)
    self.map = Map()
    self.tab_last_pressed = 0
    img = pygame.image.load('source/sprites/CameraOverlayTop.png')
    img.set_colorkey((0,0,0))
    img.set_alpha(128)
    self.camera_surf_top = pygame.transform.scale(img, (1920, 1080))
    img = pygame.image.load('source/sprites/CameraOverlaySide.png')
    img.set_colorkey((0,0,0))
    img.set_alpha(128)
    self.camera_surf_side = pygame.transform.scale(img, (1920, 1080))
  
  def render(self, screen):
    self.map.render(screen, self.camera_view, self.player.position)
    self.player.render(screen, self.camera_view)
    if self.camera_view == 'top':
      # screen.blit(self.camera_surf_top, (0,0))
      text_surface = font.render("REC", False, (255, 255, 255))
      screen.blit(text_surface, (1700,980))
    
      text_surface = font.render("TOP", False, (255, 255, 255))
      screen.blit(text_surface, (200,980))
      # screen.blit()


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

