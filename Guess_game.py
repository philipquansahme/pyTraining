import  random

lucky_num = int(random.uniform(1, 30))

# ===============================================
# This section is my sh*t till i got the answer 
# ===============================================
# print('Enter your lucky number')
# user_input = input()

# for i in range(1, 7, 1):
#     print('Enter your lucky number')
#     user_input = input()

# while  count < 7 and user_input != lucky_num : 
#     print('Sorry, Try Again')
#     user_input = input()
# else:
#     print('Thank you for try')
# print('Congratulation you have won yourself a python documentation')


# print(f'The lucky number is {lucky_num}')

# while user_input != lucky_num :
#     for i in range(1, 6, 1):
#         if user_input != lucky_num :
#             print('Sorry, Try Again')
#             user_input = input()
#         else:
#             break       


#     print(f'The lucky number is {lucky_num}')
#     # user_input = lucky_num
# else:
#     print('Congratulation you have won yourself a python documentation')
# print(f'The lucky number is {lucky_num}')
# for i in range(1, 6, 1):
#     while i < 6 :
#         print('Sorry, Try Again')
#         user_input = input() 
#     else:
#         print('Congratulation you have won yourself a python documentation')


print('What is your name?')
player_name = input()

print(f'{player_name.capitalize()}, Enter your lucky number')
user_input = int(input())

# uncomment line below to show the lucky number
# print(f'The lucky number is {lucky_num}')

# =======================================
# This section is with an 'if' condition
# =======================================
# for i in range(1,6,1):
#     if user_input != lucky_num :
#         print('Enter your lucky number')
#         user_input = int(input())
#     else:
#         print(f'Hurray! the lucky number is {lucky_num } \t Congratulation {player_name} you have won yourself a python progress')
#         break
# if user_input != lucky_num:
#     print('Better luck next time')  


# =========================================
# This section is with a 'while' loop
# =========================================
for i in range(1,6,1):
    while user_input != lucky_num :
        print('Sorry try again')
        user_input = int(input())
        break
    else:
        print(f'Hurray! the lucky number is {lucky_num }\nCongratulations {player_name.capitalize()} you have won yourself a python progress')
        break
if user_input != lucky_num:
    print(f'The lucky number is {lucky_num}\nBetter luck next time {player_name.capitalize()}')  
