import json
import pickle

with open('group.pickle', 'rb') as f:
    my_favourite_group = pickle.load(f)
print(my_favourite_group)
with open('group.json', 'r', encoding='utf-8') as f:
    my_favourite_group = json.load(f)
print(my_favourite_group)
