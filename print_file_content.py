def print_content(path):
    '''This method will print the content of the file'''
    with open(path, 'r') as file:
        print(file.read())

def main():
    path = input('Enter the file path: ')
    print_content(path)

if __name__ == '__main__':
    main()