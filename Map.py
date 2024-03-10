from BoxObject import BoxObject
from Vector3 import Vector3
from PlatformerGroundObject import PlatformerGroundObject
from Player import PLAYER_SIZE
from random import randint

class Map:
  def __init__(self):
    self.objects = []
    for i in range(-5000, 5001, 250):
      for j in range(-700, 700, 250):
        self.objects.append(PlatformerGroundObject(i, j, min(randint(1, 5), 3)))
    for i in range(-700, 700, 250):
      self.objects.append(PlatformerGroundObject(600, i, randint(4, 5)))
    self.objects.append(BoxObject(Vector3(100, 100, 0), 100, 100, 100))

  def render(self, screen, camera_view, p_pos):
    for object in self.objects:
      object.render(screen, camera_view, p_pos)

  def canPlayerMoveToPosition(self, pos, player, camera_view):
    if camera_view == 'top':
      top_rect = player.top_surf.get_rect(center=(pos.x + PLAYER_SIZE/2, pos.y + PLAYER_SIZE/2))
      for object in self.objects:
        if object.top_rect != None and (top_rect.colliderect(object.top_rect)):
          # print(f'Collision with {object}!')
          # print(f"Player rect: {top_rect.topleft}, {top_rect.bottomright}")
          # print(f"Object rect: {object.top_rect.topleft}, {object.top_rect.bottomright}")
          return False
      # print("no coll")
      return True
    else:
      side_rect = player.top_surf.get_rect(center=(pos.x + PLAYER_SIZE/2, pos.z + PLAYER_SIZE/2))
      for object in self.objects:
        if object.side_rect != None and (side_rect.colliderect(object.side_rect)):
          # print(f'Collision with {object}!')
          # print(f"Player rect: {side_rect.topleft}, {side_rect.bottomright}")
          # print(f"Object rect: {object.side_rect.topleft}, {object.side_rect.bottomright}")
          return False
      # print("no coll")
      return True


  def correctPosition(self, player, camera_view):
    if (camera_view == 'side'):
      for object in self.objects:
        if (player.side_rect.colliderect(object.side_rect)):
          print(f"top: {object.side_rect.top}, bottom: {object.side_rect.bottom}")
          player.position.z = object.side_rect.top - PLAYER_SIZE
          #print("Boom!")
    else:
      for object in self.objects:
        if object.top_rect != None and (player.top_rect.colliderect(object.top_rect)):
          print(f"top: {object.top_rect.top}, bottom: {object.top_rect.bottom}")
          player.position.y = object.top_rect.top - PLAYER_SIZE
          #print("Boom!")



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
        else:
          object.side_surf.fill(object.color)

