main_menu = input("Main Menu  Choices: Play/Credits/Tutorial ")

while True:
    if main_menu == "Credits":
        credits = input("Credits  Choices: Back ")
        if credits == 'Back':
            main_menu = input("Main Menu  Choices: Play/Credits/Tutorial ")
            continue

        else:
            print("That's not a choice kid... ")
            credits = input("Credits  Choices: Back ")
        continue
        
    if main_menu == "Tutorial":
        tutorial = input("Tutorial  Choices: Back ")
        if tutorial == 'Back':
            main_menu = input("Main Menu  Choices: Play/Credits/Tutorial ")
            continue

        else:
            print("That's not a choice kid... ")
            tutorial = input("Tutorial  Choices: Back ")
        continue

    if main_menu == "Play":
        print("Here we go! ")
        break

    else:
        print("That's not a choice kid... ")
        main_menu = input("Main Menu  Choices: Play/Credits/Tutorial ")
    continue

player_customization_screen = input("Welcome to the player customization screen, here you will make your own custom player that will progress through the story. Please refrain from using any personal information as we will not take any responsibility if your information gets leaked, thank you.  Choices: Continue ")

while True:
    if player_customization_screen == "Continue":
        player_username = input("The next King/Queen of Boxing will be: ")
        player_age = input("What is your age? ")
        player_gender = input("What is your gender? ")
        backstory_skip = input("Would you like to skip the backstory? Y/N ")