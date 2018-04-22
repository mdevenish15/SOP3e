# this program calculates retail prices

mark_up = 2.5               # the retail markup percentage
another = 'y'               # variable to control the loop

# process one or more items
while another == 'y' or another == 'Y':
    # get the wholesale cost
    wholesale = float(input('Enter the items wholesale cost: '))

    # calculate the retail price
    retail = wholesale * mark_up

    # display the retail price
    print('Retail price: $', format(retail, ',.2f'))

    # do this again?
    another = input('Do you have another item? (Enter y for yes): ')
