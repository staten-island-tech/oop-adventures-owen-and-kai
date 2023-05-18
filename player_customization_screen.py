def player_customization_screen_gui():    
    while True:
        player_customization_screen = input("Welcome to the player customization screen, here you will make your own custom player that will progress through the story. Please refrain from using any personal information as we will not take any responsibility if your information gets leaked, thank you.  Choices: Continue ")
        if player_customization_screen == "Continue":
            player_username = input("The next King/Queen of Boxing will be: ")
            player_story_name = player_username
            player_age = int(input("What is your age? "))
            player_story_age = player_age
            player_gender = input("What is your gender? M/F ")
            if player_gender == "M":
                player_pronoun1 = "He"
                player_pronoun2 = "Him"
                player_pronoun3 = "His"
                break

            if player_gender == "F":
                player_pronoun1 = "She"
                player_pronoun2 = "Her"
                player_pronoun3 = "Hers"
                break

            else:
                print("That's not a gender kid... ")
                continue

        else:
            print("That's not a choice kid... ")
            player_customization_screen = input("Welcome to the player customization screen, here you will make your own custom player that will progress through the story. Please refrain from using any personal information as we will not take any responsibility if your information gets leaked, thank you.  Choices: Continue ")
            continue