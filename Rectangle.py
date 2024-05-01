
class Rectangle:
    def __init__(self, length, breadth): # Automatically called; similar to Constructor in Java
        self.length=length
        self.breadth=breadth

    def perimeter(self):
        return self.length*2 + self.breadth*2

    def area(self):
        return self.length*self.breadth



if __name__ == '__main__':
    obj_rectangle = Rectangle(2,3) # Creating the object of the class; object name is "rectangle_object_var"
    print(obj_rectangle.perimeter())
    print(obj_rectangle.area())

