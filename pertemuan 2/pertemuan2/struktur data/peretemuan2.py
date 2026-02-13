class Person:
  def __init__(self, fname, lname):
    self.firstname = fname#atribut
    self.lastname = lname

  def printname(self):
    print(self.firstname, self.lastname)
#anak
class Student(Person):
  def __init__(self, fname, lname):
    super().__init__(fname, lname)#super untuk memanggil 
def welcome(self):
    print("Welcome", self.firstname, self.lastname, "to the class of", self.graduationyear)

x = Student("Mike", "Olsen")
p = Person
x.firstname
x.printname()





