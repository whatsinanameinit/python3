from random import randint
num = randint(1,1000)
print(num)
if num  == 1:
    print("odd")
elif num % 2 ==0:
    print("even")
else:
    print("odd")

# you can have only one if and only one else but you can have multiple elif.
