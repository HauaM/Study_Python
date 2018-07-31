#global명령하여 함수 밖 변수 변경하는 방법
a=1
def vartest():
    global a
    a=a+1
vartest()
print(a)
