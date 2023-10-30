import random

names_string = ['Angela', 'Ben', 'Jenny', 'Michael', 'Chloe'];
names = names_string.split(", ")

names_count = len(names) - 1

random_list_val = random.randint(0, names_count)
print(names[random_list_val])