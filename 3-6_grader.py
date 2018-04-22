# this program gets a numeric test score from the user and displays the corresponding letter grade

# variables theo represent the grade thresholds
A_score = 90
B_score = 80
C_score = 70
D_score = 60

# get the test scores from the user
score = int(input('Enter your test score: '))

# determine the grade
if score >= A_score:
    print('your grade is A')
else:
    if score >= B_score:
        print('your grade is B')
    else:
        if score >= C_score:
            print('your grade is C')
        else:
            if score >= D_score:
                print('your grade is D')
            else:
                print('your grade is F')
