f = open('file_1234.txt','w')
f.write('파일에 기록될 문자열입니다.\n')
f.write('파일 기록하는거 참 쉽죠?\n')
f.close

with open('file_1234.txt','a')as f:
    f.writelines(['하나','둘','셋','넷','다섯'])
    #리스트 등으로 된 여러 문장을 입력하기 위해 writelines함수를 사용함
    f.write('\n')
    f.writelines('\n'.join(['여섯','일곱','여덟','아홉','열']))
    #문자열을 빈칸(\n)으로 연결하기 위해 string 메서드 join을 사용함
