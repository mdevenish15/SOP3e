# this program demonstrates the list functions


def main():
    # first create an empty list
    word_list = []

    # show list status
    print()
    print('the list currently is: ')
    print(word_list)
    print()

    # get three names for the list
    print('Adding words to the list')
    word_1 = input('Enter word 1: ')
    word_2 = input('Enter word 2: ')
    word_3 = input('Enter word 3: ')

    # append the names to the list
    word_list.append(word_1)
    word_list.append(word_2)
    word_list.append(word_3)

    # show list status
    print()
    print('the list currently is: ')
    print(word_list)
    print()

    # return index 0 item
    print('returning the word from index 0')
    print(word_list[0])
    # return index 1 item
    print('returning the word from index 1')
    print(word_list[1])
    # return index 2 item
    print('returning the word from index 2')
    print(word_list[2])
    print()

    # insert a item into the list
    print('inserting a word into the list')
    word_4 = input('Enter the word to insert: ')
    index = int(input('Enter the index to insert word into list: '))
    word_list.insert(index, word_4)

    # show list status
    print()
    print('the list currently is: ')
    print(word_list)
    print()

    # sort the list
    print('sorting the list')
    word_list.sort()

    # show list status
    print('the list currently is: ')
    print(word_list)
    print()

    # reverse the order of the list
    print('reverse the list order')
    word_list.reverse()

    # show list status
    print('the list currently is: ')
    print(word_list)
    print()

    # remove an item from the list
    print('remove an item from the list')
    word_remove = input('Enter the word to remove from the list: ')
    word_list.remove(word_remove)

    # show list status
    print()
    print('the list currently is: ')
    print(word_list)
    print()

    # delete an element from the list
    print('delete an element from the list')
    word_delete = int(input('Enter the element to remove from the list: '))
    del word_list[word_delete]

    # show list status
    print()
    print('the list currently is: ')
    print(word_list)
    print()

    # show the min max functions
    number_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    # display list
    print('the number list is: ')
    print(number_list)
    print()

    # show the min function
    print('minimum number is: ')
    print(min(number_list))

    # show the max number
    print('maximum number is: ')
    print(max(number_list))

    # copy a list
    print('copy the word_list to my_list')
    my_list = word_list
    print('display my_list')
    print(my_list)


# call the main function
main()