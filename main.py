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
  def __init__(self, first, last, age, cohort):
    self.first = first
    self.last = last
    self.age = age
    self.cohort = cohort

  def fullname(self):
    return (self.first+" "+self.last)
  
guy = Student("Guy", "Cherkesky", "39","36")

print(guy.fullname())