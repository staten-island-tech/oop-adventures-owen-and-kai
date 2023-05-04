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
        player_story_name = player_username
        player_age = int(input("What is your age? "))
        player_story_age = player_age
        player_gender = input("What is your gender? ")
        if player_gender == "M":
            player_pronouns = "He"
            break

        if player_gender == "F":
            player_pronouns = "She"
            break

        else:
            print("That's not a gender kid... ")
            player_gender = input("What is your gender? ")
            continue

backstory_skip = input("Would you like to skip the backstory? Y/N")
while True:
    if backstory_skip == "Y":
        break

    if backstory_skip == "N":
        backstory = input()

    else:
        print("That's not a choice kid... ")
        continue