# this program displays the records that are in the employees.tx file


def main():
    # open the employees.txt file
    emp_file = open('employee.txt', 'r')

    # read the first line from the file, which is the name of the first record
    name = emp_file.readline()

    # if a field was read, continue processing
    while name != '':
        # read the ID number
        id_num = emp_file.readline()

        # read the department field
        dept = emp_file.readline()

        # strip the newlines from the fields
        name = name.rstrip('\n')
        id_num = id_num.rstrip('\n')
        dept = dept.rstrip('\n')

        # display the record
        print('Name:', name)
        print('ID:', id_num)
        print('Dept:', dept)

        # read the name field of the next record
        name = emp_file.readline()

    # close the file
    emp_file.close()


# call the main function
main()
