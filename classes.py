# creating a class 

class Student:

    # constructor
    def __init__(self, firstname, lastname, birthdate, sid):
        self.firstname = firstname
        self.lastname = lastname
        self.birthdate = birthdate
        self.sid = sid 

    # method 
    def myself(self):
        return f'My name is {self.firstname} {self.lastname}. I was born {self.birthdate}. My student id number is {self.sid}.'
# initialize user object
student1 = Student('John','Doe','2020-08-17','c27886377')

# print(student1.firstname)

print(student1.myself())
