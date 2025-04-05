print("Welcome to Glens Arena Game") # greet the player

def playGame1():
    print("Welcome to the Arena  .")
    choices = ["Pick up Axe", "Look around for a torch", "Walk around the room in the dark"]
    while True:
        print("You awake to the loud roar of a crowd, you look around the room, you can barely see, you hear metal hitting metal, and what seems to be a fight just outside, What do you do?")
        for index, c in enumerate(choices):
            print(str(index) + ": " + c)
        answer = int(input("Please enter a number from the list: "))
        if(answer == 0 or answer == 2):
            print("You pick up an Axe, you walk towards where you think the fight is taking place but since you cant see much you trip on a stone and get knocked unconscious >_<;;;")
            break
        elif(answer == 1):
            print("You pick up the torch, you can now see a large musty stone chamber that you seem to be locked in, there is a small crawl space that you can escape from,  Nice job You Win!")
            # playGame2()
            break
        else:
            print("Please enter 0, 1, or 2")
        

while True:
    print("MAIN MENU")
    # get user input and save into a variable
    answer = input("Are you ready to play? (type 'yes' or 'no')")

    if answer == "yes":
        print("Okay, let's begin.")

        playGame1()

        break
    elif answer == "no":
        print("Goodbye")
        break
    else:
        print("Please write 'yes' or 'no' and hit Enter: ")