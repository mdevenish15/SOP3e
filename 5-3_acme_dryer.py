# this program displays step-by-step instructions for disassembling an Acme dryer
# the main function performs the programs main logic

def main():
    # display the startup message
    startup_message()
    input('Press Enter to see step 1')
    # display step 1
    step1()
    input('Press Enter to see step 2')
    # display step 2
    step2()
    input('Press Enter to see step 3')
    # display step 3
    step3()
    input('Press Enter to see step 4')
    # display step 4
    step4()

# the startup message function displays the programs initial message on the screen
def startup_message():
    print('this program tells you how to  dissassemble an ACME laundry dryer')
    print('there are 4 steps in the process')
    print()

# the step1 function displays the instructions for step1
def step1():
    print('Step 1: unplug the dryer and move it away from the wall')
    print()

# the step2 function displays the instructions for step2
def step2():
    print('Step 2: remove the six screws from the back of the dryer')
    print()

# the step3 function displays the instructions for step3
def step3():
    print('Step 3: remove the back panel from the dryer')
    print()

# the step4 function displays the instructions for step4
def step4():
    print('Step 4: pull the top of the dryer straight up')
    print()

# call the main function
main()