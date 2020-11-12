import json
import pickle

my_favourite_group = {'name': 'The Prodigy',
                      'tracks': ['Narayan', 'Smack my bitch up'],
                      'Albums': [{'name': 'The Fat of the Land', 'year': 1997},
                                 {'name': 'Experience', 'year': 1992}]}

with open('group.pickle', 'wb') as f:
    pickle.dump(my_favourite_group, f)
with open('group.pickle', 'rb') as f:
    print(f.read())
with open('group.json', 'w', encoding='utf-8') as f:
    json.dump(my_favourite_group, f)
with open('group.json', 'r') as f:
    print(f.read())
