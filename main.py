# Made in 2.6.2023 from Codezilla YouTube video for OOP
# Comments meant to be very descriptive

# OOP follows four principles:

# - Encapsulation: Like a medical pill you can use it whenever you want and the pill might change
# without affecting anything. Also, it protects attributes and methods from unwanted changes
# and prevents 'ripple effect' from ruining the entire code when changes are made

# - Polymorphism: the ability of one function to perform in different ways. Applied in two ways
# -- overloading: Multiple methods with same name but with different parameters
# -- overriding: overrides methods in parent class which means that child class (inherited from parent)
# uses the same method in different way

# - inheritance: using the same attributes as the parent class without repeating codes
# and adding attributes that applies only to that object

# - Abstraction: Simplifying and hiding complexity (of implementation) behind the interface (communication)
# Example: using Coffee machine with buttons without knowing how it works


class Students:  # Making new class which will be a template to make new objects (instances)
    num_of_students = 0  # Class attribute for any objects made from this class (General attribute)

    def __init__(self, name, age=18, gpa=1):  # initialize (constructor) takes 'self' always first then any parameters
        # '=1' '=18' are default values used when none are provided

        # Public attribute which can be accessed directly. doesn't follow 'Encapsulation' principle
        self.name = name

        # Private attribute which cannot be accessed directly it needs 'getter methods' and 'setters'
        self.__age = age
        self.__gpa = gpa

    num_of_students += 1  # Adds to num of students

    def set_age(self, new_age):  # 'setters' method (functions inside classes) for private attributes
        self.__age = new_age

    def get_age(self):  # 'getter' method to get 'age' without editing it or accessing directly.
        return self.__age  # returns private attribute 'age'

    @classmethod  # initialize for class methods applies to all objects from 'Students' class
    def salary(cls, age, gpa=1):  # method for the whole class and takes 'cls' first then any parameters
        return age * gpa


# inheritance example.
class MasterStudents(Students):  # inheriting attributes from 'Students' class
    def __init__(self, major, thesis, name):  # Adding more attributes
        super().__init__(name, gpa=1, age=18)
        self.thesis = thesis  # Didn't use private attribute to make it easier to access at this case.
        self.major = major


class Ocean:  # overriding example

    def __init__(self, sea_creature_name, sea_creature_age):
        self.name = sea_creature_name
        self.age = sea_creature_age

    def __str__(self):  # overriding example
        return f'The creature type is {self.name} and the age is {self.age}'

    def __repr__(self):
        return f'Ocean(\'{self.name}\', {self.age})'


c = Ocean('Jellyfish', 5)

print(str(c))
print(repr(c))




master1 = MasterStudents('CS', 'Solar', 'Ahmed')

print(master1.thesis)

