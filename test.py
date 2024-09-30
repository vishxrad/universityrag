import random
rand = random.randrange(1, 50, 1)

num = int(input("Enter number:"))
while num > 1 and num < 50:
    if num < rand:
        print("higher")
        num = int(input("Enter number:"))
        continue
    elif num > rand:
        print("lower")
        num = int(input("Enter number:"))
        continue
    else:
        print("yay")
        break
else:
    print("Enter number withing range") 
    