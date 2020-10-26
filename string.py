# # single line

# a = 'python'
# b = "this is python "

# # multiline

# c= ''' this
#         is 
#         python 
#         string
#         demo '''
# d = """ you can use 
#         single or 
#         double quote """

# print(a)
# print(b)
# print(c)
# print(d)

# print(a+b)
# print(a*3)


# print('this is {}. hello {}'.format('python',"aniket"))
# print('this is {1}. hello {0}'.format("aniket",'python'))
# print('this is {a}. hello {b}'.format(b="aniket",a='python'))

# string function
a = 'pythonyyashdjkfnchuwueosjdhfk'

print(a.count('y',0,-1))
print(a.endswith('k',0,len(a)))
print(a.find('y',4,-1))

b= 'an23'
print(b.isalnum())

b= '23'
print(b.isdigit())
