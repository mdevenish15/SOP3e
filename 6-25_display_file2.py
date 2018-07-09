# this program displays the contents of a file


def main():
    # get the name of a file
    filename = input('Enter a filename: ')

    try:
        # open the file
        infile = open(filename, 'r')

        # read the files contents
        contents = infile.read()

        # display the files contents
        print(contents)

        # close the file
        infile.close()
    except IOError:
        print('An error occurred trying to read the file', filename)


# call the main function
main()
