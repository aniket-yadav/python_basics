def doubleNumber(no):
    return no*2

list1 = [1,3,5,6]

list2 = list(map(doubleNumber,list1))

print(list2)

list3 = list(map(lambda a: a*2,list1))
print(list3)
