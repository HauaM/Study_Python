a=1
def vartest(a):
    a=a+1
    print(a)
    #함수 안에서는 a+1이 되서 2가 출력됨

vartest(a)
print(a)
#함수 밖에서는 지역변수라 인정이 안됨 1이 출력
