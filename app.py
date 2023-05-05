main_menu = input("Kai and Owen Productions Presents: Punch-A-Looza!  Choices: Play/Credits/Tutorial ")

while True:
    if main_menu == "Credits":
        credits = input("Main Developers: Kai and Owen Productions  Teacher: Mr. Whalen  Side Contributors: Yan Sharma  People we USED to copy from: Gabe Liberov and Yizhak Zoltan  Choices: Back ")
        if credits == 'Back':
            main_menu = input("Kai and Owen Productions Presents: Punch-A-Looza!  Choices: Play/Credits/Tutorial ")
            continue

        else:
            print("That's not a choice kid... ")
            credits = input("Main Developers: Kai and Owen Productions  Teacher: Mr. Whalen  Side Contributors: Yan Sharma  People we USED to copy from: Gabe Liberov and Yizhak Zoltan  Choices: Back ")
            continue
        
    if main_menu == "Tutorial":
        tutorial = input("The concept of this game is rather simple. You can use 6 different attacks that can be blocked with their corresponding blocks(e.g. Jabs will be blocked by the move Block Jab). You will be using these attacks and defenses in turns to avoid any exploits and spamming. Everytime you attack you will lose stamina which can be replenished by resting. However, resting will result in sacrificing your turn. That's really all there is to this game, so go out there and becoming the next boxing star of the world!  Choices: Back ")
        if tutorial == 'Back':
            main_menu = input("Kai and Owen Productions Presents: Punch-A-Looza!  Choices: Play/Credits/Tutorial ")
            continue

        else:
            print("That's not a choice kid... ")
            tutorial = input("The concept of this game is rather simple. You can use 6 different attacks that can be blocked with their corresponding blocks(e.g. Jabs will be blocked by the move Block Jab). You will be using these attacks and defenses in turns to avoid any exploits and spamming. Everytime you attack you will lose stamina which can be replenished by resting. However, resting will result in sacrificing your turn. That's really all there is to this game, so go out there and becoming the next boxing star of the world!  Choices: Back ")
            continue

    if main_menu == "Play":
        break

    else:
        print("That's not a choice kid... ")
        main_menu = input("Kai and Owen Productions Presents: Punch-A-Looza!  Choices: Play/Credits/Tutorial ")
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

    else:
        print("That's not a choice kid... ")
        player_customization_screen = input("Welcome to the player customization screen, here you will make your own custom player that will progress through the story. Please refrain from using any personal information as we will not take any responsibility if your information gets leaked, thank you.  Choices: Continue ")
        continue

backstory_skip = input("Would you like to skip the backstory? Y/N ")
while True:
    if backstory_skip == "Y":
        break

    if backstory_skip == "N":
        backstory1 = input("As a child, you have always dreamed of boxing on the world stage. Every pivot of the foot, every swing of the arms, every movement you see on TV is calculated and is contributed to the finishing blow.  Choices: Continue ")
        if backstory1 == "Continue":
            backstory2 = input("Stars like Muhammad Ali and Mike Tyson seem to be so majestic in their movement. You feel like you are watching not a fight between humans, but a fight between gods. Through the TV screen, you can feel every punch, see every mistake, and hear the crowds cheers and jeers.  Choices: Continue ")

        else:
            print("That's not a choice kid... ")
            backstory1 = input("As a child, you have always dreamed of boxing on the world stage. Every pivot of the foot, every swing of the arms, every movement you see on TV is calculated and is contributed to the finishing blow.  Choices: Continue ")
                
            if backstory2 == "Continue":
                backstory3 = input("You want to be like them. You want to fight on the world stage. However, you know that it isn't possible for someone like you, so you end up only watching your favirote stars from behind the Tv screen.  Choices: Continue ")

            else:
                print("That's not a choice kid... ")
                backstory2 = input("Stars like Muhammad Ali and Mike Tyson seem to be so majestic in their movement. You feel like you are watching not a fight between humans, but a fight between gods. Through the TV screen, you can feel every punch, see every mistake, and hear the crowds cheers and jeers.  Choices: Continue ")
                    
                if backstory3 == "Continue":
                    backstory4 = input("Years go by, and you slowly lose sight of your dream. You used to have the motivation to puch a bag but you can't feel it anymore; the voice that used to tell you to beat anything that gets in your way.  Choices: Continue ")

                else:
                    print("That's not a choice kid... ")
                    backstory3 = input("You want to be like them. You want to fight on the world stage. However, you know that it isn't possible for someone like you, so you end up only watching your favirote stars from behind the Tv screen.  Choices: Continue ")
                        
                    if backstory4 == "Continue":
                        backstory5 = input("However, one day, you end up getting robbed by a street thug and you are unable to defend yourself. Frustrated at how weak you've become, the flame that used to burn in your heart was set ablaze again. On that day, you swore that you would never be defeated again. You swore that you would grow stronger, stronger then anyone you would ever fight, and thus, the future of the boxing world was born...  Choices: Continue ")
                    
                    else:
                        print("That's not a choice kid... ")
                        backstory4 = input("Years go by, and you slowly lose sight of your dream. You used to have the motivation to puch a bag but you can't feel it anymore; the voice that used to tell you to beat anything that gets in your way.  Choices: Continue ")
                            
                        if backstory5 == "Continue":
                            break

                        else:
                            print("That's not a choice kid... ")
                            backstory5 = input("However, one day, you end up getting robbed by a street thug and you are unable to defend yourself. Frustrated at how weak you've become, the flame that used to burn in your heart was set ablaze again. On that day, you swore that you would never be defeated again. You swore that you would grow stronger, stronger then anyone you would ever fight, and thus, the future of the boxing world was born...  Choices: Continue ")

    else:
        print("That's not a choice kid... ")
        continue