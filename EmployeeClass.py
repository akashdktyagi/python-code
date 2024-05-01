
import math

class Employee:
    def __init__(self, name,age):
        self.name=name
        self.age=age
        print("i m in init")

    def show_employee_detail(self):
        pass
        # print(self.name)
        # print(self.age)

if __name__ == '__main__':
    obj = Employee("Akash",25)
    obj.show_employee_detail()
