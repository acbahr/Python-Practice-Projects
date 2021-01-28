

import re

print("My Magical Calculator")
print("Type 'quit' to exit.\n")

previous = 0
run = True

def performMath():
# global inputs the run variable into the function - delete global and see run in function change color
    global run
    global previous
    equation = ""
    if previous == 0:
        equation = input("Enter equation: ")
    else:
        equation = input(str(previous))
    if equation == 'quit':
        print("Goodbye, human.")
        run = False
    else:
# eval evaluates the equation but can be problematic. Runs python code, etc. Regex keeps from entering anyhting but #s
# eval can be dangerous. Re.sub makes sure nothing specified can be input
        equation = re.sub('[a-zA-Z,.():" "]', '', equation)
        if previous == 0:
            previous = eval(equation)
        else:
            previous = eval(str(previous) + equation)


while run:
    performMath()

