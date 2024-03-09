from math import sqrt

class Vector3:
  def __init__(self, x, y, z):
    self.x = x
    self.y = y
    self.z = z

  def add(self, vec):
    self.x += vec.x
    self.y += vec.y
    self.z += vec.z

  def multiply(self, scalar):
    self.x *= scalar
    self.y *= scalar
    self.z *= scalar
  
  def normalize(self, length):
    norm = sqrt(self.x*self.x + self.y*self.y + self.z*self.z)
    if norm != 0:
      self.x *= length / norm
      self.y *= length / norm
      self.z *= length / norm
