# class Student:
#     def __init__(self):
#         self.__marks = 70
#     def get_marks(self):
#         return self.__marks
# s = Student()
# print(s.get_marks())  

# Getter& setter
# class Student:
#     def __init__(self):
#         self.__marks = 0
#     def set_marks(self,marks):
#         if 0 <= marks <= 100:
#             self.__marks = marks
#         else:
#             print("invalid marks")
#     def get_marks(self):
#         return self.__marks
# s = Student()

# s.set_marks(85)
# print(s.get_marks())

# Getter and Setter in python style

# @property

class Student:
    def __init__ (self):
        self.__marks = 0
    @property
    def marks(self):
        return self .__marks
    @marks.setter
    def marks(self,value):
        if 0 <= value <= 100:
            self.__marks = value
        else:
            print("Invalid value")
s = Student()
s.marks = 75
print(s.marks)