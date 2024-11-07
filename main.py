# Programmers:  Leif LaBianca
# Course:  CS151, Professor Yalew
# Due Date: November 8 2024
# Programming Assignment:  PA3
# Problem Statement:  outputs a given ASCII art based on user input
# Data In: type of art requested, number of lines if applicable
# Data Out:  outputed ASCII art
# Credits: all original code

#imports the random function
import random

#function "circle" is defined
def circle():
    # prints a circle made up of asterisks
    print('         ******          ')
    print('    *****      *****     ')
    print('  ***              ***   ')
    print('**                     **')
    print('*                       *')
    print('**                     **')
    print('  ***              ***   ')
    print('    *****      *****     ')
    print('         ******          ')
    print()

#function "line" is defined
def line():
    #passthru variable is defined for loop cancellation
    passthru = False
    while not passthru:
        #user inputs the number of lines they want outputted
        line_count = input('Please enter the amount of lines you want to display: ')
        if not line_count.isdigit():
            print('This is an invalid input. Please express your count in the form of a positive whole number')
        else:
            #a counter is set up so that the loop will continue for the requested amount of lines
            line_count = int(line_count)
            current_count = 0
            while current_count < line_count:
                print('********************')
                current_count += 1
            print()
            passthru = True

#function "randomascii" is defined
def randomascii():
    #a variable is set to a random number from 0 to 2
    design = random.randint(0,2)
    #outputted ASCII depends on random number selected
    if design == 0:
        print('        ---------   ')
        print('-------|     *   |--')
        print('        ---------   ')
        print('       /     |      ')
        print('      /      |      ')
        print()
    elif design == 1:
        print(f'{"|":<10}{"|":>10}')
        print(f'{"|":<10}{"/ ":>9}')
        print(f'{"|":<10}{"/  ":>8}')
        print('-' * 15)
        print()
    elif design == 2:
        print(f'{"<":>5}{">":<5}')
        print(f'{"<<":>5}{">>":<5}')
        print(f'{"<<<":>5}{">>>":<5}')
        print(f'{"<<<<":>5}{">>>>":<5}')
        print(f'{"<<<<<":>5}{">>>>>":<5}')
        print(f'{"<<<<":>5}{">>>>":<5}')
        print(f'{"<<<":>5}{">>>":<5}')
        print(f'{"<<":>5}{">>":<5}')
        print(f'{"<":>5}{">":<5}')
        print()

#variable "wholepassthru" serves as end marker for the loop
wholepassthru = False
print('Welcome to the ASCII art generator.\nThis machine can generate a circle, a set number of lines, or a random choice of 3 designs')
while not wholepassthru:
    #two passthrus are defined for the main function for error checking
    passthru2 = False
    passthru3 = False
    while not passthru2:
        #the user selects one of the options, and the relevent function is executed to print the ASCII
        selected_output = input('What type of ASCII art would you like to generate?\nPlease express your answer in the form of the first letter: ')
        if selected_output.lower() == 'c':
            circle()
            passthru2 = True
        elif selected_output.lower() == 'l':
            line()
            passthru2 = True
        elif selected_output.lower() == 'r':
            randomascii()
            passthru2 = True
        else:
            print('This input is invalid.\nExpress your answer in the form of the first letter of the option (c,l,r)\n')
    while not passthru3:
        #the user is prompted to answer whether or not they would like to generate another ASCII
        continue_query = input('Would you like to generate another art piece?\nExpress your answer with y or n: ')
        if continue_query.lower() == 'y':
            print('Restarting...\n')
            passthru3 = True
        elif continue_query.lower() == 'n':
            print('Thank you for using our art generator!')
            passthru3 = True
            wholepassthru = True
        else:
            print('This input is invalid. Please express your query with y or n\n')



