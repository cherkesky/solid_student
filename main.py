'''
Practice: Solid Student
Define a Python class named Student. This class will have 5 properties.

First name (string)
Last name (string)
Age (integer)
Cohort number (integer)
Full name (read-only string)
Define getters for all properties.
Define a setter for all but the read only property.
Ensure that only the appropriate value can be assigned to each.
The full name property should return first name and last name separated by a space. It's value cannot be set.
'''

class Student():
  def __init__(self,last, age, cohort):
    self.last = last
    self.age = age
    self.cohort = cohort

  def fullname(self):
    return (self.first+" "+self.last)
  
  @property 
  def first(self):
    try: 
      return self.__first
    except AttributeError:
      return "Not Defined"

  @first.setter
  def first(self, newFirst):
    if type(newFirst) is str:
      self.__first = newFirst
    else:
      raise TypeError('Not A String')

guy = Student("Cherkesky", "39","36")
print(guy.fullname())
print(guy.first)
guy.first = "Guy"

print(guy.fullname())





