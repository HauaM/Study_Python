color = ["red","blue","green"]
color2 = ["orange","black","white"]
print(color+color2)
#두 리스트 합치기
len(color)
#리스트 길이
color[0]="yellow"
#0번째 리스트의 값을 변경
print(color*2)
#color 리스트 2회 반복
'blue' in color2
#문자열 'blue'가 color2 존재 여부 반환 true or false 밖에 안들어감
total_color = color + color2

color.append("white")
#리스트에 "white"추가
color.extend(["black","purple"])
#리스트에 새로운 리스트 추가
color.insert(0,"orange")
#0번째 주소에 "orange"추가
print(color)
color.remove("white")
#리스트에서 "white"삭제
del color[0]
#0번째 주소 리스트 객체 삭제
print(color)
