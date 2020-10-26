# a = [1,3,5,'a',"aniket",[1,2,3,4],(1,2,3,4),{'name':'pyton'}]

# print(isinstance(a,list))
# print(a)

# print(a[0:3])
# print(a[5:])
# print(a[:5])
# print(a[4]+' likes '+a[-1]['name'])
# print(a[5]*5)

mobileBrand = []
no = int(input('Enter number  of value you want to enter : '))

for i in range(0,no):
    mobileBrand.append(input("Enter element : "))

print("Mobile brands : ")
for i in mobileBrand:
    print(i)
