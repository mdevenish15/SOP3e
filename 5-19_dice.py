# this program simulates the rolling of dice
import random

# constants for the minimum and maximum random numbers
MIN = 1
MAX = 6

def main():
    # create a variable to control the loop
    again = 'y'

    # simulate the rolling of the dice
    while again == 'y' or again == 'Y':
        print('Rolling the dice......')
        print('their values are:')
        print(random.randint(MIN, MAX))
        print(random.randint(MIN, MAX))

        # do another roll?
        again = input('Roll them again? (y = yes): ')

# call the main function
main()