class Item():
  ''' Class for defining each of the items in the grocery store '''
  def __init__(self, name, portion, calories, fat, protein, carbs, salt, fiber, sugar ):
    self.name = name
    self.portion = portion
    self.calories = calories
    self.fat = fat 
    self.protein = protein
    self.carbs = carbs
    self.salt = salt
    self.sugar = sugar
    self.fiber = fiber
    
  # SETTERS AND GETTERS
  @property
  def name(self):
    return self._name
  @name.setter
  def name(self, name):
    self._name = name

  @property
  def portion(self):
    return self._portion
  @portion.setter
  def portion(self, portion):
    self._portion = portion

  @property
  def calories(self):
    return self._calories
  @calories.setter
  def calories(self, calories):
    self._calories = self.checkint(calories)

  @property
  def fat(self):
    return self._fat
  @fat.setter
  def fat(self, fat):
    self._fat = self.checkint(fat)

  @property
  def protein(self):
    return self._protein
  @protein.setter
  def protein(self, protein):
    self._protein = self.checkint(protein)

  @property
  def carbs(self):
    return self._carbs
  @carbs.setter
  def carbs(self, carbs):
    self._carbs = self.checkint(carbs)

  @property
  def salt(self):
    return self._salt
  @salt.setter
  def salt(self, salt):
    self._salt = self.checkint(salt)

  @property
  def sugar(self):
    return self._sugar
  @sugar.setter
  def sugar(self, sugar):
    self._sugar = self.checkint(sugar)

  @property
  def fiber(self):
    return self._fiber
  @fiber.setter
  def fiber(self, fiber):
    self._fiber = self.checkint(fiber)

  def checkint(self,property):
    if type(property) != float:
      try: property = float(property)
      except: self.raiseError(f"{property} could not be set as it is not convertable to a float")
    return property

  def getPortion(self,portion):
    self._portion*=portion
    self.changemacros()

  def changemacros():
    return 

  @staticmethod
  def raiseError(error):
    print(error)
    exit(1)
    
def getToday():
  return 1600, [0,0,0]

def doSearch(item):
  # look for item in db
  # return item details
  return 'carrots'
