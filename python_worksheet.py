# python page to work through concepts and examples

# comment  (comments are preceded by #)
print('****************************************************')

# Hello World Program
print('Hello World')

# long statements can be broken into multiple lines - use a \
print('\nlong statements can be broken into multilines by the use', \
      'of the "\\" key and the "+" key')

# display multiple lines with the + operator
print('this long statement is broken up into multiple' + \
      'lines with the use of the "+" key')


# print('text') always ends with a newline
# suppressing the print functions ending newline
# print('text', end='')
print("\nto print without a newline, use end=''")
print('one', end='')
print('two', end='')

print('\n')
print("\nto specify item separator, use sep='' for nor space, sep='*' for * separator, etc")
print('one', 'two', 'three', sep='')
print('one', 'two', 'three', sep='*')

print('\nescape characters')
print('use the "\\" key')
# \n    newline
# \t    tab
# \'    single quote
# \"    double quote
# \\    bashslash


print('\n')
print('****************************************************')
print('**Print functions**')
# print function
print("Hello World - double quotes")
print('Hello World - single quotes')

# print with both double and single quotes
print("I'm ready!")
print('shout "Hello World!!"')

print('****************************************************')
print('**Variables**')
# variables
width = 10
length = 5
print(width)
print("width")                  # this will print the word 'width' not the variable assigned
print(length)

# variable naming conventions
# first character must be a-z, A-Z or underscore _
# after the first character may use a-z, A-Z, 0-9, or underscore _
# UPPERCASE and lowercase characters are distinct, width and Width are different variables
# popular naming convention in python is to use underscore to represent space between words in variable name
# ie. gross_pay, pay_rate

# display multiple items with the print function
room = 503
print("I am staying in room number", room)
my_name = 'Tom'
print('My name is', my_name, 'and I am staying in room number', room)

print('****************************************************')
print('**Data types**')
# data types
# an integer is stored as an int
print('the integer 1 is stored as',type(1))
# a real number is stored as a float
print('the real number 1.0 is stored as', type(1.0))
# a string is stored as a str
print('the string, "Tom" is stored as', type('Tom'))

print("\n")
print('**Data conversion**')
# function that converts string values
age = 10.5
print('age in integers: ', int(age))
print('age in float is: ', float(age))

print('****************************************************')
print('**Input - from keyboard**')
# input function reads a piece of data entered at the keyboard and returns that data as a string to the program
# variable = input(prompt)
# input does not display a space after last character of prompt
number = input('Enter a number: ')
print('the number you entered was ........', number)

# data conversion of input in single statement
print('data conversion example: enter 1.5')
hours = int(float(input('How many hours did you work? ')))
print('hours worked =', hours)

print('****************************************************')
print('**Calculations**')
# addition +                            # adds two numbers
# subtraction -                         # subtracts one number from another
# multiplication *                      # multiplies one number by another
# division /                            # divides one number by another and gives a float result
# integer division //                   # divides one number by another and gives int result
# remainder %               (modulus)   # divides one number by another abd gives remainder
# exponent **                           # raises a number to a power

# operator precedence
# 1. exponents                                  **
# 2. multiplication, division, remainder        * / // %
# 3. addition, subraction                       + -

# examples
print('5/2 = ', 5/2)
print('5//2 = ', 5//2)
print('5%2 = ', 5%2)
print('5**2 = ', 5**2)

print('****************************************************')
print('**Formatting numbers**')
# to format numbers use the format function
# format float          f
# format scientific     e
# format percentage     %
# format integer        d

print('format [column width][, comma separator], [decimal precision], [type ~ f/e/%/d]')

# format(12345.6789, '.2f') will format the number (f~float to 0.2 precision)
print('\nto format a number use the format function,' + " format(number, \'0.2f\')")
print(format(12345.6789, '0.1f'), '\t1 decimal place')
print(format(12345.6789, '0.2f'), '\t2 decimal place')
print(format(12345.6789, '0.3f'), '\t3 decimal place')
print(format(12345.6789, '0.4f'), '\t4 decimal place')

print('\nto format in scientific notation use "e" instead of f')
print(format(12345.6789, 'e'))
print('\nto insert comma separators in numbers use "\',.2f\'"')
print(format(12345.6789, ',.2f'))
print('\nto specify a minimum field width use "\'12,.2f\'" for a column width of 12')
print('the number is', format(12345.6789, '12,.2f'))
print('\nto format in a percentage use "%" instead of f')
print(format(0.5, '%'))
print('for 0 precision, use "\'.0%\'"')
print(format(0.5, '.0%'))
print('integer formatting - use d')
print(format(123456, '10,d'))

print('****************************************************')
print('**Decision Structures and Boolean Logic**')

#     >         greater than
#     <         less than
#     >=        greater than or equal to
#     <=        less than or equal to
#     ==        equal to
#     !=        not equal to

# if statement
# if condition:
#      statement for true
print('use the if statement for conditions true')

print('use the if-else statement, if for true, else for false - dual decision')

print('use nested if-elif-else statement for more that one condition')

print('\nlogic operators ~ and(&&) or(||) not(!=)')

print('****************************************************')
print('**Repetition Structures**')

print('while loop - condition controlled loop')
# the while loop is a pre-test loop - the condition is tested before each iteration

print('for loop - count controlled loop')
# the for loop while iterates through a sequence

print('range function')
# range([first item], [last item], [step value (can be negative)])

print('**augmented assignment operators**')
print('x = x + num \t\t x += num')
print('x = x - num \t\t x -= num')
print('x = x * num \t\t x *= num')
print('x = x / num \t\t x /= num')
print('x = x % num \t\t x %= num')

print('\nSentinel is a special value that marks the end of a sequence of values')



