# this program demonstrates the insert method

def main():
    # create a list with some names
    names = ['James', 'Kathryn', 'Bill']

    # display the list
    print('the list of names before the insert')
    print(names)

    # insert a new name into the list at element 0
    names.insert(0, 'Joe')

    # display the list again
    print('the list of names after the insert')
    print(names)

# call the main function
main()