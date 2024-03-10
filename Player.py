import pygame
from math import sqrt
from Vector3 import Vector3

MOVE_SPEED = 5
THRUST_SPEED = -7.5
SQRT_2 = sqrt(2)
PLAYER_SIZE = 96
Z_ACCEL = 0.015
MAX_Z_VELOCITY = 25

pygame.font.init()
my_font = pygame.font.SysFont('Comic Sans MS', 30)

class Player:
  def __init__(self, screen):
    self.position = Vector3(0,0, 200-PLAYER_SIZE)
    self.z_velocity = 0
    self.top_img = {}
    self.side_img = {}
    for dir in ['North', 'South', 'East', 'West']:
      img = pygame.image.load(f'./source/sprites/PlayerRobotTop{dir}.png')
      self.side_img[dir] = pygame.transform.scale(img, (PLAYER_SIZE, PLAYER_SIZE))
    self.index = 0
    self.is_jump_pressed = False
    img = pygame.image.load(f'./source/sprites/PlayerRobotSideRight.png')
    self.side_img['Right'] = pygame.transform.scale(img, (PLAYER_SIZE, PLAYER_SIZE))
    # for i in range(6):
    #   img = pygame.image.load(f'./source/sprites/PlayerWalkingRight-{i}.png').convert()
    #   img.set_colorkey((0,0,0))
    #   self.img['Right'].append(pygame.transform.scale(img, (PLAYER_SIZE, PLAYER_SIZE)))
    img = pygame.image.load('./source/sprites/PlayerRobotSideLeft.png')
    self.side_img['Left'] = pygame.transform.scale(img, (PLAYER_SIZE, PLAYER_SIZE))
    self.facing_lr = 'Right'
    self.facing_nsew = 'East'
    self.top_surf = self.side_img[self.facing_nsew]
    self.side_surf = self.side_img[self.facing_lr]
    self.top_rect = self.top_surf.get_rect(center=(self.position.x + PLAYER_SIZE/2, self.position.y + PLAYER_SIZE/2))
    self.side_rect = self.side_surf.get_rect(center=(self.position.x + PLAYER_SIZE/2, self.position.z + PLAYER_SIZE/2))
    self.render_pos = Vector3(screen.get_width()/2 - PLAYER_SIZE/2, screen.get_height()/2 - PLAYER_SIZE/2 + self.position.y, screen.get_height()/2 - PLAYER_SIZE/2 - self.position.z)



  # vec = direction
  def move(self, vec, map, camera_view):
    vec.normalize_xy(MOVE_SPEED)
    if self.is_jump_pressed or not self.can_fall(map, camera_view):
      self.is_jump_pressed = True
      vec.z *= THRUST_SPEED
    else:
      vec.z = 0
    newPos = Vector3(self.position.x, self.position.y, self.position.z)
    newPos.add(vec)
    self.moveToPosition(self.position, newPos, map, camera_view)
  
  def moveToPosition(self, old_pos, new_pos, map, camera_view):
    if old_pos.x != new_pos.x or old_pos.y != new_pos.y or old_pos.z != new_pos.z:
      if map.canPlayerMoveToPosition(new_pos, self, camera_view):
        # print('no conflict')
        self.position = new_pos
      elif map.canPlayerMoveToPosition(Vector3(old_pos.x, new_pos.y, new_pos.z), self, camera_view):
        self.position = Vector3(old_pos.x, new_pos.y, new_pos.z)
      elif map.canPlayerMoveToPosition(Vector3(new_pos.x, old_pos.y, new_pos.z), self, camera_view):
        self.position = Vector3(new_pos.x, old_pos.y, new_pos.z)
      elif map.canPlayerMoveToPosition(Vector3(new_pos.x, new_pos.y, old_pos.z), self, camera_view):
        self.position = Vector3(new_pos.x, new_pos.y, old_pos.z)
      else:
        print("can't move")
        return False
    self.side_rect.update((self.position.x, self.position.z), (self.side_rect.width, self.side_rect.height))
    return True
      # else:
      #   print("can't move!")


  def can_fall(self, map, camera_view):
    return map.canPlayerMoveToPosition(Vector3(self.position.x, self.position.y, self.position.z + 3), self, camera_view)

  def update(self, keys, camera_view, screen, map):
    self.handleKeys(keys, camera_view, map)
    # print(self.position.z)
    if camera_view == 'side' and self.can_fall(map, camera_view):
      self.z_velocity += Z_ACCEL
      # print(f"z velo: {self.z_velocity}")
      self.z_velocity = min(self.z_velocity, MAX_Z_VELOCITY)
      newPos = Vector3(self.position.x, self.position.y, self.position.z)
      newPos.z += self.z_velocity
      self.moveToPosition(self.position, newPos, map, camera_view)
      # self.position.z += self.z_velocity
      # exit(0)
    else:
      self.z_velocity = 0
    self.position.z = min(self.position.z, 200 - PLAYER_SIZE + 10)
    # print(f"Player ({self.position.x}, {self.position.y}, {self.position.z})")
    self.top_rect.update((self.position.x, self.position.y), (self.top_rect.width, self.top_rect.height))
    self.side_rect.update((self.position.x, self.position.z), (self.side_rect.width, self.side_rect.height))
    self.render_pos = Vector3(screen.get_width()/2, screen.get_height()/2 + self.position.y, screen.get_height()/2 + self.position.z)
    # if self.facing_lr == 'Right':
      # self.side_surf = self.img[self.facing_lr][self.index // 70]
      
    # else:
    self.top_surf = self.side_img[self.facing_nsew]
    self.side_surf = self.side_img[self.facing_lr]


  def handleKeys(self, keys, camera_view, map):
    dx = 0
    dy = 0 # y is the non-x direction here
    if keys[pygame.K_w]:
      dy = -1
      if camera_view == 'top':
        self.facing_nsew = 'North'
    elif keys[pygame.K_s]:
      dy = 1
      if camera_view == 'top':
        self.facing_nsew = 'South'
    if keys[pygame.K_d]:
      dx = 1
      self.facing_lr = 'Right'
      self.facing_nsew = 'East'
    #  self.index = (self.index + 1) % (len(self.img['Right']) * 70)
    elif keys[pygame.K_a]:
      dx = -1
      self.facing_nsew = 'West'
      self.facing_lr = 'Left'
    if camera_view == 'top':
      self.move(Vector3(dx, dy, 0), map, camera_view)
    else:
      jump = 0
      if keys[pygame.K_w]:
        jump = 1
      else:
        self.is_jump_pressed = False
      self.move(Vector3(dx, 0, jump), map, camera_view)

  def render(self, screen, camera_view):
    if camera_view == 'top':
      screen.blit(self.top_surf, [self.render_pos.x, self.render_pos.y, PLAYER_SIZE, PLAYER_SIZE])
    else:
      screen.blit(self.side_surf, [self.render_pos.x, self.render_pos.z, PLAYER_SIZE, PLAYER_SIZE])
      # print(self.position.x, self.position.z)
    text_surface = my_font.render("(%.2f, %.2f, %.2f)" % (self.position.x, self.position.y, self.position.z), False, (0, 0, 0))
    screen.blit(text_surface, (0,0))
    