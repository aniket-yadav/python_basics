# object identityfier memory management for same value python doesn't give new memory location

a = 100
b = a

print(id(a))
print(id(b))

b= 1

print(id(b))
