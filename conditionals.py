# True
# False

# not 
# and
# ==
# is
print('What is your age')
age = int(input())
if age >= 18 and age < 30:
    print(f'You\'re eligible to vote cuz you\'re {age} years old')
elif age >= 30:
    print('Go and Marry')
else:
    print(f'You\'re NOT eligible to vote cuz you\'re {age} years old')