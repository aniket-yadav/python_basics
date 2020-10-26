import calculation as cal 

while 1: 
    try:       
        a = int(input("Enter value of a : "))
        b = int(input("Enter value of b : "))

        op = int(input("""Options :
            1. Add 
            2. sub
            3. mult
            4. div
        Enter option no : """))
        oplist = [1,2,3,4]
        if(op not in oplist):
            raise ValueError("Invalid option selected")


        if(op == 1):
            print(f'Addition of {a} and {b} is {cal.add(a,b)}')
        elif(op == 2):
            print(f'Subtraction of {b} from {a} is {cal.sub(a,b)}')
        elif(op == 3):
            print(f'Multiplication of {a} and {b} is {cal.mult(a,b)}')
        elif(op == 4):
            print(f'Division of {b} by {a} is {cal.div(a,b)}')
        else:
            print('invalid input ')
    except Exception as e:
        print(e)
    else:
        print("Operation successful")
    finally:
        cont = input("Do you want to continue y/n : ")
        if(cont == 'n'):
            break
