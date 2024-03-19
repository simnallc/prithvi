# This file is to perform addition of two number give by user

def addition(a, b):
    '''This method will help add 2 integers received from user as input'''
    c = a + b
    return c

def main():
    a = int(input('Enter the first number: '))
    b = int(input('Enter the second number: '))
    print('The sum of the two numbers is: ', addition(a, b))

if __name__ == '__main__':
    main()