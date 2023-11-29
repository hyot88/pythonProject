import random

data = list(range(1, 46))


def poppop(data):
    choice_num = random.choice(data)
    print(choice_num, end=" ")
    data.remove(choice_num)
    return data


for i in range(6):
    data = poppop(data)