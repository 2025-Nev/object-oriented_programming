class Employee:
    empCount = 0

    def __init__(self, name, salary):
    self.name = name
    self.salary = salary
    Employee.empCount += 1

    def displayCount(self):
    print("Total Employee %d" % Employee.empCount)

    def displayCount(self):
    print("Name : ", self.name, ", Salary: ", self.salary)
