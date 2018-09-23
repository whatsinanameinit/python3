While loops

We can also iterate using a while loop instead of a for loop
Format is

>while im_tired:
    seek caffine

while loop will continue to execute while a certain condition is truthy and will end when they become false

> user_response= None
> while user_response != "please":
    user_response = input("Ah ah ah", you didnt say the magic word: ")

While loops requires more careful setup than a forloop since you have to specify the termination condition manually

Be careful! If the conditons does not become false these will loop forever.

example of a loop for both for and while loop

for num in range(1,11):
    print(num)

num=1
while num < 11
    print(num)
    num += 1
