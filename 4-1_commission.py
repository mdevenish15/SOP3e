# this program calculates sales commissions

# create a variable to control the loop
keep_going = 'y'

# calculate a series of commissions
while keep_going == 'y':
    # get a salespersons sales ans commission rate
    sales = float(input('Enter the amount of sales: '))
    comm_rate = float(input('Enter the commission rates: '))

    # calculate the commission
    commission = sales * comm_rate

    # display the commission
    print('the commission is $', format(commission, ',.2f'), sep='')

    # see if the user wants to do another
    keep_going = input('Do you want to calculate another commission(enter y for yes): ')
    