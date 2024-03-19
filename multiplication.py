# This file shall perform multiplication of two numbers given by the user.

def multiplication(a, b):
    '''This method will help multiply 2 integers received from user as input'''
    c = a * b
    return c

def main():
    a = int(input('Enter the first number: '))
    b = int(input('Enter the second number: '))
    print('The product of the two numbers is: ', multiplication(a, b))

if __name__ == '__main__':
    main()