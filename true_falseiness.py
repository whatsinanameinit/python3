if 0:
    print("Yay!")
if 1:
    print("Yay?")

#The o/p is Yay? as by default 1 is always true and 0 is always false
#take advantage of inherent truithiness and falsiness

animal=input("Enter your favourite animal \n")

if animal: #What this line does is that it checks if i put anything in. So if animal is empty then this wont get executed
# So empty strings , empty objects , none and Zero are all falsy!
    print(animal + " is my favourite too")
else:
    print("Say something")
