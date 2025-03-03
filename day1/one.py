class Employee:
    def __init__(self, empid=None, name=None, salary=None):
        self.empid=empid
        self.name=name
        self.salary=salary
    def setEmpid(self,empid):
        self.empid=empid
    def setName(self,name):
        self.name=name
    def setSalary(self,salary):
        self.salary=salary
    def getEmpid(self):
        return self.empid
    def getSalary(self):
        return self.salary
    def getName(self):
        return self.name
    
e1=Employee()
e2=Employee(1, "sameer", 100000000)
e1.setEmpid(2)
e1.setName("sameers")
e1.setSalary(300000)
print(e1.getEmpid(),e1.getName(),e1.getSalary())
print(e2.getEmpid(),e2.getName(),e2.getSalary())

    
        