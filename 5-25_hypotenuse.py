# this program calcualtes the length of a right triangle hypotenuse
import math

def main():
    # get the length of the triangles two sides
    a = float(input('Enter the length of side A: '))
    b = float(input('Enter the length of side B: '))

    # calculate the length of the hypotenuse
    c = math.hypot(a, b)

    # display the length of the hypotenuse
    print('The length of the hypotneuse if', c)

# call the main function
main()