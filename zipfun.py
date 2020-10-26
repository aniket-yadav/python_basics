list1 = [1,2,3,4,5]
list2 = ['one','two','three','four','five']
list3 = set(zip(list1,list2))
print(list3)


list4 = ['1','2','3']
list5 = [1,2]
print(list(zip(list4,list5)))


list4 = ['1','2','3']
list5 = [1,2,4,6]
print(list(zip(list4,list5)))