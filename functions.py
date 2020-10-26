
def hello(name):
    print(f'hello, {name}')
hello("aniket")

def factorial(no):
    if(no == 0):
        return 1
    return no*factorial(no - 1)
print(factorial(5))

# types function based on arguments
# normal
def hello(name):
    print(f'hello, {name}')
hello("aniket")

# default args
def sayName(name = "Anom"):
    print(name)
sayName()
sayName("aniket")

# variable length args

def createList(*elements):
    return(list(elements))

print(createList('python','java','C#'))

# keyword arguments

def person(name,age):
    print(f'my name is {name} and i am {age} old')

person(age=23,name="aniket")

def createDict(**args):
    print(args)

createDict(name="apple",color='res')