import random
import time


def pause(scentence):
    print(scentence)
    time.sleep(2)


def game_scenario():
    pause("It's 1 am, you find yourself laying on your bed watching tiktoks ")
    pause("You look to your right and you see your to-do list un-touched")
    pause("you are shook at how quickly time passed")


game_scenario()


flag1 = bool(False)
flag2 = bool(False)
while (True):
    # to exit the while loop if user doesn't wanna play
    if(not flag2):

        option = input(
            "enter (a) calm yourself down \nenter (b) get to the tasks "
                      )
        if (option.lower().strip() == "a"):
            if(not flag1):
                print(
                    "You take a deep breath and you choose"
                    "to forgive and be kind to yourself "
                    )

                print("you won clarity of mind")
                flag1 = bool(True)
            else:
                print("you are already calm ")
        elif (option.lower().strip() == "b"):
            while(True):
                # cry
                if(not flag1):
                    print(random.choice(
                        ["You are in a state of shock from how late"
                         "it is so you feel like you're so"
                         "close to having a panic attack",
                         "You are too mad at yourself for"
                         "procrastinating all day"
                         "so you cry non-stop"]))
                    print("You look at yourself in the mirror"
                          "realizing that you might not be in the right"
                          "state of mind to start working on your tasks ")
                # support
                elif(flag1):
                    print("you feel more calm ready to face the task")

                option2 = input("enter (a) Do task (b) avoid task")
                if (option2.lower().strip() == "b"):
                    break
                elif(option2.lower().strip() == "a"):
                    if(not flag1):
                        print("You failed to cope with the situation correctly"
                              ", so you end up quitting your job cuz you think"
                              " it's too overwhelming for you. Tragical fail!")
                    else:
                        print("You learn from the mistake and you develop a"
                              " solution plan that"
                              " help you get back on track."
                              " That's how to win when you mess up <33 ")
                    while(True):
                        option3 = input("wanna play again? y/n ")
                        if (option3.lower().strip() == "y"):
                            game_scenario()
                            # to reset the value of getting the sword to False
                            flag1 = bool(False)
                            break
                        elif (option3.lower().strip() == "n"):
                            print("thanks for playing. Bye!")
                            flag2 = bool(True)
                            break
                    break
