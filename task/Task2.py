class rectangle:
    def __init__(self, Length, Width):
        self.length = Length 
        self.width = Width

    def method_area(self):
        return   self.width * self.length
    
    def perimeter(self):
        return 2 * (self.width + self.length)
    

    def chk_sq(self):
        if self.width == self.length :
            return True
        else:
            return False   
    
r = rectangle(4,6)
print("Area:",r.method_area())
print("Is it sq:",r.chk_sq())
print("Perimeter :",r.perimeter())
