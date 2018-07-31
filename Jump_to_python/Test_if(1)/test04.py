a = "나이 :30,키:180"
temp = a.split(",")
age = temp[0].split(":")[-1]
height = temp[1].split(":")[-1]
if int(age)<30 and int(height)>=175:
    #문자열을 숫자열로 형변환
    print("Yes")
else:
    print("No")
