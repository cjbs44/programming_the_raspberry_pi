import random
print('Dice 1    Dice 2')
for x in range(1,11):
    throw_1 = random.randint(1,6)
    throw_2 = random.randint(1,6)
    print(throw_1,'       ',throw_2)
    total = throw_1 + throw_2
    if total == 7:
        print('Seven Thrown!')
    elif total == 11:
        print('Eleven Thrown!')
    elif throw_1 == throw_2:
        print('Double Thrown!')
    elif not (total < 5 or total > 9):
        print('not bad')
    elif total > 10:
        print('Good Throw!')
    else:
        print('Unlucky!')
        
    
