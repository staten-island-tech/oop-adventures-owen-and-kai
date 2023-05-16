import random
import time
from attacks import Jab, Straight, Left_Hook, Right_Hook, Right_Uppercut
from defense import Block_Forward, Block_Side, Block_Down
from resting import Relax_Muscles, Put_Guard_Down, Full_Body_Relaxation
from NPC import Tutorial_Boss, Round_1_Boss, Round_2_Boss, Round_3_Boss, Quarter_Finals_Boss, Semi_Finals_Boss, Final_Round_Boss, Glove_seller, Black_Market_Dealer, Coach, The_Miracle_Builder

stat_point = None
Attack = 1
Defend = 2
Rest = 3
Hit = 4
Miss = 5

player_dexterity_points = []
player_strength_points = []
player_stamina_points = []
player_technique_points = []

player_health = 500 + len(player_dexterity_points) * 10
player_strength = 10 + len(player_strength_points) * 1
player_stamina = 100 + len(player_stamina_points) * 5
player_technique = 5 + len(player_technique_points) * 1

tutorial_boss_enemy_actions = [Attack, Attack, Attack, Defend, Defend, Rest]
tutorial_boss_enemy_turn = random.choice(tutorial_boss_enemy_actions)

tutorial_boss_enemy_attack = [Jab, Straight, Left_Hook, Right_Hook, Right_Uppercut]
tutorial_boss_turn_attack = random.choice(tutorial_boss_enemy_attack)
print(tutorial_boss_enemy_turn)

tutorial_boss_enemy_spontaneous_strike = [Hit, Miss, Miss, Miss]
tutorial_boss_enemy_spontaneous_strike_chance = random.choice(tutorial_boss_enemy_spontaneous_strike)

player_spontaneous_strike = [Hit, Miss, Miss, Miss]
player_spontaneous_strike_chance = random.choice(tutorial_boss_enemy_spontaneous_strike)

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
        scene1_pt1 = input("BOOM! BANG! POW! The sounds of fists colliding in the gym is almost like a melody. You're in your own corner, concentrating on your own bag.  Choices: Continue ")
        
        if scene1_pt1 == "Continue":
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
            scene1_pt5 = input("As you continue to destroy your bag, you take a glance at him from across the room. You see the coach firing him up as he fires some combos onto the bag. Two jabs followed by a striahgt and a hook. Easily one of the most basic combos in boxing and he manages to mess up on so many things. He forgets the pivot of his foot, the extending of his shoulders, and his form is terrible. The whole gym knows this, but no one can say anything as what makes him shine brighter than the rest of us, as the coach says, is his physique. 6 ft 1 weighing at 210 pounds of pure muscle, he was a tank to be reckoned with. Last person that ever fought him was sent to the hospital with multiple fractures all acrosss the body. After that, no one would even try to fight him in our area, so he's stuck with only punching a bag.  Choices: Continue ")
        
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
        scene1_dialogue_choice1 = input("John: wHat arE yOu lOokInG aT ya sQuAb?! wHy'd yoU LoOk At mE iN ThAt dIsGusTeD wAy?! WaNt mE to mEsS yoU uP?!  Choices: 1. I wasn't looking at you. / 2. What am I looking at? Of course it's that blob of a brain that you have! All that muscle's not going to help you in a fight if it belongs to that retard of a brain you have. ")

    if scene1_dialogue_choice1 == "1":
        scene1_dialogue1 = input(f"{player_story_name}: I wasn't looking at you.  Choices: Continue ")

        if scene1_dialogue1 == "Continue":
            scene1_pt7 = input("You don't know why these words left your mouth; only a few seconds ago you were thinking you would be able to beat John easily. However, now that he was in front of you in person, you feel almost like a mere bug in front of the pressure of his presence.  Choices: Continue ")

        else:
            print("That's not a choice kid... ")
            continue

        if scene1_pt7 == "Continue":
            scene1_dialogue2 = input("John: oH YeS yOu WerE. NoW lEt mE BeAt yoU tO A PulP. I diDn'T lIkE yOu tHE DaY I SAw YoU.  Choices: Continue ")

        else:
            print("That's not a choice kid... ")
            continue

        if scene1_dialogue2 == "Continue":
            scene1_pt8 = input("John cranks back his hand and closes it into a fist into what seems to be a hook. It's slow, anyone could easily dodge it. However, somehow you're unable to move; the pressure being emitted from him is too strong.  Choices: Continue ")

        else:
            print("That's not a choice kid... ")
            continue

        if scene1_pt8 == "Continue":
            scene1_pt9 = input("You flinch and you mentally get ready for the pain that is about to come. However, Coach Wilson suddenly appears between the two of you and puts a hand on John's shoulder.  Choices: Continue ")

        else:
            print("That's not a choice kid... ")
            continue
        
        if scene1_pt9 == "Continue":
            scene1_dialogue3 = input("Coach Wilson: Alright now Johnny, we don't want to waste your punches on some weakling like him.  Choices: Continue ")

        else:
            print("That's not a choice kid... ")
            continue

        if scene1_dialogue3 == "Continue":
            scene1_dialogue4 = input("John: wElL, aT lEAsT leT mE BEat HiM uP iN thE RiNg!  Choices: Continue ")

        else:
            print("That's not a choice kid... ")
            continue 
        
        if scene1_dialogue4 == "Continue":
            scene1_dialogue5 = input("Coach Wilson: Well, if you insist on wrecking this piece of trash in front of everyone, I'll give you what you want.  Choices: Continue ")

        else:
            print("That's not a choice kid... ")
            continue

        if scene1_dialogue5 == "Continue":
            scene1_pt10 = input("Coach Wilson throws a pair of boxing gloves at your face which snaps you back to reality.  Choices: Continue ")

        else:
            print("That's not a choice kid... ")
            continue

        if scene1_pt10 == "Continue":
            scene1_dialogue6 = input(f"{player_story_name}: O-Okay...  Choices: Continue ")

        else:
            print("That's not a choice kid... ")
            continue
        
        if scene1_dialogue6 == "Continue":
            scene1_pt11 = input("This wasn't the type of fight you wanted. Sure, you always dreamed of fighting John in front of everyone; you were always so confident in yourself. However, now that you had fell under John's shadow, all the confidence you had just vaporized right on the spot. You don't know what to do. You want to just melt away at the spot. But now isn't the time to be panicking. You had a fight on your hands, and if you were to redeem yourself in front of everyone you would have to win this fight.  Choices: Continue ")

        else:
            print("That's not a choice kid... ")
            continue

        if scene1_pt11 == "Continue":
            print("You start to enter the ring... ")
            break

    if scene1_dialogue_choice1 == "2":
        scene1_dialogue1 = input(f"{player_story_name}: What am I looking at? Of course it's that blob of a brain that you have! All that muscle's not going to help you in a fight if it belongs to that retard of a brain you have.  Choices: Continue ")

        if scene1_dialogue1 == "Continue":
            scene1_pt7 = input("You don't know why these words left your mouth, but it felt good. Everyone is looking at you in shock and you feel power rushing through your veins as adrenaline rushes through your entire body. However, John is visibly fuming as the vein in his head looked like it was about to burst.  Choices: Continue ")

        else:
            print("That's not a choice kid... ")
            continue

        if scene1_pt7 == "Continue":
            scene1_dialogue2 = input("John: HoW dARe yOU SaY tHaT tO mE!  Choices: Continue ")

        else:
            print("That's not a choice kid... ")
            continue

        if scene1_dialogue2 == "Continue":
            scene1_pt8 = input("Before you can react John tucks in his hand and hits you with a uppercut straight to the chin. You are knocked straight off your feet; his punch felt like a hammer knocking you from between the world of the living and the dead. You are on the ground, but to everyones surprise, you spit out two of your teeth and, instead of crumbling in fear, you laugh and look him staight in the eyes.  Choices: Continue ")

        else:
            print("That's not a choice kid... ")
            continue

        if scene1_pt8 == "Continue":
            scene1_pt9 = input("At first, John is shocked. However, that shock soon turns into anger as his face turns a very visible red and he charges at you to give you a few more blows. As you are about to get up and start fighting John right then and there, Coach Wilson suddenly rushes behind John and holds him back.  Choices: Continue ")

        else:
            print("That's not a choice kid... ")
            continue

        if scene1_pt9 == "Continue":
            scene1_dialogue3 = input("Coach Wilson: Woah there, Johnny boy, cooldown, don't let this kid here provoke you. We don't want any trouble.  Choices: Continue ")

        else:
            print("That's not a choice kid... ")
            continue

        if scene1_dialogue3 == "Continue":
            scene1_dialogue4 = input("John: ThEn aT lEAsT lEt Me beAT hIM iN tHe rInG!  Choices: Continue ")

        else:
            print("That's not a choice kid... ")
            continue

        if scene1_dialogue4 == "Continue":
            scene1_dialogue5 = input(f"Coach Wilson: Alright, alright, {player_story_name}, get your gloves on and get in the ring, your fighting.  Choices: Continue ")

        else:
            print("That's not a choice kid... ")
            continue

        if scene1_dialogue5 == "Continue":
            scene1_dialogue6 = input(f"{player_story_name}: Whatever you say coach. I've been waiting for this moment for some time.  Choices: Continue ")

        else:
            print("That's not a choice kid... ")
            continue

        if scene1_dialogue6 == "Continue":
            scene1_pt10 = input("This is it, the chance you've been waiting for, the chance to be able to prove yourself in front of everyone in the gym. Although your mouth is starting to throb from the punch you received from John, your heart is filled with all sorts of feelings ranging from excitment to anger. However, you put on your gloves and step into the ring; this could be the life changing moment that you've always needed...  Choices: Continue ")

        else:
            print("That's not a choice kid... ")
            continue

        if scene1_pt10 == "Continue":
            print("You start to enter the ring... ")
            time.sleep(1)
            break

        else:
            print("That's not a choice kid... ")
            continue        

    else:
        print("That's not a choice kid... ")
        continue

while True:
    print("Refree: Okay gentlemen, you should know the rules by know, protect yourself at all times, and attack at any chance you got. I don't wanna see anything dirty. ")
    ready = input("Are you ready? Choices: Y/N ")
    if ready == "Y":
        print("Ready. Set. BOX! ")
        while player_health and Tutorial_Boss.health != 0:
            player_turn = input("What do you want to do?  Choices: Attack/Defend/Rest ")
            if player_turn == "Attack":
                attack_move = input("What kind of attack do you want to use?  Choices: Jab/Straight/Left Hook/Right Hook/Right Uppercut ")
                if attack_move == "Jab":
                    if player_stamina >= 10:
                        player_stamina -= 10
                        print(f"{player_story_name} goes for a beautiful jab! ")
                        tutorial_boss_turn = random.choice(tutorial_boss_enemy_actions)
                        time.sleep(1)
                        if tutorial_boss_turn != Defend:
                            print(f"And it penetrates straight through {Tutorial_Boss.name}'s defense! ")
                            Tutorial_Boss.health -= Jab.damage  
                            continue               

                        if tutorial_boss_turn == Defend:
                            print(f"But {player_story_name}'s punch was skillfully evaded by an excellent block from {Tutorial_Boss.name}! ")
                            Tutorial_Boss.health = Tutorial_Boss.health
                            continue

                        if tutorial_boss_turn == Attack:
                            if tutorial_boss_turn_attack == Jab:
                                if Tutorial_Boss.stamina >= 10:
                                    Tutorial_Boss.stamina -= 10
                                    print(f"And {Tutorial_Boss.name} tries for a jab! ")
                                    time.sleep(1)
                                    if tutorial_boss_enemy_spontaneous_strike_chance and player_spontaneous_strike_chance == Hit:
                                        print(f"And we have a amazing spectalce! Both {player_story_name} and {Tutorial_Boss.name} hit each other at the same time! ")
                                        continue

                                    if tutorial_boss_enemy_spontaneous_strike_chance == Hit and player_spontaneous_strike_chance == Miss:
                                        print(f"Oh! What a spectacle! Both competitiors crash into each other but {Tutorial_Boss.name}'s punch collides and {player_story_name}'s only misses by a large margain!")
                                        continue

                                    if tutorial_boss_enemy_spontaneous_strike_chance == Miss and player_spontaneous_strike_chance == Hit:
                                        print(f"Oh! What do we have here?! {player_story_name} and {Tutorial_Boss.name} have swung at each other at the same time! However, {player_story_name}'s punch collides hard with {Tutorial_Boss.name}'s face and {Tutorial_Boss.name} only misses his face by a few inches! ")      
                                        continue

                                    if tutorial_boss_enemy_spontaneous_strike_chance and player_spontaneous_strike_chance == Miss:
                                        print(f"Oh what a spectacle! Both {player_story_name} and {Tutorial_Boss.name} strike at each other with an enormous amount of force but they both miss! This is sure one hell of a fight! ")
                                        continue

                                if Tutorial_Boss.stamina < 10:
                                    print(f"{Tutorial_Boss.name} has started to take a short break and let his guard down! ")
                                    Tutorial_Boss.stamina + 20
                                    continue

                            if tutorial_boss_turn_attack == Straight:
                                if Tutorial_Boss.stamina >= 30:
                                    Tutorial_Boss.stamina -= 30
                                    print(f"And {Tutorial_Boss.name} tries for a straight! ")
                                    time.sleep(1)
                                    if tutorial_boss_enemy_spontaneous_strike_chance and player_spontaneous_strike_chance == Hit:
                                        print(f"And we have a amazing spectalce! Both {player_story_name} and {Tutorial_Boss.name} hit each other at the same time! ")
                                        continue

                                    if tutorial_boss_enemy_spontaneous_strike_chance == Hit and player_spontaneous_strike_chance == Miss:
                                        print(f"Oh! What a spectacle! Both competitiors crash into each other but {Tutorial_Boss.name}'s punch collides and {player_story_name}'s only misses by a large margain!")
                                        continue

                                    if tutorial_boss_enemy_spontaneous_strike_chance == Miss and player_spontaneous_strike_chance == Hit:
                                        print(f"Oh! What do we have here?! {player_story_name} and {Tutorial_Boss.name} have swung at each other at the same time! However, {player_story_name}'s punch collides hard with {Tutorial_Boss.name}'s face and {Tutorial_Boss.name} only misses his face by a few inches! ")      
                                        continue

                                    if tutorial_boss_enemy_spontaneous_strike_chance and player_spontaneous_strike_chance == Miss:
                                        print(f"Oh what a spectacle! Both {player_story_name} and {Tutorial_Boss.name} strike at each other with an enormous amount of force but they both miss! This is sure one hell of a fight! ")
                                        continue

                                if Tutorial_Boss.stamina < 30:
                                    print(f"{Tutorial_Boss.name} has started to take a short break and let his guard down! ")
                                    Tutorial_Boss.stamina + 20
                                    continue

                            if tutorial_boss_turn_attack == Left_Hook:
                                if Tutorial_Boss.stamina >= 15:
                                    Tutorial_Boss.stamina -= 15
                                    print(f"And {Tutorial_Boss.name} tries for a left hook! ")
                                    time.sleep(1)
                                    if tutorial_boss_enemy_spontaneous_strike_chance and player_spontaneous_strike_chance == Hit:
                                        print(f"And we have a amazing spectalce! Both {player_story_name} and {Tutorial_Boss.name} hit each other at the same time! ")
                                        continue

                                    if tutorial_boss_enemy_spontaneous_strike_chance == Hit and player_spontaneous_strike_chance == Miss:
                                        print(f"Oh! What a spectacle! Both competitiors crash into each other but {Tutorial_Boss.name}'s punch collides and {player_story_name}'s only misses by a large margain!")
                                        continue

                                    if tutorial_boss_enemy_spontaneous_strike_chance == Miss and player_spontaneous_strike_chance == Hit:
                                        print(f"Oh! What do we have here?! {player_story_name} and {Tutorial_Boss.name} have swung at each other at the same time! However, {player_story_name}'s punch collides hard with {Tutorial_Boss.name}'s face and {Tutorial_Boss.name} only misses his face by a few inches! ")      
                                        continue

                                    if tutorial_boss_enemy_spontaneous_strike_chance and player_spontaneous_strike_chance == Miss:
                                        print(f"Oh what a spectacle! Both {player_story_name} and {Tutorial_Boss.name} strike at each other with an enormous amount of force but they both miss! This is sure one hell of a fight! ")
                                        continue

                            if tutorial_boss_turn_attack == Right_Hook:
                                if Tutorial_Boss.stamina >= 45:
                                    Tutorial_Boss.stamina -= 45
                                    print(f"And {Tutorial_Boss.name} tries for a right hook! ")
                                    time.sleep(1)
                                    if tutorial_boss_enemy_spontaneous_strike_chance and player_spontaneous_strike_chance == Hit:
                                        print(f"And we have a amazing spectalce! Both {player_story_name} and {Tutorial_Boss.name} hit each other at the same time! ")
                                        continue

                                    if tutorial_boss_enemy_spontaneous_strike_chance == Hit and player_spontaneous_strike_chance == Miss:
                                        print(f"Oh! What a spectacle! Both competitiors crash into each other but {Tutorial_Boss.name}'s punch collides and {player_story_name}'s only misses by a large margain!")
                                        continue

                                    if tutorial_boss_enemy_spontaneous_strike_chance == Miss and player_spontaneous_strike_chance == Hit:
                                        print(f"Oh! What do we have here?! {player_story_name} and {Tutorial_Boss.name} have swung at each other at the same time! However, {player_story_name}'s punch collides hard with {Tutorial_Boss.name}'s face and {Tutorial_Boss.name} only misses his face by a few inches! ")      
                                        continue

                                    if tutorial_boss_enemy_spontaneous_strike_chance and player_spontaneous_strike_chance == Miss:
                                        print(f"Oh what a spectacle! Both {player_story_name} and {Tutorial_Boss.name} strike at each other with an enormous amount of force but they both miss! This is sure one hell of a fight! ")
                                        continue

                                if Tutorial_Boss.stamina < 45:
                                    print(f"{Tutorial_Boss.name} has started to take a short break and let his guard down! ")
                                    Tutorial_Boss.stamina + 20
                                    continue                                    

                            if tutorial_boss_turn_attack == Right_Uppercut:
                                if Tutorial_Boss.stamina >= 60:
                                    Tutorial_Boss.stamina -= 60
                                    print(f"And {Tutorial_Boss.name} tries for a right uppercut! ")
                                    time.sleep(1)
                                    if tutorial_boss_enemy_spontaneous_strike_chance and player_spontaneous_strike_chance == Hit:
                                        print(f"And we have a amazing spectalce! Both {player_story_name} and {Tutorial_Boss.name} hit each other at the same time! ")
                                        continue

                                    if tutorial_boss_enemy_spontaneous_strike_chance == Hit and player_spontaneous_strike_chance == Miss:
                                        print(f"Oh! What a spectacle! Both competitiors crash into each other but {Tutorial_Boss.name}'s punch collides and {player_story_name}'s only misses by a large margain!")
                                        continue

                                    if tutorial_boss_enemy_spontaneous_strike_chance == Miss and player_spontaneous_strike_chance == Hit:
                                        print(f"Oh! What do we have here?! {player_story_name} and {Tutorial_Boss.name} have swung at each other at the same time! However, {player_story_name}'s punch collides hard with {Tutorial_Boss.name}'s face and {Tutorial_Boss.name} only misses his face by a few inches! ")      
                                        continue

                                    if tutorial_boss_enemy_spontaneous_strike_chance and player_spontaneous_strike_chance == Miss:
                                        print(f"Oh what a spectacle! Both {player_story_name} and {Tutorial_Boss.name} strike at each other with an enormous amount of force but they both miss! This is sure one hell of a fight! ")
                                        continue

                                if Tutorial_Boss.stamina < 60:
                                    print(f"{Tutorial_Boss.name} has started to take a short break and let his guard down! ")
                                    Tutorial_Boss.stamina + 20
                                    continue

                    if player_stamina < 10:
                        print("Sorry, you do not have enough stamina to perform this attack. ")
                        continue

                if attack_move == "Straight":
                    if player_stamina >= 30:
                        player_stamina -= 30
                        print(f"{player_story_name} goes for a beautiful straight! ")
                        tutorial_boss_turn = random.choice(tutorial_boss_enemy_actions)                       
                        time.sleep(1)
                        if tutorial_boss_turn != Defend:
                            print(f"And it penetrates straight through {Tutorial_Boss.name}'s defense! ")
                            Tutorial_Boss.health -= Straight.damage
                            continue

                        if tutorial_boss_turn == Defend:
                            print(f"But {player_story_name}'s punch was skillfully evaded by an excellent block from {Tutorial_Boss.name}! ")
                            Tutorial_Boss.health = Tutorial_Boss.health
                            continue

                        if tutorial_boss_turn == Attack:
                            if tutorial_boss_turn_attack == Jab:
                                if Tutorial_Boss.stamina >= 10:
                                    Tutorial_Boss.stamina -= 10
                                    print(f"And {Tutorial_Boss.name} tries for a jab! ")
                                    time.sleep(1)
                                    if tutorial_boss_enemy_spontaneous_strike_chance and player_spontaneous_strike_chance == Hit:
                                        print(f"And we have a amazing spectalce! Both {player_story_name} and {Tutorial_Boss.name} hit each other at the same time! ")
                                        continue

                                    if tutorial_boss_enemy_spontaneous_strike_chance == Hit and player_spontaneous_strike_chance == Miss:
                                        print(f"Oh! What a spectacle! Both competitiors crash into each other but {Tutorial_Boss.name}'s punch collides and {player_story_name}'s only misses by a large margain!")
                                        continue

                                    if tutorial_boss_enemy_spontaneous_strike_chance == Miss and player_spontaneous_strike_chance == Hit:
                                        print(f"Oh! What do we have here?! {player_story_name} and {Tutorial_Boss.name} have swung at each other at the same time! However, {player_story_name}'s punch collides hard with {Tutorial_Boss.name}'s face and {Tutorial_Boss.name} only misses his face by a few inches! ")      
                                        continue

                                    if tutorial_boss_enemy_spontaneous_strike_chance and player_spontaneous_strike_chance == Miss:
                                        print(f"Oh what a spectacle! Both {player_story_name} and {Tutorial_Boss.name} strike at each other with an enormous amount of force but they both miss! This is sure one hell of a fight! ")
                                        continue

                                if Tutorial_Boss.stamina < 10:
                                    print(f"{Tutorial_Boss.name} has started to take a short break and let his guard down! ")
                                    Tutorial_Boss.stamina + 20
                                    continue

                            if tutorial_boss_turn_attack == Straight:
                                if Tutorial_Boss.stamina >= 30:
                                    Tutorial_Boss.stamina -= 30
                                    print(f"And {Tutorial_Boss.name} tries for a straight! ")
                                    time.sleep(1)
                                    if tutorial_boss_enemy_spontaneous_strike_chance and player_spontaneous_strike_chance == Hit:
                                        print(f"And we have a amazing spectalce! Both {player_story_name} and {Tutorial_Boss.name} hit each other at the same time! ")
                                        continue

                                    if tutorial_boss_enemy_spontaneous_strike_chance == Hit and player_spontaneous_strike_chance == Miss:
                                        print(f"Oh! What a spectacle! Both competitiors crash into each other but {Tutorial_Boss.name}'s punch collides and {player_story_name}'s only misses by a large margain!")
                                        continue

                                    if tutorial_boss_enemy_spontaneous_strike_chance == Miss and player_spontaneous_strike_chance == Hit:
                                        print(f"Oh! What do we have here?! {player_story_name} and {Tutorial_Boss.name} have swung at each other at the same time! However, {player_story_name}'s punch collides hard with {Tutorial_Boss.name}'s face and {Tutorial_Boss.name} only misses his face by a few inches! ")      
                                        continue

                                    if tutorial_boss_enemy_spontaneous_strike_chance and player_spontaneous_strike_chance == Miss:
                                        print(f"Oh what a spectacle! Both {player_story_name} and {Tutorial_Boss.name} strike at each other with an enormous amount of force but they both miss! This is sure one hell of a fight! ")
                                        continue

                                if Tutorial_Boss.stamina < 30:
                                    print(f"{Tutorial_Boss.name} has started to take a short break and let his guard down! ")
                                    Tutorial_Boss.stamina + 20
                                    continue

                            if tutorial_boss_turn_attack == Left_Hook:
                                if Tutorial_Boss.stamina >= 15:
                                    Tutorial_Boss.stamina -= 15
                                    print(f"And {Tutorial_Boss.name} tries for a left hook! ")
                                    time.sleep(1)
                                    if tutorial_boss_enemy_spontaneous_strike_chance and player_spontaneous_strike_chance == Hit:
                                        print(f"And we have a amazing spectalce! Both {player_story_name} and {Tutorial_Boss.name} hit each other at the same time! ")
                                        continue

                                    if tutorial_boss_enemy_spontaneous_strike_chance == Hit and player_spontaneous_strike_chance == Miss:
                                        print(f"Oh! What a spectacle! Both competitiors crash into each other but {Tutorial_Boss.name}'s punch collides and {player_story_name}'s only misses by a large margain!")
                                        continue

                                    if tutorial_boss_enemy_spontaneous_strike_chance == Miss and player_spontaneous_strike_chance == Hit:
                                        print(f"Oh! What do we have here?! {player_story_name} and {Tutorial_Boss.name} have swung at each other at the same time! However, {player_story_name}'s punch collides hard with {Tutorial_Boss.name}'s face and {Tutorial_Boss.name} only misses his face by a few inches! ")      
                                        continue

                                    if tutorial_boss_enemy_spontaneous_strike_chance and player_spontaneous_strike_chance == Miss:
                                        print(f"Oh what a spectacle! Both {player_story_name} and {Tutorial_Boss.name} strike at each other with an enormous amount of force but they both miss! This is sure one hell of a fight! ")
                                        continue

                            if tutorial_boss_turn_attack == Right_Hook:
                                if Tutorial_Boss.stamina >= 45:
                                    Tutorial_Boss.stamina -= 45
                                    print(f"And {Tutorial_Boss.name} tries for a right hook! ")
                                    time.sleep(1)
                                    if tutorial_boss_enemy_spontaneous_strike_chance and player_spontaneous_strike_chance == Hit:
                                        print(f"And we have a amazing spectalce! Both {player_story_name} and {Tutorial_Boss.name} hit each other at the same time! ")
                                        continue

                                    if tutorial_boss_enemy_spontaneous_strike_chance == Hit and player_spontaneous_strike_chance == Miss:
                                        print(f"Oh! What a spectacle! Both competitiors crash into each other but {Tutorial_Boss.name}'s punch collides and {player_story_name}'s only misses by a large margain!")
                                        continue

                                    if tutorial_boss_enemy_spontaneous_strike_chance == Miss and player_spontaneous_strike_chance == Hit:
                                        print(f"Oh! What do we have here?! {player_story_name} and {Tutorial_Boss.name} have swung at each other at the same time! However, {player_story_name}'s punch collides hard with {Tutorial_Boss.name}'s face and {Tutorial_Boss.name} only misses his face by a few inches! ")      
                                        continue

                                    if tutorial_boss_enemy_spontaneous_strike_chance and player_spontaneous_strike_chance == Miss:
                                        print(f"Oh what a spectacle! Both {player_story_name} and {Tutorial_Boss.name} strike at each other with an enormous amount of force but they both miss! This is sure one hell of a fight! ")
                                        continue

                                if Tutorial_Boss.stamina < 45:
                                    print(f"{Tutorial_Boss.name} has started to take a short break and let his guard down! ")
                                    Tutorial_Boss.stamina + 20
                                    continue                                    

                            if tutorial_boss_turn_attack == Right_Uppercut:
                                if Tutorial_Boss.stamina >= 60:
                                    Tutorial_Boss.stamina -= 60
                                    print(f"And {Tutorial_Boss.name} tries for a right uppercut! ")
                                    time.sleep(1)
                                    if tutorial_boss_enemy_spontaneous_strike_chance and player_spontaneous_strike_chance == Hit:
                                        print(f"And we have a amazing spectalce! Both {player_story_name} and {Tutorial_Boss.name} hit each other at the same time! ")
                                        continue

                                    if tutorial_boss_enemy_spontaneous_strike_chance == Hit and player_spontaneous_strike_chance == Miss:
                                        print(f"Oh! What a spectacle! Both competitiors crash into each other but {Tutorial_Boss.name}'s punch collides and {player_story_name}'s only misses by a large margain!")
                                        continue

                                    if tutorial_boss_enemy_spontaneous_strike_chance == Miss and player_spontaneous_strike_chance == Hit:
                                        print(f"Oh! What do we have here?! {player_story_name} and {Tutorial_Boss.name} have swung at each other at the same time! However, {player_story_name}'s punch collides hard with {Tutorial_Boss.name}'s face and {Tutorial_Boss.name} only misses his face by a few inches! ")      
                                        continue

                                    if tutorial_boss_enemy_spontaneous_strike_chance and player_spontaneous_strike_chance == Miss:
                                        print(f"Oh what a spectacle! Both {player_story_name} and {Tutorial_Boss.name} strike at each other with an enormous amount of force but they both miss! This is sure one hell of a fight! ")
                                        continue

                                if Tutorial_Boss.stamina < 60:
                                    print(f"{Tutorial_Boss.name} has started to take a short break and let his guard down! ")
                                    Tutorial_Boss.stamina + 20
                                    continue
                
                    if player_stamina < 30:
                        print("Sorry, you do not have enough stamina to perform this attack. ")
                        continue               
                                                  
                if attack_move == "Left Hook":
                    if player_stamina >= 15:
                        player_stamina -= 15
                        print(f"{player_story_name} goes for a beautiful left hook! ")
                        tutorial_boss_turn = random.choice(tutorial_boss_enemy_actions)
                        time.sleep(1)
                        if tutorial_boss_turn != Defend:
                            print(f"And it penetrates straight through {Tutorial_Boss.name}'s defense! ")                       
                            Tutorial_Boss.health -= Left_Hook.damage

                        if tutorial_boss_turn == Defend:
                            print(f"But {player_story_name}'s punch was skillfully evaded by an excellent block from {Tutorial_Boss.name}! ")
                            Tutorial_Boss.health = Tutorial_Boss.health
                            continue

                        if tutorial_boss_turn == Attack:
                            if tutorial_boss_turn_attack == Jab:
                                if Tutorial_Boss.stamina >= 10:
                                    Tutorial_Boss.stamina -= 10
                                    print(f"And {Tutorial_Boss.name} tries for a jab! ")
                                    time.sleep(1)
                                    if tutorial_boss_enemy_spontaneous_strike_chance and player_spontaneous_strike_chance == Hit:
                                        print(f"And we have a amazing spectalce! Both {player_story_name} and {Tutorial_Boss.name} hit each other at the same time! ")
                                        continue

                                    if tutorial_boss_enemy_spontaneous_strike_chance == Hit and player_spontaneous_strike_chance == Miss:
                                        print(f"Oh! What a spectacle! Both competitiors crash into each other but {Tutorial_Boss.name}'s punch collides and {player_story_name}'s only misses by a large margain!")
                                        continue

                                    if tutorial_boss_enemy_spontaneous_strike_chance == Miss and player_spontaneous_strike_chance == Hit:
                                        print(f"Oh! What do we have here?! {player_story_name} and {Tutorial_Boss.name} have swung at each other at the same time! However, {player_story_name}'s punch collides hard with {Tutorial_Boss.name}'s face and {Tutorial_Boss.name} only misses his face by a few inches! ")      
                                        continue

                                    if tutorial_boss_enemy_spontaneous_strike_chance and player_spontaneous_strike_chance == Miss:
                                        print(f"Oh what a spectacle! Both {player_story_name} and {Tutorial_Boss.name} strike at each other with an enormous amount of force but they both miss! This is sure one hell of a fight! ")
                                        continue

                                if Tutorial_Boss.stamina < 10:
                                    print(f"{Tutorial_Boss.name} has started to take a short break and let his guard down! ")
                                    Tutorial_Boss.stamina + 20
                                    continue

                            if tutorial_boss_turn_attack == Straight:
                                if Tutorial_Boss.stamina >= 30:
                                    Tutorial_Boss.stamina -= 30
                                    print(f"And {Tutorial_Boss.name} tries for a straight! ")
                                    time.sleep(1)
                                    if tutorial_boss_enemy_spontaneous_strike_chance and player_spontaneous_strike_chance == Hit:
                                        print(f"And we have a amazing spectalce! Both {player_story_name} and {Tutorial_Boss.name} hit each other at the same time! ")
                                        continue

                                    if tutorial_boss_enemy_spontaneous_strike_chance == Hit and player_spontaneous_strike_chance == Miss:
                                        print(f"Oh! What a spectacle! Both competitiors crash into each other but {Tutorial_Boss.name}'s punch collides and {player_story_name}'s only misses by a large margain!")
                                        continue

                                    if tutorial_boss_enemy_spontaneous_strike_chance == Miss and player_spontaneous_strike_chance == Hit:
                                        print(f"Oh! What do we have here?! {player_story_name} and {Tutorial_Boss.name} have swung at each other at the same time! However, {player_story_name}'s punch collides hard with {Tutorial_Boss.name}'s face and {Tutorial_Boss.name} only misses his face by a few inches! ")      
                                        continue

                                    if tutorial_boss_enemy_spontaneous_strike_chance and player_spontaneous_strike_chance == Miss:
                                        print(f"Oh what a spectacle! Both {player_story_name} and {Tutorial_Boss.name} strike at each other with an enormous amount of force but they both miss! This is sure one hell of a fight! ")
                                        continue

                                if Tutorial_Boss.stamina < 30:
                                    print(f"{Tutorial_Boss.name} has started to take a short break and let his guard down! ")
                                    Tutorial_Boss.stamina + 20
                                    continue

                            if tutorial_boss_turn_attack == Left_Hook:
                                if Tutorial_Boss.stamina >= 15:
                                    Tutorial_Boss.stamina -= 15
                                    print(f"And {Tutorial_Boss.name} tries for a left hook! ")
                                    time.sleep(1)
                                    if tutorial_boss_enemy_spontaneous_strike_chance and player_spontaneous_strike_chance == Hit:
                                        print(f"And we have a amazing spectalce! Both {player_story_name} and {Tutorial_Boss.name} hit each other at the same time! ")
                                        continue

                                    if tutorial_boss_enemy_spontaneous_strike_chance == Hit and player_spontaneous_strike_chance == Miss:
                                        print(f"Oh! What a spectacle! Both competitiors crash into each other but {Tutorial_Boss.name}'s punch collides and {player_story_name}'s only misses by a large margain!")
                                        continue

                                    if tutorial_boss_enemy_spontaneous_strike_chance == Miss and player_spontaneous_strike_chance == Hit:
                                        print(f"Oh! What do we have here?! {player_story_name} and {Tutorial_Boss.name} have swung at each other at the same time! However, {player_story_name}'s punch collides hard with {Tutorial_Boss.name}'s face and {Tutorial_Boss.name} only misses his face by a few inches! ")      
                                        continue

                                    if tutorial_boss_enemy_spontaneous_strike_chance and player_spontaneous_strike_chance == Miss:
                                        print(f"Oh what a spectacle! Both {player_story_name} and {Tutorial_Boss.name} strike at each other with an enormous amount of force but they both miss! This is sure one hell of a fight! ")
                                        continue

                            if tutorial_boss_turn_attack == Right_Hook:
                                if Tutorial_Boss.stamina >= 45:
                                    Tutorial_Boss.stamina -= 45
                                    print(f"And {Tutorial_Boss.name} tries for a right hook! ")
                                    time.sleep(1)
                                    if tutorial_boss_enemy_spontaneous_strike_chance and player_spontaneous_strike_chance == Hit:
                                        print(f"And we have a amazing spectalce! Both {player_story_name} and {Tutorial_Boss.name} hit each other at the same time! ")
                                        continue

                                    if tutorial_boss_enemy_spontaneous_strike_chance == Hit and player_spontaneous_strike_chance == Miss:
                                        print(f"Oh! What a spectacle! Both competitiors crash into each other but {Tutorial_Boss.name}'s punch collides and {player_story_name}'s only misses by a large margain!")
                                        continue

                                    if tutorial_boss_enemy_spontaneous_strike_chance == Miss and player_spontaneous_strike_chance == Hit:
                                        print(f"Oh! What do we have here?! {player_story_name} and {Tutorial_Boss.name} have swung at each other at the same time! However, {player_story_name}'s punch collides hard with {Tutorial_Boss.name}'s face and {Tutorial_Boss.name} only misses his face by a few inches! ")      
                                        continue

                                    if tutorial_boss_enemy_spontaneous_strike_chance and player_spontaneous_strike_chance == Miss:
                                        print(f"Oh what a spectacle! Both {player_story_name} and {Tutorial_Boss.name} strike at each other with an enormous amount of force but they both miss! This is sure one hell of a fight! ")
                                        continue

                                if Tutorial_Boss.stamina < 45:
                                    print(f"{Tutorial_Boss.name} has started to take a short break and let his guard down! ")
                                    Tutorial_Boss.stamina + 20
                                    continue                                    

                            if tutorial_boss_turn_attack == Right_Uppercut:
                                if Tutorial_Boss.stamina >= 60:
                                    Tutorial_Boss.stamina -= 60
                                    print(f"And {Tutorial_Boss.name} tries for a right uppercut! ")
                                    time.sleep(1)
                                    if tutorial_boss_enemy_spontaneous_strike_chance and player_spontaneous_strike_chance == Hit:
                                        print(f"And we have a amazing spectalce! Both {player_story_name} and {Tutorial_Boss.name} hit each other at the same time! ")
                                        continue

                                    if tutorial_boss_enemy_spontaneous_strike_chance == Hit and player_spontaneous_strike_chance == Miss:
                                        print(f"Oh! What a spectacle! Both competitiors crash into each other but {Tutorial_Boss.name}'s punch collides and {player_story_name}'s only misses by a large margain!")
                                        continue

                                    if tutorial_boss_enemy_spontaneous_strike_chance == Miss and player_spontaneous_strike_chance == Hit:
                                        print(f"Oh! What do we have here?! {player_story_name} and {Tutorial_Boss.name} have swung at each other at the same time! However, {player_story_name}'s punch collides hard with {Tutorial_Boss.name}'s face and {Tutorial_Boss.name} only misses his face by a few inches! ")      
                                        continue

                                    if tutorial_boss_enemy_spontaneous_strike_chance and player_spontaneous_strike_chance == Miss:
                                        print(f"Oh what a spectacle! Both {player_story_name} and {Tutorial_Boss.name} strike at each other with an enormous amount of force but they both miss! This is sure one hell of a fight! ")
                                        continue

                                if Tutorial_Boss.stamina < 60:
                                    print(f"{Tutorial_Boss.name} has started to take a short break and let his guard down! ")
                                    Tutorial_Boss.stamina + 20
                                    continue

                    if player_stamina < 15:
                        print("Sorry, you do not have enough stamina to perform this attack. ")
                        continue      

                if attack_move == "Right Hook":
                    if player_stamina >= 45:
                        player_stamina -= 45
                        print(f"{player_story_name} goes for a beautiful right hook! ")
                        tutorial_boss_turn = random.choice(tutorial_boss_enemy_actions)
                        time.sleep(1)
                        if tutorial_boss_turn != Defend:
                            print(f"And it penetrates straight through {Tutorial_Boss.name}'s defense! ")                       
                            Tutorial_Boss.health -= Right_Hook.damage

                        if tutorial_boss_turn == Defend:
                            print(f"But {player_story_name}'s punch was skillfully evaded by an excellent block from {Tutorial_Boss.name}! ")
                            Tutorial_Boss.health = Tutorial_Boss.health
                            continue

                        if tutorial_boss_turn == Attack:
                            if tutorial_boss_turn_attack == Jab:
                                if Tutorial_Boss.stamina >= 10:
                                    Tutorial_Boss.stamina -= 10
                                    print(f"And {Tutorial_Boss.name} tries for a jab! ")
                                    time.sleep(1)
                                    if tutorial_boss_enemy_spontaneous_strike_chance and player_spontaneous_strike_chance == Hit:
                                        print(f"And we have a amazing spectalce! Both {player_story_name} and {Tutorial_Boss.name} hit each other at the same time! ")
                                        continue

                                    if tutorial_boss_enemy_spontaneous_strike_chance == Hit and player_spontaneous_strike_chance == Miss:
                                        print(f"Oh! What a spectacle! Both competitiors crash into each other but {Tutorial_Boss.name}'s punch collides and {player_story_name}'s only misses by a large margain!")
                                        continue

                                    if tutorial_boss_enemy_spontaneous_strike_chance == Miss and player_spontaneous_strike_chance == Hit:
                                        print(f"Oh! What do we have here?! {player_story_name} and {Tutorial_Boss.name} have swung at each other at the same time! However, {player_story_name}'s punch collides hard with {Tutorial_Boss.name}'s face and {Tutorial_Boss.name} only misses his face by a few inches! ")      
                                        continue

                                    if tutorial_boss_enemy_spontaneous_strike_chance and player_spontaneous_strike_chance == Miss:
                                        print(f"Oh what a spectacle! Both {player_story_name} and {Tutorial_Boss.name} strike at each other with an enormous amount of force but they both miss! This is sure one hell of a fight! ")
                                        continue

                                if Tutorial_Boss.stamina < 10:
                                    print(f"{Tutorial_Boss.name} has started to take a short break and let his guard down! ")
                                    Tutorial_Boss.stamina + 20
                                    continue

                            if tutorial_boss_turn_attack == Straight:
                                if Tutorial_Boss.stamina >= 30:
                                    Tutorial_Boss.stamina -= 30
                                    print(f"And {Tutorial_Boss.name} tries for a straight! ")
                                    time.sleep(1)
                                    if tutorial_boss_enemy_spontaneous_strike_chance and player_spontaneous_strike_chance == Hit:
                                        print(f"And we have a amazing spectalce! Both {player_story_name} and {Tutorial_Boss.name} hit each other at the same time! ")
                                        continue

                                    if tutorial_boss_enemy_spontaneous_strike_chance == Hit and player_spontaneous_strike_chance == Miss:
                                        print(f"Oh! What a spectacle! Both competitiors crash into each other but {Tutorial_Boss.name}'s punch collides and {player_story_name}'s only misses by a large margain!")
                                        continue

                                    if tutorial_boss_enemy_spontaneous_strike_chance == Miss and player_spontaneous_strike_chance == Hit:
                                        print(f"Oh! What do we have here?! {player_story_name} and {Tutorial_Boss.name} have swung at each other at the same time! However, {player_story_name}'s punch collides hard with {Tutorial_Boss.name}'s face and {Tutorial_Boss.name} only misses his face by a few inches! ")      
                                        continue

                                    if tutorial_boss_enemy_spontaneous_strike_chance and player_spontaneous_strike_chance == Miss:
                                        print(f"Oh what a spectacle! Both {player_story_name} and {Tutorial_Boss.name} strike at each other with an enormous amount of force but they both miss! This is sure one hell of a fight! ")
                                        continue

                                if Tutorial_Boss.stamina < 30:
                                    print(f"{Tutorial_Boss.name} has started to take a short break and let his guard down! ")
                                    Tutorial_Boss.stamina + 20
                                    continue

                            if tutorial_boss_turn_attack == Left_Hook:
                                if Tutorial_Boss.stamina >= 15:
                                    Tutorial_Boss.stamina -= 15
                                    print(f"And {Tutorial_Boss.name} tries for a left hook! ")
                                    time.sleep(1)
                                    if tutorial_boss_enemy_spontaneous_strike_chance and player_spontaneous_strike_chance == Hit:
                                        print(f"And we have a amazing spectalce! Both {player_story_name} and {Tutorial_Boss.name} hit each other at the same time! ")
                                        continue

                                    if tutorial_boss_enemy_spontaneous_strike_chance == Hit and player_spontaneous_strike_chance == Miss:
                                        print(f"Oh! What a spectacle! Both competitiors crash into each other but {Tutorial_Boss.name}'s punch collides and {player_story_name}'s only misses by a large margain!")
                                        continue

                                    if tutorial_boss_enemy_spontaneous_strike_chance == Miss and player_spontaneous_strike_chance == Hit:
                                        print(f"Oh! What do we have here?! {player_story_name} and {Tutorial_Boss.name} have swung at each other at the same time! However, {player_story_name}'s punch collides hard with {Tutorial_Boss.name}'s face and {Tutorial_Boss.name} only misses his face by a few inches! ")      
                                        continue

                                    if tutorial_boss_enemy_spontaneous_strike_chance and player_spontaneous_strike_chance == Miss:
                                        print(f"Oh what a spectacle! Both {player_story_name} and {Tutorial_Boss.name} strike at each other with an enormous amount of force but they both miss! This is sure one hell of a fight! ")
                                        continue

                            if tutorial_boss_turn_attack == Right_Hook:
                                if Tutorial_Boss.stamina >= 45:
                                    Tutorial_Boss.stamina -= 45
                                    print(f"And {Tutorial_Boss.name} tries for a right hook! ")
                                    time.sleep(1)
                                    if tutorial_boss_enemy_spontaneous_strike_chance and player_spontaneous_strike_chance == Hit:
                                        print(f"And we have a amazing spectalce! Both {player_story_name} and {Tutorial_Boss.name} hit each other at the same time! ")
                                        continue

                                    if tutorial_boss_enemy_spontaneous_strike_chance == Hit and player_spontaneous_strike_chance == Miss:
                                        print(f"Oh! What a spectacle! Both competitiors crash into each other but {Tutorial_Boss.name}'s punch collides and {player_story_name}'s only misses by a large margain!")
                                        continue

                                    if tutorial_boss_enemy_spontaneous_strike_chance == Miss and player_spontaneous_strike_chance == Hit:
                                        print(f"Oh! What do we have here?! {player_story_name} and {Tutorial_Boss.name} have swung at each other at the same time! However, {player_story_name}'s punch collides hard with {Tutorial_Boss.name}'s face and {Tutorial_Boss.name} only misses his face by a few inches! ")      
                                        continue

                                    if tutorial_boss_enemy_spontaneous_strike_chance and player_spontaneous_strike_chance == Miss:
                                        print(f"Oh what a spectacle! Both {player_story_name} and {Tutorial_Boss.name} strike at each other with an enormous amount of force but they both miss! This is sure one hell of a fight! ")
                                        continue

                                if Tutorial_Boss.stamina < 45:
                                    print(f"{Tutorial_Boss.name} has started to take a short break and let his guard down! ")
                                    Tutorial_Boss.stamina + 20
                                    continue                                    

                            if tutorial_boss_turn_attack == Right_Uppercut:
                                if Tutorial_Boss.stamina >= 60:
                                    Tutorial_Boss.stamina -= 60
                                    print(f"And {Tutorial_Boss.name} tries for a right uppercut! ")
                                    time.sleep(1)
                                    if tutorial_boss_enemy_spontaneous_strike_chance and player_spontaneous_strike_chance == Hit:
                                        print(f"And we have a amazing spectalce! Both {player_story_name} and {Tutorial_Boss.name} hit each other at the same time! ")
                                        continue

                                    if tutorial_boss_enemy_spontaneous_strike_chance == Hit and player_spontaneous_strike_chance == Miss:
                                        print(f"Oh! What a spectacle! Both competitiors crash into each other but {Tutorial_Boss.name}'s punch collides and {player_story_name}'s only misses by a large margain!")
                                        continue

                                    if tutorial_boss_enemy_spontaneous_strike_chance == Miss and player_spontaneous_strike_chance == Hit:
                                        print(f"Oh! What do we have here?! {player_story_name} and {Tutorial_Boss.name} have swung at each other at the same time! However, {player_story_name}'s punch collides hard with {Tutorial_Boss.name}'s face and {Tutorial_Boss.name} only misses his face by a few inches! ")      
                                        continue

                                    if tutorial_boss_enemy_spontaneous_strike_chance and player_spontaneous_strike_chance == Miss:
                                        print(f"Oh what a spectacle! Both {player_story_name} and {Tutorial_Boss.name} strike at each other with an enormous amount of force but they both miss! This is sure one hell of a fight! ")
                                        continue

                                if Tutorial_Boss.stamina < 60:
                                    print(f"{Tutorial_Boss.name} has started to take a short break and let his guard down! ")
                                    Tutorial_Boss.stamina + 20
                                    continue

                    if player_stamina < 45:
                        print("Sorry, you do not have enough stamina to perform this attack. ")
                        continue     

                if attack_move == "Right Uppercut":
                    if player_stamina >= 60:
                        player_stamina -= 60
                        print(f"{player_story_name} goes for a beautiful right uppercut! ")
                        tutorial_boss_turn = random.choice(tutorial_boss_enemy_actions)
                        time.sleep(1)
                        if tutorial_boss_turn != Defend:
                            print(f"And it penetrates straight through {Tutorial_Boss.name}'s defense! ")                        
                            Tutorial_Boss.health -= Right_Uppercut.damage

                        if tutorial_boss_turn == Defend:
                            print(f"But {player_story_name}'s punch was skillfully evaded by an excellent block from {Tutorial_Boss.name}! ")
                            Tutorial_Boss.health = Tutorial_Boss.health
                            continue

                        if tutorial_boss_turn == Attack:
                            if tutorial_boss_turn_attack == Jab:
                                if Tutorial_Boss.stamina >= 10:
                                    Tutorial_Boss.stamina -= 10
                                    print(f"And {Tutorial_Boss.name} tries for a jab! ")
                                    time.sleep(1)
                                    if tutorial_boss_enemy_spontaneous_strike_chance and player_spontaneous_strike_chance == Hit:
                                        print(f"And we have a amazing spectalce! Both {player_story_name} and {Tutorial_Boss.name} hit each other at the same time! ")
                                        continue

                                    if tutorial_boss_enemy_spontaneous_strike_chance == Hit and player_spontaneous_strike_chance == Miss:
                                        print(f"Oh! What a spectacle! Both competitiors crash into each other but {Tutorial_Boss.name}'s punch collides and {player_story_name}'s only misses by a large margain!")
                                        continue

                                    if tutorial_boss_enemy_spontaneous_strike_chance == Miss and player_spontaneous_strike_chance == Hit:
                                        print(f"Oh! What do we have here?! {player_story_name} and {Tutorial_Boss.name} have swung at each other at the same time! However, {player_story_name}'s punch collides hard with {Tutorial_Boss.name}'s face and {Tutorial_Boss.name} only misses his face by a few inches! ")      
                                        continue

                                    if tutorial_boss_enemy_spontaneous_strike_chance and player_spontaneous_strike_chance == Miss:
                                        print(f"Oh what a spectacle! Both {player_story_name} and {Tutorial_Boss.name} strike at each other with an enormous amount of force but they both miss! This is sure one hell of a fight! ")
                                        continue

                                if Tutorial_Boss.stamina < 10:
                                    print(f"{Tutorial_Boss.name} has started to take a short break and let his guard down! ")
                                    Tutorial_Boss.stamina + 20
                                    continue

                            if tutorial_boss_turn_attack == Straight:
                                if Tutorial_Boss.stamina >= 30:
                                    Tutorial_Boss.stamina -= 30
                                    print(f"And {Tutorial_Boss.name} tries for a straight! ")
                                    time.sleep(1)
                                    if tutorial_boss_enemy_spontaneous_strike_chance and player_spontaneous_strike_chance == Hit:
                                        print(f"And we have a amazing spectalce! Both {player_story_name} and {Tutorial_Boss.name} hit each other at the same time! ")
                                        continue

                                    if tutorial_boss_enemy_spontaneous_strike_chance == Hit and player_spontaneous_strike_chance == Miss:
                                        print(f"Oh! What a spectacle! Both competitiors crash into each other but {Tutorial_Boss.name}'s punch collides and {player_story_name}'s only misses by a large margain!")
                                        continue

                                    if tutorial_boss_enemy_spontaneous_strike_chance == Miss and player_spontaneous_strike_chance == Hit:
                                        print(f"Oh! What do we have here?! {player_story_name} and {Tutorial_Boss.name} have swung at each other at the same time! However, {player_story_name}'s punch collides hard with {Tutorial_Boss.name}'s face and {Tutorial_Boss.name} only misses his face by a few inches! ")      
                                        continue

                                    if tutorial_boss_enemy_spontaneous_strike_chance and player_spontaneous_strike_chance == Miss:
                                        print(f"Oh what a spectacle! Both {player_story_name} and {Tutorial_Boss.name} strike at each other with an enormous amount of force but they both miss! This is sure one hell of a fight! ")
                                        continue

                                if Tutorial_Boss.stamina < 30:
                                    print(f"{Tutorial_Boss.name} has started to take a short break and let his guard down! ")
                                    Tutorial_Boss.stamina + 20
                                    continue

                            if tutorial_boss_turn_attack == Left_Hook:
                                if Tutorial_Boss.stamina >= 15:
                                    Tutorial_Boss.stamina -= 15
                                    print(f"And {Tutorial_Boss.name} tries for a left hook! ")
                                    time.sleep(1)
                                    if tutorial_boss_enemy_spontaneous_strike_chance and player_spontaneous_strike_chance == Hit:
                                        print(f"And we have a amazing spectalce! Both {player_story_name} and {Tutorial_Boss.name} hit each other at the same time! ")
                                        continue

                                    if tutorial_boss_enemy_spontaneous_strike_chance == Hit and player_spontaneous_strike_chance == Miss:
                                        print(f"Oh! What a spectacle! Both competitiors crash into each other but {Tutorial_Boss.name}'s punch collides and {player_story_name}'s only misses by a large margain!")
                                        continue

                                    if tutorial_boss_enemy_spontaneous_strike_chance == Miss and player_spontaneous_strike_chance == Hit:
                                        print(f"Oh! What do we have here?! {player_story_name} and {Tutorial_Boss.name} have swung at each other at the same time! However, {player_story_name}'s punch collides hard with {Tutorial_Boss.name}'s face and {Tutorial_Boss.name} only misses his face by a few inches! ")      
                                        continue

                                    if tutorial_boss_enemy_spontaneous_strike_chance and player_spontaneous_strike_chance == Miss:
                                        print(f"Oh what a spectacle! Both {player_story_name} and {Tutorial_Boss.name} strike at each other with an enormous amount of force but they both miss! This is sure one hell of a fight! ")
                                        continue

                            if tutorial_boss_turn_attack == Right_Hook:
                                if Tutorial_Boss.stamina >= 45:
                                    Tutorial_Boss.stamina -= 45
                                    print(f"And {Tutorial_Boss.name} tries for a right hook! ")
                                    time.sleep(1)
                                    if tutorial_boss_enemy_spontaneous_strike_chance and player_spontaneous_strike_chance == Hit:
                                        print(f"And we have a amazing spectalce! Both {player_story_name} and {Tutorial_Boss.name} hit each other at the same time! ")
                                        continue

                                    if tutorial_boss_enemy_spontaneous_strike_chance == Hit and player_spontaneous_strike_chance == Miss:
                                        print(f"Oh! What a spectacle! Both competitiors crash into each other but {Tutorial_Boss.name}'s punch collides and {player_story_name}'s only misses by a large margain!")
                                        continue

                                    if tutorial_boss_enemy_spontaneous_strike_chance == Miss and player_spontaneous_strike_chance == Hit:
                                        print(f"Oh! What do we have here?! {player_story_name} and {Tutorial_Boss.name} have swung at each other at the same time! However, {player_story_name}'s punch collides hard with {Tutorial_Boss.name}'s face and {Tutorial_Boss.name} only misses his face by a few inches! ")      
                                        continue

                                    if tutorial_boss_enemy_spontaneous_strike_chance and player_spontaneous_strike_chance == Miss:
                                        print(f"Oh what a spectacle! Both {player_story_name} and {Tutorial_Boss.name} strike at each other with an enormous amount of force but they both miss! This is sure one hell of a fight! ")
                                        continue

                                if Tutorial_Boss.stamina < 45:
                                    print(f"{Tutorial_Boss.name} has started to take a short break and let his guard down! ")
                                    Tutorial_Boss.stamina + 20
                                    continue                                    

                            if tutorial_boss_turn_attack == Right_Uppercut:
                                if Tutorial_Boss.stamina >= 60:
                                    Tutorial_Boss.stamina -= 60
                                    print(f"And {Tutorial_Boss.name} tries for a right uppercut! ")
                                    time.sleep(1)
                                    if tutorial_boss_enemy_spontaneous_strike_chance and player_spontaneous_strike_chance == Hit:
                                        print(f"And we have a amazing spectalce! Both {player_story_name} and {Tutorial_Boss.name} hit each other at the same time! ")
                                        continue

                                    if tutorial_boss_enemy_spontaneous_strike_chance == Hit and player_spontaneous_strike_chance == Miss:
                                        print(f"Oh! What a spectacle! Both competitiors crash into each other but {Tutorial_Boss.name}'s punch collides and {player_story_name}'s only misses by a large margain!")
                                        continue

                                    if tutorial_boss_enemy_spontaneous_strike_chance == Miss and player_spontaneous_strike_chance == Hit:
                                        print(f"Oh! What do we have here?! {player_story_name} and {Tutorial_Boss.name} have swung at each other at the same time! However, {player_story_name}'s punch collides hard with {Tutorial_Boss.name}'s face and {Tutorial_Boss.name} only misses his face by a few inches! ")      
                                        continue

                                    if tutorial_boss_enemy_spontaneous_strike_chance and player_spontaneous_strike_chance == Miss:
                                        print(f"Oh what a spectacle! Both {player_story_name} and {Tutorial_Boss.name} strike at each other with an enormous amount of force but they both miss! This is sure one hell of a fight! ")
                                        continue

                                if Tutorial_Boss.stamina < 60:
                                    print(f"{Tutorial_Boss.name} has started to take a short break and let his guard down! ")
                                    Tutorial_Boss.stamina + 20
                                    continue

                    if player_stamina < 60:
                        print("Sorry, you do not have enough stamina to perform this attack. ")
                        continue                

                else:
                    print("That's not a choice kid... ")
                    continue

            if player_turn == "Defend":
                defend_move = input("What kind of defense do you want to use?  Choices: Block Forward/Block Side/Block Down ")
                if defend_move == "Block Forward":
                    print(f"{player_story_name} tries to block a forward punch ")

                if defend_move == "Block Side":
                    print(f"{player_story_name} tries to block a punch to the side! ")

                if defend_move == "Block Down":
                    print(f"{player_story_name} tries to block a uppercut! ")

                else:
                    print("That's not a choice kid... ")
                    continue

            if player_turn == "Rest":
                rest_move = input("How do you want to rest?  Choices: Relax Muscles/Put Guard Down/Full Body Relaxation ")
                if rest_move == "Relax Muscles":
                    print(f"{player_story_name} seems to be relaxing {player_pronoun3.lower} muscles! ")

                if rest_move == "Put Guard Down":
                    print(f"{player_story_name} seems to be relaxing putting {player_pronoun3.lower} guard down! ")

                if rest_move == "Full Body Relaxation":
                    print(f"{player_story_name} seems to be relaxing fully relaxing {player_pronoun3.lower} body! ")
                
                else:
                    print("That's not a choice kid... ")
                    continue   

            else:
                print("That's not a choice kid... ")
                continue

    if ready == "N":
        print("Thank you for playing our game! ")