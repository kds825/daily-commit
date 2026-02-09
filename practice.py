
class FourCal:
    def setdata(self, first, second):
        self.first = first
        self.second = second
    def add(self):
        result = self.first + self.second
        return result

a = FourCal()
a.setdata(4,2)

print(a.add())    # def __init__(self):
    #     self.result = 0
        
    
    # def sub(self, num):
    #     self.result -= num
    #     return self.result
    
