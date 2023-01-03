from requests import get

# # Lists and Tuples
# # Lists
# names = ('Badrudin', 'Ali', 'Mohamed', "Hassan")
# names.reverse()
# names.sort()
# names.append('Ahmed')
# names.clear()
# print(names)

# sending http get request
response = get('https://jsonplaceholder.typicode.com/users')
# Read dictionary

users = response.json();
for user in users:
    print(user['name'])












# # Dictionary and sets


# people = [
#     {
#         'name': 'Mohamed',
#         'age': 19,
#         'isOld': False
#     },
#     {
#         'name': 'AHmed',
#         'age': 50,
#         'isOld': True
#     }
# ]

# print(people[0])







# OOPs