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

a=FourCal(4,2) #생성자를 생성하여 a의 인스턴스에 매개변수를 넣음
a.sum()
a.mul()
a.sub() # self 함수 사용한 first와 second의 틀린 호출
a.div() # self 함수를 사용 하지 않아 인수를 받을 수 없음
