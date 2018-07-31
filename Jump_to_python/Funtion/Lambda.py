# lambda 매개변수1, 매개변수2,...:매개변수를 이용한 표현
sum=lambda a,b :a+b
sum(3,4)

#def sum(a,b):
#   return a+b

myList=[lambda a,b: a+b, lambda a,b:a*b]
#a,b값을 입력받아 더하고 곱하는 방식을 리스트의 요소로 사용가능

print(myList[0](3,4))
#0번째 리스트 요소인 덧셈을 이용 값은 7
print(myList[1](3,4))
#1번째 리스트 요소인 곱셈을 이용한 값은 12
