class student:
    def __init__(self,name,roll_number,marks):
        self.name = name      #artibute 
        self.roll_number = roll_number
        self.marks = marks 

    def display__info(self):
        print(f"Name :  {self.name}")
        print(f"Roll_Number : {self.roll_number}")
        print(f"Marks : {self.marks}")
        print(f"Passed : {"True"if self.has_passed() else "False"}")

    def has_passed(self):
        return  self.marks >= 40 


s1 = student("My name is Rohan",12,50)
s2 = student("My name is Ali",13,45)         
s3 = student("My name is Zain",14,36)


s1.display__info()
s2.display__info()
s3.display__info()