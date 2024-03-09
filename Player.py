import pygame
from math import sqrt

MOVE_SPEED = 0.05
SQRT_2 = sqrt(2)

class Player:
  def __init__(self):
    self.x = 0
    self.y = 0


  # Args = direction
  def move(self, dx, dy):
    if dx != 0 and dy != 0:
      dx = MOVE_SPEED / SQRT_2
      dy = MOVE_SPEED / SQRT_2
    else:
      dx *= MOVE_SPEED
      dy *= MOVE_SPEED
    self.x += dx
    self.y += dy

  def handleKeys(self, keys):
    dx = 0
    dy = 0
    if keys[pygame.K_w]:
      dy = -1
    elif keys[pygame.K_s]:
      dy = 1
    if keys[pygame.K_d]:
      dx = 1
    elif keys[pygame.K_a]:
      dx = -1
    self.move(dx, dy)
    