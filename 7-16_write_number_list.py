# this progam saves a list of numbers to a file


def main():
    # creat a list of numbers
    numbers = [1, 2, 3, 4, 5, 6, 7]

    # open a file for writing
    outfile = open('numberslist.txt', 'w')

    # write the list to the file
    for item in numbers:
        outfile.write(str(item) + '\n')

    # close the file
    outfile.close()


# call the main function
main()
