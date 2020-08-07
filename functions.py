# def add_numbers(num1, num2=None):
#     try:
#         total = num1 + num2
#         return total
#     except:
#         print("An error happened")

# print(add_numbers(5))


#WHILE LOOP
#BREAK, CONTINUE, PASS
#SCOPING WHEN IT COMES TO FUNCTIONS
#TRY AND EXCEPT(CATCH) BLOCK
#COME UP WITH YOUR OWN EXAMPLE ON FUNCTIONS


def div(num):
    try:
        return  42 / num
    except ZeroDivisionError:
        print('Error: You can\'t divide by zero')

print(div(2))
print(div(12))
print(div(0))
print(div(1))
print(div(6))





