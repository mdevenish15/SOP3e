# this program uses the return value of a function

def main():
    # get the users age
    first_age = int(input('Enter your age: '))

    # get the users friend age
    second_age = int(input('Enter your friends age: '))

    # get the sum of both ages
    total = sum(first_age, second_age)

    # display the total age
    print('Together you are', total, 'years old')

# the sum function accepts two numeric arguments and returns the sum of those two arguments
def sum(num1, num2):
    result = num1 + num2
    return result
    # return num1 + num2                # simpler way

# call the main function
main()
