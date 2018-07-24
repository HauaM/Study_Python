import pickle
load_alpha=[]
try:
    with open('alphabet.txt','rb')as alpha_file:
        load_alpha=pickle.load(alpha_file)
    print(load_alpha)
except IOError as err:
  print('File error : ' +str(err))
except pickle.PickleError as perr:
  print('Pickling error : ' + str(perr))
