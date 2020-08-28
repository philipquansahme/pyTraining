import json

userJSON = '{"firstname": "Jack", "lastname": "Daniels", "age": 100}'

# parse to dictionary
user1 = json.loads(userJSON)

print(user1['firstname'])

# parse from dictionary to JSON 
books = {'Novel': 'City Escape', 'Journal': 'The Good News'}

new_books = json.dumps(books)

print(new_books)