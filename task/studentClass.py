class Student:
    def __init__(self, name, roll, marks):
        self.Name = name
        self.Roll = roll
        self.Marks = marks
    
    def display_info(self):
        print(f"Name: {self.Name}, Roll: {self.Roll}, Marks: {self.Marks}");
    def isPAssed(self):
        if(self.Marks <= 45):
            print('Failed')
        else:
            print('Passed')

quddus_std = Student("quddus",103,20)
quddus_std.display_info()
quddus_std.isPAssed()