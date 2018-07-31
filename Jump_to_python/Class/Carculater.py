class FourCal():
    def setdate(self,first,second):
        self.first = first
        self.second = second
    #생성자 없이 self를 사용한 방법
    def sum(self):
        print(self.first+self.second)
    def mul(self):
        print(self.first*self.second)

    #def sub(self):
    #    print(first-second)

    #def div(first,second):
    #    print(first/second)

a=FourCal()
a.setdate(4,2)  #생성자 없이 self함수 리콜
a.sum()
a.mul()
a.sub() # self 함수 사용한 first와 second의 틀린 호출
a.div() # self 함수를 사용 하지 않아 인수를 받을 수 없음
