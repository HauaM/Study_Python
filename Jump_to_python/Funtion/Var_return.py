#return을 사용해서 값을 전역변수 a에 값을 반환

a=1
def vartest(a):
    a=a+1
    return a

a=vartest(a)
print(a)
