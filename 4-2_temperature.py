# this program assists a technician in the process of checking a substances temperature

# create a variable to represent the maximum temperature
max_temp = 102.5

# get the substances temperature
temperature = float(input('Enter the substances Celcius temperature: '))

# as long as necesary, instruct the user to adjust the thermostat
while temperature > max_temp:
    print('the temperature is too high')
    print('turn the thermostat down and wait 5 minutes')
    print('then take the temperature again and enter it')
    temperature = float(input('Enter the Celcius temperature: '))

# remind the user to check the temperature again in 15 minutes
print('the temperature is acceptable')
print('check it again in 15 minutes')
