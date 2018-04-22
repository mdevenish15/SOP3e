# this program displays property values

tax_factor = 0.0065         # represents the tax facter

# get the first lot number
print('Enter the property lot number or enter 0 to end')
lot = int(input('Lot number: '))

# continue processing as long as the user does not enter lot number 0
while lot != 0:
    # get the property value
    value = float(input('Enter the property value: '))

    # calculate the property tax
    tax = value * tax_factor

    # display the tax
    print('Property tax: $', format(tax, ',.2f'), sep='')

    # get the next lot number
    print('Enter the next lot number or enter 0 to end')
    lot = int(input('Lot number: '))
    