# this program gets three test scores and displays their average
# it congratulates the user if the average score is a high score

# the high score variable holds the value that is considered a high score
high_score = 95

# get the three test scores
test1 = float(input('Enter the first test score: '))
test2 = float(input('Enter the second test score: '))
test3 = float(input('Enter the third test score: '))

# calculate the average of the three scores and assign the result to the average variable
average = (test1 + test2 + test3) / 3.0

# display the average
print('the average test score is', average)

# if the average is a high score congratulate the user
if average >= high_score:
    print('Congratulations!')
    print('that is a great average!')

