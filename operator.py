# arithmetic operators
a = 5 
b = 2

print(a+b)
print(a-b)
print(a*b)
print(a/b)
print(a**b)
print(a//b)
print(a%b)

# comparison operators

print(a == b)
print(a != b)
print(a <= b)
print(a >= b)
print(a > b)
print(a < b)

# assignment operator
a+=b
print(a)
a-=b
print(a)
a/=b
print(a)
a//=b
print(a)
a*=b
print(a)
a**=b
print(a)

# bitwise operator

a = 1
b = 2

# 0001
# 0010
print(a & b )
print(a | b )
print(a ^ b )
print( ~b )
print(a << 1 )
print(a >> 1 )



# logical operator

print( True and True)
print( True and False)
print( True or True)
print( True or False)
print( not True)


# membership operator

a = (1,3,5,7)

print( 3 in a)
print(4 in a)
print(3 not in a)
print(4 not in a)

# identity operator
a = 5
b = 5

print( a is b)
print(a is not b)