# this program determines whether a bank customer qualies for a load

min_salary = 30000.0        # minimum annual salary
min_years = 2               # minimum years on the job

# get the customers annual salary
salary = float(input('Enter your annual salary: '))

# get the number of years on the current job
years_on_job = int(input('Enter the number of years employed: '))

# determine whether the customer qualifies
if salary >= min_salary and years_on_job >= min_years:
    print('you qualify for the loan')
else:
    print('you do not qualify for the loan')