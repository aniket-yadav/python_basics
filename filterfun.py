def greaterThanFive(no):
    if no > 5:
        return True
    return False


list1 = [2,34,5,66,4,34,23,6]
list2 = list(filter(greaterThanFive,list1))
print(list2)


list3 = list(filter(lambda a: a>5,list1))
print(list3)
