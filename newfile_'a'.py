f=open("newfile.txt",'a')
for i in range(11,21):
  data = "%d \n" %i
  f.write(data)
f.close
