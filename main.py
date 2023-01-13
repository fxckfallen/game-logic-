class Player:
  def __init__(self, name, hp, inventory):
    self.name = name
    self.hp = hp
    self.inventory = [] + inventory
    self.pos = (0, 0, 0)

  def move(self, x, y, z):
    self.pos[0] += x
    self.pos[1] += y
    self.pos[2] += z

  def heal(self, hp):
   self.hp += hp

  def __del__(self):
    print('dead')
  def damage(self, hp):
    if self.hp - hp <= 0:
      self.__del__()
      self.hp = 0
    else:
      self.hp -= hp

player = Player("test", 100, [])
player.damage(10)
print(player.hp)
player.damage(89)
print(player.hp)
player.heal(10)
print(player.hp)