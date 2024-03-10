from BoxObject import BoxObject
from Vector3 import Vector3
from PlatformerGroundObject import PlatformerGroundObject
from Player import PLAYER_SIZE
from random import randint
from TextObject import TextObject
import pygame

class Map:
  def __init__(self):
    self.objects = []
    for i in range(-2000, 10001, 250):
      for j in range(-700, 700, 250):
        self.objects.append(PlatformerGroundObject(i, j, min(randint(1, 5), 3)) if i != 750 else PlatformerGroundObject(750, j, randint(4, 5), 1))
    # self.objects.append(BoxObject(Vector3(100, 100, 0), Vector3(100, 200, 50), (0, 0, 255), True))
    self.objects.append(BoxObject(Vector3(837.5, -700, 198), Vector3(75, 1400, 1), (255, 255, 255, 0), False, transparent=True))
    self.objects.append(BoxObject(Vector3(1300, -400, 130), Vector3(75, 75, 75), collectable=True, top_image='source/sprites/SpecimenTop.png', side_image='source/sprites/SpecimenSide.png'))
    self.objects.append(BoxObject(Vector3(2100, -150, -490), Vector3(300, 300, 700), top_image='source/sprites/RockObstacleTop.png', side_image='source/sprites/RockObstacleSide.png'))
    self.objects.append(BoxObject(Vector3(2230, -37.5, -515), Vector3(75, 75, 75), collectable=True, top_image='source/sprites/SpecimenTop.png', side_image='source/sprites/SpecimenSide.png'))
    self.objects.append(BoxObject(Vector3(3912.5, 37.5, 130), Vector3(75, 75, 75), collectable=True, top_image='source/sprites/SpecimenTop.png', side_image='source/sprites/SpecimenSide.png'))
    self.objects.append(BoxObject(Vector3(3600, -350, -600), Vector3(700, 700, 600), top_image='source/sprites/CloudObstacleTop.png', side_image='source/sprites/CloudObstacleSide.png'))
    self.objects.append(BoxObject(Vector3(4800,-300,-300), Vector3(200, 600, 600), is_walkable=True, top_image='source/sprites/RampTop.png', side_image='source/sprites/RampSide.png'))
    self.objects.append(BoxObject(Vector3(4800,-300,-1000), Vector3(1, 600, 0), transparent=True))
    self.objects.append(BoxObject(Vector3(5000,-300,-1000), Vector3(1, 600, 0), transparent=True))
    self.objects.append(BoxObject(Vector3(4800,-300,-1000), Vector3(200, 1, 0), transparent=True))
    # self.objects.append(BoxObject(Vector3(4800,-300,-300), Vector3(200, 600, 600), is_walkable=True))
    self.objects.append(BoxObject(Vector3(5400,-300,-300), Vector3(200, 200, 200), is_walkable=True, top_image='source/sprites/PlatformTop.png', side_image='source/sprites/PlatformSide.png'))
    self.objects.append(BoxObject(Vector3(5400,-300,-1000), Vector3(200, 1, 0), transparent=True))
    self.objects.append(BoxObject(Vector3(5400,-300,-1000), Vector3(1, 200, 0), transparent=True))
    self.objects.append(BoxObject(Vector3(5400,-100,-1000), Vector3(200, 1, 0), transparent=True))
    self.objects.append(BoxObject(Vector3(5600,-300,-1000), Vector3(1, 200, 0), transparent=True))
    self.objects.append(BoxObject(Vector3(5900,-300,-300), Vector3(200, 200, 200), is_walkable=True, top_image='source/sprites/PlatformTop.png', side_image='source/sprites/PlatformSide.png'))
    self.objects.append(BoxObject(Vector3(5962.5, -237.5, -370), Vector3(75, 75, 75), collectable=True, top_image='source/sprites/SpecimenTop.png', side_image='source/sprites/SpecimenSide.png'))
    self.objects.append(BoxObject(Vector3(5900,-300,-1000), Vector3(200, 1, 0), transparent=True))
    self.objects.append(BoxObject(Vector3(5900,-300,-1000), Vector3(1, 200, 0), transparent=True))
    self.objects.append(BoxObject(Vector3(5900,-100,-1000), Vector3(200, 1, 0), transparent=True))
    self.objects.append(BoxObject(Vector3(6100,-300,-1000), Vector3(1, 200, 0), transparent=True))

    self.objects.append(TextObject(Vector3(-700, -200, -200), "Trip to Mars"))
    self.objects.append(TextObject(Vector3(-755, 300, 300), 'Move right to start'))
    self.objects.append(TextObject(Vector3(1000, 200, -1000), 'Press Tab to switch cameras'))
    self.objects.append(TextObject(Vector3(1200, -300, 20), 'Collect 4 aliens to win!'))

  def render(self, screen, camera_view, p_pos):
    for object in self.objects:
      object.render(screen, camera_view, p_pos)

  def canPlayerMoveToPosition(self, pos, player, camera_view):
    if pos.x < -1000 or pos.y < (-500 - 96) or pos.y > 500:
      return False
    if camera_view == 'top':
      top_rect = player.top_surf.get_rect(center=(pos.x + PLAYER_SIZE/2, pos.y + PLAYER_SIZE/2))
      for object in self.objects:
        if object.top_rect != None and (top_rect.colliderect(object.top_rect)):
          if hasattr(object, 'collectable') and object.collectable:
            self.objects.remove(object)
            player.score += 1
            pygame.mixer.Sound("source/game-start-6104.mp3").play()
            continue
          return False
    else:
      side_rect = player.side_surf.get_rect(center=(pos.x + PLAYER_SIZE/2, pos.z + PLAYER_SIZE/2))
      for object in self.objects:
        if object.side_rect != None and (side_rect.colliderect(object.side_rect)):
          if hasattr(object, 'collectable') and object.collectable:
            self.objects.remove(object)
            player.score += 1
            pygame.mixer.Sound("source/game-start-6104.mp3").play()
            continue
          return False
    return True

  def correctPosition(self, player, camera_view):
    if (camera_view == 'side'):
      for object in self.objects:
        if object.side_rect != None and (player.side_rect.colliderect(object.side_rect)):
          # print(f"top: {object.side_rect.top}, bottom: {object.side_rect.bottom}")
          player.position.z = object.side_rect.top - PLAYER_SIZE
          #print("Boom!")
    else:
      for object in self.objects:
        if object.top_rect != None and (player.top_rect.colliderect(object.top_rect)):
          # print(f"top: {object.top_rect.top}, bottom: {object.top_rect.bottom}")
          if object.top_rect.top > -500:
            player.position.y = object.top_rect.top - PLAYER_SIZE
          else:
            player.position.x = object.top_rect.left - PLAYER_SIZE

          #print("Boom!")
    
  def fallToNearestObject(self, player, camera_view):
    target = Vector3(player.position.x, player.position.y, player.position.z + 3)
    while player.can_fall(self, camera_view) and target.z < 400:
      player.moveToPosition(player.position, target, self, camera_view)
      target.z += 1
    self.correctPosition(player, camera_view)



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

