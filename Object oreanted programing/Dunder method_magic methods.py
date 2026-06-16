# __init__ Methods
# Object Create hote hi automatically call hota hai

# class student:
#     def __init__(self,name):
#         self.name = name
# s = student("Anjali")
# print(s.name)

#__Str__ () Readable String Reprsentation

# class Student:
#     def __str__(self):
#         return "Student object"
# s = Student()
# print(s)

# __repr__() - Developer Representation

# class Student:
#     def __repr__(self):
#         return "Student('Anjali')"
    
# s = Student()
# print(repr(s))

# __len__()Length Return karna

# class Demo:
#     def __len__(self):
#         return 20 
# d = Demo()
# print(len(d))

# __add__() + Operator Overloading

# class Number:
#     def __init__(self, value):
#         self.value = value
#     def __add__(self, other):
#         return self.value + other.value
# n1 = Number(90)
# n2 = Number(30)
# print(n1 + n2)

# __eq__n( )- Equality Check(==)
# class Student:
#     def __init__(self,marks):
#         self.marks = marks
#     def __eq__(self,other):
#         return self.marks == other.marks
# s1 = Student(90)
# s2 = Student(90)
# print(s1 == s2)

# __getitem__()- Index Access
# class Demo:
#    def __getitem__(self,index):
#         return index * 10
# d = Demo()
# print(d[8])

# __call__ ()- object ko function ki tarh Call karna
# class Demo:
#     def __call__(self):
#         print("object called")
# d = Demo()
# d()

#__iter__ () And __next__()- Iterator Banana
# 
# class Count:
#   def __init__(self): 
#     self.num = 0
#   def __iter__(self):
#     return self
#   def __next__(self):
#     if self.num <= 5:
#       x = self.num
#       self.num += 4
#       return x
#     raise StopIteration
# c = Count()
# for i in c :
#     print(i)

# __contains__()- Operator

class Demo:
    def __contains__(self, item):
        return item == "Python"
d = Demo()
print("Python" in d)
