name = input("Please, type your name: ")
print("Welcome to this adventure,", name + "!")

answer = input("You're on a dirt road, it has come to an end and you can go left or right. Which way would you like to go? ").lower()

if answer == "left":
    answer == input("You come to a river. You can walk around it or swim accross. (walk / swim): ").lower()
    
    if answer == "walk":
        print("You walker for many miles and ran out of water.")
    elif answer == "swim":
        print("You swam accross and were eaten by an alligator.")
    else:
        print("Not a valid option. You lose. :(")

elif answer == "right":
    answer == input("You come to a bridge, it looks wobbly. Do you want to cross it or head back? (cross / back): ").lower()
    
    if answer == "cross":
        answer == input("You cross the bridge and meet a stranger. Talk to them? (yes / no): ").lower()
        
        if answer == "yes":
            print("You talk to the stranger and they give you gold. You win! =D")
        elif answer == "no":
            print("You ignore the stranger. They're offended. You lose.")
        else:
            print("Not a valid option. You lose. :(")

    elif answer == "back":
        print("You go back and lose.")
    else:
        print("Not a valid option. You lose. :(")

else:
    print("Not a valid option. You lose. :(")

print("Thank you for trying,", name + "!")