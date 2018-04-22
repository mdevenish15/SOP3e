# this program calculates a retail items sale price

# DISCOUNT_PERCENTAGE is used as a global constant for the discount percentage
DISCOUNT_PERCENTAGE = 0.20

# the main function
def main():
    # get the items regular price
    reg_price = get_regular_price()

    # calculate the sale price
    sale_price = reg_price - discount(reg_price)

    # display the sale price
    print('The sale price is $', format(sale_price, ',.2f'), sep='')

# the get_regular_price function promts the user to enter an items regular price and it returns that value
def get_regular_price():
    price = float(input('Enter the items regular price: '))
    return price

# the discount functionaccepts an items price as an argument and returns the amount of
# the discount, specified by the DISCOUNT_PERCENTAGE
def discount(price):
    return price * DISCOUNT_PERCENTAGE

# call the main function
main()