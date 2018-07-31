
def input_avr(*args):
    result = 0
    for i in args:
        result = result + i
    print(result)
    return result / len(args)


    #len 함수를 사용해서 길이를 추정

input_avr(1,2)
input_avr(1,2,3,4,5,6,7,8,9,10)
