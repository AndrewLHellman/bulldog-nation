import pygame
from Map import Map
from Player import Player

class Game:
  def __init__(self):
    self.player = Player()
    self.map = Map()
  
  def render(self, screen):
    self.map.render(screen, self.player.x, self.player.y)
    self.player.render(screen)

    
