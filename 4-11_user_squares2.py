# this program uses a loop to display a table of numbers and their squares

# get the starting limit
print('This program displays a list of numbers and their squares')
start = int(input('Enter the starting number '))

# get the ending limit
end = int(input('How high should I go? '))

# print the table headings
print()
print('Number\tSquare')
print('--------------')

# print the numbers and their squares
for number in range(start, end + 1):
    square = number**2
    print('\t', number, '\t', square)
