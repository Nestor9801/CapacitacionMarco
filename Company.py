class Company:
 def __init__(self):
  #Protected number
  self.__project = "NLP"

#child class
class Employee(Company):
  def __init__(self,name):
    self.name = name
    Company.__init__(self)
  def show(self):
    print("Employee name:", self.name)
    #Accessing protected member in child class
    print("Working in project:", self.__project)
c= Employee("Jessa")
c.show()
print("Ending program")
