def tutorial(tutorial_question, main_menu):
    tutorial_question = input("Tutorial  Choices: Back")
    while tutorial_question == "Back":
        main_menu = input("Main Menu  Choices: Play/Credits/Tutorial ")
    else:
        print("That's not a choice kid... ")
        tutorial_question = input("Tutorial  Choices: Back")

def credits(credits_question, main_menu):
    credits_question = input("Credits  Choices: Back")
    while credits_question == "Back":
        main_menu = input("Main Menu  Choices: Play/Credits/Tutorial ")
    else:
        print("That's not a choice kid... ")
        credits_question = input("Tutorial  Choices: Back")

main_menu = input("Main Menu  Choices: Play/Credits/Tutorial ")
while main_menu == "Credits":
    credits()
while main_menu == "Tutorial":
    tutorial()
while main_menu == "Play":
    print("Here we go! ")
    break
else:
    print("That's not a choice kid... ")
    main_menu = input("Main Menu  Choices: Play/Credits/Tutorial ")