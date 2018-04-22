# this program converts the speeds 60kph thru 130kph (in 10 kph increments) to mph

start_speed = 60                # starting speed
end_speed = 131                 # ending speed
increment = 10                  # speed increment
conversion_factor = 0.6214      # conversion factor

# print the table headings
print('KPH \t\t MPH')
print('--------------')

# print the speeds
for kph in range(start_speed, end_speed, increment):
    mph = kph * conversion_factor
    print(kph, '\t\t', format(mph, '.1f'))
