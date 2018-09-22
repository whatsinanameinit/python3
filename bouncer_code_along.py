#ask for age
age = input("How old are you? \n")

if age:
    if int(age) >= 18 and int(age) < 21:
        print("You can enter, but need a wristband!")
    elif int(age) >= 21:
        print("You can enter normally!")
    else:
        print("Too young, sorry!")
else:
    print("Write something duhh")
