from BoxObject import BoxObject
from Vector3 import Vector3
from PlatformerGroundObject import PlatformerGroundObject

class Map:
  def __init__(self):
    self.objects = []
    self.objects.append(PlatformerGroundObject())
    self.objects.append(BoxObject(Vector3(-200, 200, 200), 100, 75, 50))

  def render(self, screen, camera_view, p_pos):
    for object in self.objects:
      object.render(screen, camera_view, p_pos)
