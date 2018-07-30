# this program reads a files contents into a list


def main():
    infile = open('cities.txt', 'r')

    # read the contents of the file into a list
    cities = infile.readlines()

    # cloe the file
    infile.close()

    # print the contents of the list
    print(cities)

    # strip the \n from each element
    index = 0
    while index < len(cities):
        cities[index] = cities[index].rstrip('\n')
        index += 1

    # print the contents of the list
    print(cities)


# call the main function
main()
