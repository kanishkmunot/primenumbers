import random
y = random.randint(1,100)
print(y)
for x in range(2,y-1):
    if y%x==0:
     print('Not a Prime Number')
     break
    else:
     print('Prime number')
     break
