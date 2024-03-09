from BoxObject import BoxObject
from Vector3 import Vector3
from PlatformerGroundObject import PlatformerGroundObject

class Map:
  def __init__(self):
    self.objects = []
    for i in range(-5000, 5001, 2000):
      self.objects.append(PlatformerGroundObject(-i))
    self.objects.append(BoxObject(Vector3(0, 0, 0), 100, 100, 100))

  def render(self, screen, camera_view, p_pos):
    for object in self.objects:
      object.render(screen, camera_view, p_pos)
