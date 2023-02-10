class School:
  def __init__(self,name,level,numberOfStudents):
    self.name = name
    self.level = level
    self.numberOfStudents = numberOfStudents
    
  def getName(self):
    return self.name

  def getLevel(self):
    return self.level

  def getNumberOfStudents(self):
    return self.numberOfStudents

  def setNumberOfStudents(self):
    self.numberOfStudents = newNumberOfStudents

  def __repr__(self):
    return "A "+ str(self.level) + " school named "+ str(self.name) +" with " + str(self.numberOfStudents) + " students"

class PrimarySchool(School):
  def __init__(self,pickupPolicy):
    self.pickupPolicy = pickupPolicy
    parentInit = super().__init__()

  def __repr__(self):
    parentRepr = super().__repr__()
    return parentRepr + "The pickup policy is {pickupPolicy}".format(pickupPolicy = self.pickupPolicy)

  def getPickupPolicy(self):
    self.pickupPolicy = pickupPolicy


a = School("Codecademy", "high", 100)
print(a)
print(a.getName())
print(a.getLevel())
a.setNumberOfStudents(200)
print(a.getNumberOfStudents())

b = PrimarySchool("Codecademy", 300, "Pickup Allowed")
print(b.getPickupPolicy())
print(b)
# output:A high school named Codecademy with 100 students
# Codecademy
# high




# 