import random as r

#generation
class Mines:
  def __init__(self):
    pass
  
  def generateMines():
      coordinates = [(r.randint(0, 9), r.randint(0, 9)) for _ in range(10)]
      return coordinates
