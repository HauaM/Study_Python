f= open("newfile.txt",'w')
for i in range(1,11):
  data="%d \n"%i
  #%d는 뒤에 i의 값을 가져오는 것임
  f.write(data)
  #f.을 붙여서 newfile에 작성함
  f.close
