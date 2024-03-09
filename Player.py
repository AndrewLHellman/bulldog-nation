import pygame
from math import sqrt
from Vector3 import Vector3

MOVE_SPEED = 1
THRUST_SPEED = 2
SQRT_2 = sqrt(2)
PLAYER_SIZE = 64
Z_ACCEL = -0.002
MAX_Z_VELOCITY = -3

pygame.font.init()
my_font = pygame.font.SysFont('Comic Sans MS', 30)

class Player:
  def __init__(self, screen):
    self.position = Vector3(0,0,-100)
    self.z_velocity = 0
    self.top_surf = pygame.surface.Surface((PLAYER_SIZE, PLAYER_SIZE))
    self.top_surf.fill((255, 0, 0))
    self.side_surf = pygame.image.load('./source/sprites/playerSideRight.png').convert()
    self.side_surf.set_colorkey((0, 0, 0))
    self.top_rect = self.top_surf.get_rect(center=(self.position.x + PLAYER_SIZE/2, self.position.y + PLAYER_SIZE/2))
    self.side_rect = self.side_surf.get_rect(center=(self.position.x, self.position.z))
    self.render_pos = Vector3(screen.get_width()/2 - PLAYER_SIZE/2, screen.get_height()/2 - PLAYER_SIZE/2, screen.get_height()/2 - PLAYER_SIZE/2 - self.position.z)
    # self.top_render_pos = [screen.get_width()/2 - PLAYER_SIZE/2, screen.get_height()/2 - PLAYER_SIZE/2, PLAYER_SIZE, PLAYER_SIZE]
    # self.side_render_pos = [screen.get_width()/2 - PLAYER_SIZE/2, screen.get_height()/2 - PLAYER_SIZE/2 - self.position.z, PLAYER_SIZE, PLAYER_SIZE]


  # Args = direction
  def move(self, vec):
    vec.normalize_xy(MOVE_SPEED)
    vec.z *= THRUST_SPEED
    self.position.add(vec)

  def update(self, keys, camera_view, screen):
    self.handleKeys(keys, camera_view)
    # print(self.position.z)
    if self.position.z > -200:
      self.z_velocity += Z_ACCEL
      # print(f"z velo: {self.z_velocity}")
      self.z_velocity = max(self.z_velocity, MAX_Z_VELOCITY)
      self.position.z += self.z_velocity
      # exit(0)
    else:
      self.z_velocity = 0
    self.position.z = max(self.position.z, -200)
    print(f"Player ({self.position.x}, {self.position.y}, {self.position.z})")
    self.top_rect.update((self.position.x - (self.top_rect.width)/2, self.position.y - self.top_rect.height/2), (self.top_rect.width, self.top_rect.height))
    self.side_rect.update((self.position.x - (self.side_rect.width)/2, self.position.z - self.side_rect.height/2), (self.side_rect.width, self.side_rect.height))
    self.render_pos = Vector3(screen.get_width()/2 - PLAYER_SIZE/2, screen.get_height()/2 - PLAYER_SIZE/2, screen.get_height()/2 - PLAYER_SIZE/2 - self.position.z)


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
      screen.blit(self.top_surf, [self.render_pos.x, self.render_pos.y, PLAYER_SIZE, PLAYER_SIZE])
    else:
      screen.blit(self.side_surf, [self.render_pos.x, self.render_pos.z, PLAYER_SIZE, PLAYER_SIZE])
      print(self.position.x, self.position.z)
    text_surface = my_font.render("(%.2f, %.2f, %.2f)" % (self.position.x, self.position.y, self.position.z), False, (0, 0, 0))
    screen.blit(text_surface, (0,0))
    