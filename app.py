main_menu = input("Main Menu  Choices: Play/Credits/Tutorial ")

while True:
    if main_menu == "Credits":
        credits = input("Credits  Choices: Back ")
        if credits == 'Back':
            main_menu = input("Main Menu  Choices: Play/Credits/Tutorial ")
            continue
        
        else:
            print("That's not a choice kid... ")
            main_menu = input("Main Menu  Choices: Play/Credits/Tutorial ")
            continue

    if main_menu == "Tutorial":
        tutorial = input("Tutorial  Choices: Back ")
        if tutorial == 'Back':
            main_menu = input("Main Menu  Choices: Play/Credits/Tutorial ")
            continue
        else:
            print("That's not a choice kid... ")
            main_menu = input("Main Menu  Choices: Play/Credits/Tutorial ")

    if main_menu == "Play":
        print("Here we go! ")
        break

    else:
        print("That's not a choice kid... ")
        main_menu = input("Main Menu  Choices: Play/Credits/Tutorial ")
        continue