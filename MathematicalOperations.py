flag = True
#to inform user about input
print("Please enter the value of the opertaion that you want to perform \n1.+ to add\n2.- to subtract\n3.* to multiply\n4./ to divide\n5.% to get modulus\n6.! to get factorial\nType EXIT to exit \n")
    
while(flag):
    #to take user input
    input1 = input("Operation: ")
    
    #For addition
    
    if input1 == '+':
        number1 = input("Please enter first number ")
        if number1.isdigit():
            number2 = input("Plaese enter second number ")
            if number2.isdigit():
                print(int(number1)+int(number2))
            else:
                print("Plaese enter a valid value")
        else:
            print("Please enter a valid value")
    
    #For subtraction
    
    elif input1 == '-':
        number1 = input("Please enter first number ")
        if number1.isdigit():
            number2 = input("Plaese enter second number ")
            if number2.isdigit():
                print(int(number1)-int(number2))
            else:
                print("Plaese enter a valid value")
        else:
            print("Please enter a valid value")
    
    #For multiplication
    
    elif input1 == '*':
        number1 = input("Please enter first number ")
        if number1.isdigit():
            number2 = input("Plaese enter second number ")
            if number2.isdigit():
                print(int(number1)*int(number2))
            else:
                print("Plaese enter a valid value")
        else:
            print("Please enter a valid value")
    
    #For division
    
    elif input1 == '/':
        number1 = input("Please enter first number ")
        if number1.isdigit():
            number2 = input("Plaese enter second number ")
            if number2.isdigit():
                print(int(number1)/int(number2))
            else:
                print("Plaese enter a valid value")
        else:
            print("Please enter a valid value")
    
    #For Mod
    
    elif input1 == '%':
        number1 = input("Please enter first number ")
        if number1.isdigit():
            number2 = input("Please enter second number ")
            if number2.isdigit():
                print(int(number1)%int(number2))
            else:
                print("Please enter a valid value")
        else:
            print("Please enter a valid value")
    
    #For factorial
    
    elif input1 == '!':
        number1 = input("Please enter the number ")
        if number1.isdigit():
            result = 1
            for x in range(1,int(number1)+1):
                result = result*x
            print(result)
        else:
            print("Please enter a valid value")
    
    # To exit the program
    
    elif input1 == 'EXIT':
        flag = False
    else:
        print("Please enter a valid value")
