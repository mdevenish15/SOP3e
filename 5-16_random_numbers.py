# this program displays a random number in the range of 1 thru 10
import random

def main():
    # get a random number
    number = random.randint(1, 10)
    # display the number
    print('the number is', number)

# call the main function
main()