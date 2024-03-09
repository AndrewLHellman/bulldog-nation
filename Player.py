import pygame
from math import sqrt
from Vector3 import Vector3

MOVE_SPEED = 0.05
SQRT_2 = sqrt(2)
PLAYER_SIZE = 64

class Player:
  def __init__(self):
    self.position = Vector3(0,0,0)


  # Args = direction
  def move(self, vec):
    vec.normalize(MOVE_SPEED)
    self.position.add(vec)

  def handleKeys(self, keys, camera_view):
    dx = 0
    dy = 0 # y is the non-x direction here
    if keys[pygame.K_w]:
      dy = -1
    elif keys[pygame.K_s]:
      dy = 1
    if keys[pygame.K_d]:
      dx = 1
    elif keys[pygame.K_a]:
      dx = -1
    if camera_view == 'top':
      self.move(Vector3(dx, dy, 0))
    else:
      self.move(Vector3(dx, 0, dy))

  def render(self, screen, camera_view):
    if camera_view == 'top':
      pygame.draw.rect(screen, (255, 0, 0), [screen.get_width()/2 - PLAYER_SIZE/2, screen.get_height()/2 - PLAYER_SIZE/2, PLAYER_SIZE, PLAYER_SIZE])
    else:
      pygame.draw.rect(screen, (255, 0, 0), [screen.get_width()/2 - PLAYER_SIZE/2, screen.get_height()/2 - PLAYER_SIZE/2 + self.position.z, PLAYER_SIZE, PLAYER_SIZE])
    