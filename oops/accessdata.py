class Student:
    def __init__(self,fn,ln,age):
        self.firstname=fn
        self.lastname=ln
        self.age=age
        
        
s1=Student("Randrita","Sarkar",'21')
s2=Student("Poulami","Mondal","20")

print(s1.firstname,s1.lastname,s1.age)
print(s2.firstname,s2.lastname,s2.age)