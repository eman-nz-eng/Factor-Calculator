import random
all_members = []

for item in range(0,5):

    # generate a random number
    mystery_num = random.randint(1,10)

    if mystery_num not in all_members:
        all_members.append(mystery_num)

all_members.sort()
print(all_members)