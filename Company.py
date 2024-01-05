class Company:
 def __init__(self):
  #Protected number

#child class
class Employee(Company):
  def __init__(self,name):
    self.name = name
    Company.__init__(self)
  def show(self):
    print("Employee name:", self.name)
    #Accessing protected member in child class

c= Employee("Jessa")
c.show()
print("Ending program")
