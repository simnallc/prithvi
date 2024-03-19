# This file is to perform substraction of two number give by user

def subsstraction(a, b):
    '''This method will help subtract 2 integers received from user as input'''
    c = a - b
    return c

def main():
    a = int(input('Enter the first number: '))
    b = int(input('Enter the second number: '))
    print('The difference of the two numbers is: ', subsstraction(a, b))

if __name__ == '__main__':
    main()