#ordered or unordered group of elements -> collections
#list are mutable

x = [4,True,'hi']
x.append('hello')
print((x))
x.extend([4,2,6,3])
print(x)
print(x.pop())      #remove and return the last element work of pop()

print(x)

print(x.pop(0))   # here element is removed from place zero
print(x)

x.extend(['roht','yadav','amity'])
print(x)
x[0]="computer"
print(x)


