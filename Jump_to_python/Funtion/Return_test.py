#특별한 상황이 되면 함수를 빠져나가고자 할 때는
#return을 단독으로 써서 함수를 즉시 빠져나갈 수 있다.
def say_nick(nick):
    if nick =="바보":
        return
    print("나의 별명은 %s 입니다."%nick)

say_nick('야호')
say_nick('바보')
