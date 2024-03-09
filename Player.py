import pygame
from math import sqrt
from Vector3 import Vector3

MOVE_SPEED = 0.1
SQRT_2 = sqrt(2)
PLAYER_SIZE = 64
Z_ACCEL = -0.00003
MAX_Z_VELOCITY = -3

class Player:
  def __init__(self):
    self.position = Vector3(0,0,-100)
    self.z_velocity = 0


  # Args = direction
  def move(self, vec):
    vec.normalize(MOVE_SPEED)
    self.position.add(vec)

  def update(self, keys, camera_view):
    self.handleKeys(keys, camera_view)
    # print(self.position.z)
    if self.position.z > -100:
      self.z_velocity += Z_ACCEL
      # print(f"z velo: {self.z_velocity}")
      self.z_velocity = max(self.z_velocity, MAX_Z_VELOCITY)
      self.position.z += self.z_velocity
      self.position.z = max(self.position.z, -100)
      # exit(0)
    else:
      self.z_velocity = 0



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
      self.move(Vector3(dx, 0, -dy))

  def render(self, screen, camera_view):
    if camera_view == 'top':
      pygame.draw.rect(screen, (255, 0, 0), [screen.get_width()/2 - PLAYER_SIZE/2, screen.get_height()/2 - PLAYER_SIZE/2, PLAYER_SIZE, PLAYER_SIZE])
    else:
      pygame.draw.rect(screen, (255, 0, 0), [screen.get_width()/2 - PLAYER_SIZE/2, screen.get_height()/2 - PLAYER_SIZE/2 - self.position.z, PLAYER_SIZE, PLAYER_SIZE])
    