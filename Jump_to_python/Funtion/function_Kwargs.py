def func(**kwargs):
    print(kwargs)

func(a=1)
#{'a':1}
func(name='foo',age=3)
#{'age':3,'name':'foo'}
