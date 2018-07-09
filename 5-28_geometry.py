# this program allows the user to choose various geometry calculations from a menu
# this program imports the circle and rectangle modules
import circle
import rectangle

# constants for the menu choices
AREA_CIRCLE_CHOICE = 1
CIRCUMFERENCE_CHOICE = 2
AREA_RECTANGLE_CHOICE = 3
PERIMETER_CHOICE = 4
QUIT_CHOICE = 5

# the main function
def main():
    # the choice variable controls the loop and holds the users menu choice
    choice = 0

    while choice != QUIT_CHOICE:
        # display the menu
        print()
        display_menu()

        # get the users choice
        choice = int(input('Enter your choice: '))
        print()
        # perform the selected action
        if choice == AREA_CIRCLE_CHOICE:
            radius = float(input('Enter the circles radius: '))
            print('The ares is', circle.area(radius))
        elif choice == CIRCUMFERENCE_CHOICE:
            radius = float(input('Enter the circles radius: '))
            print('The circumference is', circle.circumference(radius))
        elif choice == AREA_RECTANGLE_CHOICE:
            width = float(input('Enter the rectangles width: '))
            length = float(input('Enter the rectangles length: '))
            print('The ares is', rectangle.area(width, length))
        elif choice == PERIMETER_CHOICE:
            width = float(input('Enter the rectangles width: '))
            length = float(input('Enter the rectangles length: '))
            print('The perimeter is', rectangle.perimeter(width, length))
        elif choice == QUIT_CHOICE:
            print('Exiting the program')
        else:
            print('Error: invalid selection')

# the display_menu function displays a menu
def display_menu():
    print('MENU')
    print('1) Area of a circle')
    print('2) Circumference of a circle')
    print('3) Area of a rectangle')
    print('4) Perimeter of a rectangle')
    print('5) Quit')

# call the main function
main()