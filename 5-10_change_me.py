# thios program demonstrates what happens when you change the value of a parameter

def main():
    value = 99
    print('the value is', value)
    change_me(value)
    print('back in the main the value is', value)

def change_me(arg):
    print('I am changing the value')
    arg = 0
    print('now the value is', arg)

# call the main function
main()
