#Building my first class

class PlayerCharacter:
  def __init__(self, name, age):
    self.name = name #attribute
    self.age = age #attribute
  
  def run(self):
    print('run')
    return 'done'

player1 = PlayerCharacter('gagan',27)
player2 =PlayerCharacter('Raavi',27)

print(player1.age) #accessing attributes of object
print(player2.age)
print(player1.run()) #accessing method on the object

