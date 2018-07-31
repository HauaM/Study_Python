class FourCal():
    def __init__(self,first,second):
        self.first = first
        self.second = second
    #생성자를 사용한 값 지정

    def sum(self):
        print(self.first+self.second)
    def mul(self):
        print(self.first*self.second)

    def sub(self):
        print(self.first-self.second)

    def div(self):
        print(self.first/self.second)

class MoreFourCal(FourCal):
    def pow(self):
        result = self.first ** self.second
        return result

a = MoreFourCal(4,2)
a.pow()
a.sum()
a.mul()
a.sub()
a.div()
