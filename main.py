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

  @property 
  def last(self):
    try: 
      return self.__last
    except AttributeError:
      return "Not Defined"

  @last.setter
  def last(self, newLast):
    if type(newLast) is str:
      self.__last = newLast
    else:
      raise TypeError('Not A String')
  
  @property 
  def age(self):
    try: 
      return self.__age
    except AttributeError:
      return "Not Defined"

  @age.setter
  def age(self, newAge):
    if type(newAge) is int:
      self.__age = newAge
    else:
      raise TypeError('Not An Integer')

  @property 
  def cohort(self):
    try: 
      return self.__cohort
    except AttributeError:
      return "Not Defined"

  @cohort.setter
  def cohort(self, newCohort):
    if type(newCohort) is int:
      self.__cohort = newCohort
    else:
      raise TypeError('Not An Integer')

  @property 
  def full_name(self):
    try: 
      return self.first + " " + self.last
    except AttributeError:
      return "Not Defined"

guy = Student()

guy.first = "Guy"
guy.last = "Cherkesky"
guy.age = 39
guy.cohort = 36

print(guy.full_name)

