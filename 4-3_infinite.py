# this program demonstrates an infinite loop
# create a variable to control the loop
keep_going = 'y'

# warning! infinite loop!
while keep_going == 'y':
    # get the salespersons sales and commission rate
    sales = float(input('Enter the amount of sales: '))
    comm_rate = float(input('Enter the commission rates: '))

    # calculate the commission
    commission = sales * comm_rate

    # display the commission
    print('the commission is $', format(commission, ',.2f'), sep='')