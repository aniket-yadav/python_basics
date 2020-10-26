
def add(*args):
    sum = 0
    for i in args:
        sum+=i
    return sum

def sub(a,b):
    return a-b

def mult(*args):
    product = 1
    for i in args:
        product *= i
    return product

def div(a,b):
    return a//b
