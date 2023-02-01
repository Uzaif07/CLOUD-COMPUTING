"""
THIS FILE WILL RUN AS CONTAINER
"""

def add_two_number(number1,number2):
    return number1 + number2

# number1 = int(input("ENTER FIRST NUMBER : "))
# number2 = int(input("ENTER SECOND NUMBER: "))

#-------------------------------------------main-------------------------------------handler

def my_handler():
    try:
        number1 = int(input("ENTER FIRST NUMBER : "))
        number2 = int(input("ENTER SECOND NUMBER : "))
        result = add_two_number(number1,number2)
        print(f"SUM OF {number1} and {number2} is {result}")
    except Exception as e:
        print("ERROR EXCEPTION IN MAIN HANDLER",e)

#calling main handler
my_handler()