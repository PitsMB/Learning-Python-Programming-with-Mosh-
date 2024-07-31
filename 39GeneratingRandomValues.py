#Generating Random Values

import random

members = ['John', 'Pits', 'Mac']

leader = random.choice(members)

print(leader)

for i in range(3):
    print(random.randint(10, 20))