from BoxObject import BoxObject

class Map:
  def __init__(self):
    self.objects = []
    self.objects.append(BoxObject(200, 200, 100, 50))

  def render(self, screen, px, py):

    for object in self.objects:
      object.render(screen, px, py)
