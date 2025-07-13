'''
def func(x):
    def func2():
        print(x)
    return func2

x= func(3)
x()
'''


#def func(*args, **kwargs): kwargs stands for keyword arguements
 #   pass

def func(x,y):
    print(x,y)
pairs = [(1,2),(3,4)]

for pair in pairs:
    func(*pair)

