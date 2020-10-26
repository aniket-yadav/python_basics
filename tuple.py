a = (1,2,34,5,5,'abc',"python",(1212,344,56,3),[12,34,56],{'name':'python'})

print(isinstance(a,tuple))
print(a)
print(a[3:5])
print(a[:])
print(a[:4])
print(a[2:])
print(a[6]*2)
print(a[-4])

# does not support assignment
a[4]='a'