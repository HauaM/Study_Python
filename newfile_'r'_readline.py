f=open("newfile.txt",'r')
while 1:
  line=f.readline()
  if not line: break
  print(line)
f.close
