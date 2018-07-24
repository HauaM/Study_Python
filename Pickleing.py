import pickle
alphabet=['a','b','c','d','e','f','g']
try:
  with open('alphabet.txt','wb')as alpha_file:
    pickle.dump(alphabet,alpha_file)
    #alphabet을 alpha_file속에 저장함 피클링 부분
except IOError as err:
  print('File error : ' +str(err))
except pickle.PickleError as perr:
  print('Pickling error : ' + str(perr))
