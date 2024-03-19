# This file will perform division of two numbers given by the user.

def division(a, b):
    '''This method will help divide 2 integers received from user as input'''
    c = a / b
    return c

def main():
    a = int(input('Enter the first number: '))
    b = int(input('Enter the second number: '))
    print('The division of the two numbers is: ', division(a, b))

if __name__ == '__main__':
    main()