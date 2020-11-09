class Managers:
    def __init__(self):
        self.developers = []
        self.designers = []
        self.testers = []

    def addDeveloper(self, dev):
        self.developers.append(dev)

    def addDesigners(self, design):
        self.designers.append(design)
    
    def addTesters(self, testers):
        self.testers.append(testers)

class Developer:
    def __init__(self):
        print("developer added")

class Designer:
    def __init__(self):
        print("designer added")

class Testers:
    def __init__(self):
        print("tester added")

#### Dependency inversion principle #####

class Employee:
    def Work():
        pass

class Manager:
    def __init__(self):
        self.employees = []
    def addEmployee(self, a):
        self.employees.append(a)

class Developer(Employee):
    def __init__(self):
        print("developer added")
    def Work():
        print("turning coffee into code")

class Designer(Employee):
    def __init__(self):
        print("designer added")
    def Work():
        print("turning lines to wiresframes")

class Testers(Employee):
    def __init__(self):
        print("tester added")
    def Work():
        print("testing every out there")
