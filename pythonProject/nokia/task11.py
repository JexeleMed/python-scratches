import random

def refactor(dices):
    y =0
    for i in dices:
        if i == 1:
            dices[y] = random.randrange(1, 7)
        y+=1

    dices = [x for x in dices if x <=3 != 0]
    dices = random.choices(range(1, 7, ), k=len(dices))
    dices = [x for x in dices if x <= 3 != 0]
    return dices


roll = random.choices(range(1, 7,), k=420)
n = 0
while n <2101:
    roll =(refactor(roll))
    n +=1


print(len(roll))
