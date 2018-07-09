# this program gets employee data from the user and saves it as a record in the employee.txt file

def main():
    # get the number of employee records to create
    num_emps = int(input('How many employee records do you want to create? '))

    # open a file for writing
    emp_file = open('employee.txt', 'w')

    # get each emplyees data and write it to the file
    for count in range(1, num_emps + 1):
        # get the data for an emplyee
        print('Enter data for employee #', count, sep='')
        name = input('Name: ')
        id_num = input('ID number: ')
        dept = input('Department: ')

        # write the data as a record to the file
        emp_file.write(name + '\n')
        emp_file.write(id_num + '\n')
        emp_file.write(dept + '\n')

        # display a blank line
        print()

    # close the file
    emp_file.close()
    print('Employee records written to employees.txt')

# call the main function
main()