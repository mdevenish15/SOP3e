# this program displays a rectangular pattern of asterisks

rows = int(input('how many rows? '))
cols = int(input('how many columns? '))

for r in range(rows):
    for c in range(cols):
        print('*', end='')
    print()


