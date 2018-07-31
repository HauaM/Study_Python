def myfunc(number):
    result = []
    for number in number:
        if number>5:
            result.append(number)
    print(result)
    return result

myfunc([2,3,4,5,6,7,8])
