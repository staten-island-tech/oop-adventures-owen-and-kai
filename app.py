main_menu = input("Kai and Owen Productions Presents: Punch-A-Looza!  Choices: Play/Credits/Tutorial ")

while True:
    if main_menu == "Credits":
        credits = input("Main Developers: Kai and Owen Productions  Teacher: Mr. Whalen  Side Contributors: Yan Sharma  People we USED to copy from: Gabe Liberov and Yizhak Zoltan  Choices: Back ")
        if credits == 'Back':
            main_menu = input("Kai and Owen Productions Presents: Punch-A-Looza!  Choices: Play/Credits/Tutorial ")
            continue

        else:
            print("That's not a choice kid... ")
            continue
        
    if main_menu == "Tutorial":
        tutorial = input("The concept of this game is rather simple. You can use 6 different attacks that can be blocked with their corresponding blocks(e.g. Jabs will be blocked by the move Block Jab). You will be using these attacks and defenses in turns to avoid any exploits and spamming. Everytime you attack you will lose stamina which can be replenished by resting. However, resting will result in sacrificing your turn. That's really all there is to this game, so go out there and becoming the next boxing star of the world!  Choices: Back ")
        if tutorial == 'Back':
            main_menu = input("Kai and Owen Productions Presents: Punch-A-Looza!  Choices: Play/Credits/Tutorial ")
            continue

        else:
            print("That's not a choice kid... ")
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
        player_gender = input("What is your gender? M/F ")
        if player_gender == "M":
            player_pronouns = "He"
            break

        if player_gender == "F":
            player_pronouns = "She"
            break

        else:
            print("That's not a gender kid... ")
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
            continue
                
        if backstory2 == "Continue":
            backstory3 = input("You want to be like them. You want to fight on the world stage. However, you know that it isn't possible for someone like you, so you end up only watching your favirote stars from behind the Tv screen.  Choices: Continue ")

        else:
            print("That's not a choice kid... ")
            continue

        if backstory3 == "Continue":
            backstory4 = input("Years go by, and you slowly lose sight of your dream. You used to have the motivation to puch a bag but you can't feel it anymore; the voice that used to tell you to beat anything that gets in your way.  Choices: Continue ")

        else:
            print("That's not a choice kid... ")
            continue

        if backstory4 == "Continue":
            backstory5 = input("However, one day, you end up getting robbed by a street thug and you are unable to defend yourself. Frustrated at how weak you've become, the flame that used to burn in your heart was set ablaze again. On that day, you swore that you would never be defeated again. You swore that you would grow stronger, stronger then anyone you would ever fight, and thus, the future of the boxing world was born...  Choices: Continue ")

        else:
            print("That's not a choice kid... ")
            continue

        if backstory5 == "Continue":
            break

        else:
            print("That's not a choice kid... ")
            continue

    else:
        print("That's not a choice kid... ")
        continue

filler = input("A few years later...  Choices: Continue ")
while True:
    if filler == "Continue":
        scene1 = input("BOOM! BANG! POW! The sounds of fists colliding in the gym is almost like a melody. You're in your own corner, concentrating on your own bag.  Choices: Continue ")
        if scene1 == "Continue":
            scene1_pt2 = input("Jab. Straight to the body. Left feint. Left hook to the body followed by another one to the head. Endless amounts of combos are forming in your head, and you continue to beat the bag before you to a pulp.  Choices: Continue ")
            
        else:
            print("That's not a choice kid... ")
            continue

        if scene1_pt2 == "Continue":
            scene1_pt3 = input("If any outsider were to look at everyone inside the gym, they would easily see that you were much more talented then the rest. However, the gym coach is no such outsider. Shawn Wilson, in his mid 50s, used to do some boxing himself. If he were to stop being so naive and actually look at you for a split second he would be able to see that you easily outshone everyone in the gym.  Choices: Continue ")

        else:
            print("That's not a choice kid... ")
            continue

        if scene1_pt3 == "Continue":
            scene1_pt4 = input("Instead, he diverts his attention to someone else, someone that is nothing more than a pebble in your way to you: John Parksinson, the pride of the Wilson Boxing Gym.  Choices: Continue ")

        else:
            print("That's not a choice kid... ")
            continue

        if scene1_pt4 == "Continue":
            scene1_pt5 = input("As you continue to destroy your bag, you take glance at him from across the room. You see the coach firing him up as he fires some combos onto the bag. Two jabs followed by a striahgt and a hook. Easily one of the most basic combos in boxing and he manages to mess up on so many things. He forgets the pivot of his foot, the extending of his shoulders, and his form is terrible. The whole gym knows this, but no one can say anything as what makes him shine brighter than the rest of us, as the coach says, is his physique. 6 ft 1 weighing at 210 pounds of pure muscle, he was a tank to be reckoned with. Last person that ever fought him was sent to the hospital with multiple fractures all acrosss the body. After that, no one would even try to fight him in our area, so he's stuck with only punching a bag.  Choices: Continue ")
        
        else:
            print("That's not a choice kid... ")
            continue

        if scene1_pt5 == "Continue":
            scene1_pt6 = input("You shake your head and continue to punch the bag; you decide you shouldn't let your emotions get into your head. You had an actual goal to reach while that meathead had nothing. As your punching your bag you see a massive shadow consume all the light around you, and you look around to see, the man himself, John, towering over you with a vein bulging on his head.  Choices: Continue ")

        else:
            print("That's not a choice kid... ")
            continue

        if scene1_pt6 == "Continue":
            break

        else:
            print("That's not a choice kid... ")
            continue

    else:
        print("That's not a choice kid... ")
        continue

while True:
    if scene1_pt6 == "Continue":
        scene1_dialogue1 = input("John: wHat arE yOu lOokInG aT ya sQuAb?! wHy'd yoU LoOk At mE iN ThAt dIsGusTeD wAy?! WaNt mE to mEsS yoU uP?!  Choices: 1. I wasn't looking at you. / 2. What am I looking at? Of course it's that blob of a brain that you have! All that muscle's not going to help you in a fight if it belongs to that retard of a brain you have. ")

    if scene1_dialogue1 == "1":
        scene1_pt7 = input("")

    else:
        print("That's not a choice kid... ")
        continue