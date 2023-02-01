"""
THIS FILE WILL RUN AS CONTAINER
"""

def add_two_number(number1,number2):
    return number1 + number2

number1 =10
number2 = 15
#-------------------------------------------main-------------------------------------handler

def my_handler():
    try:
        number1 = 10
        number2 = 15
        result = add_two_number(number1,number2)
        print(f"SUM OF {number1} and {number2} is {result}")
    except Exception as e:
        print("ERROR EXCEPTION IN MAIN HANDLER",e)

#calling main handler
my_handler()