main_menu = input("Main Menu  Choices: Play/Credits/Tutorial ")
if main_menu == "Credits":
    credits = input("Credits  Choices: Back ")
    if credits == "Back":
        main_menu = input("Main Menu  Choices: Play/Credits/Tutorial ")
    else:
        print("That's not a choice kid... ")
        credits = ("Credits  Choices: Back ")
if main_menu == "Tutorial":
    tutorial = input("Tutorial  Choices: Back ")
    if tutorial == "Back":
        main_menu = input("Main Menu  Choices: Play/Credits/Tutorial ")
    else:
        print("That's not a choice kid... ")
        tutorial = input("Tutorial  Choices: Back ")
if main_menu == "Play":
    print("Here we go! ")
else:
    print("That's not a choice kid... ")
    main_menu = input("Main Menu  Choices: Play/Credits/Tutorial ")