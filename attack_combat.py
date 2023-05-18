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

tutorial_boss_enemy_actions = [Attack, Attack, Attack, Defend]
tutorial_boss_enemy_turn = random.choice(tutorial_boss_enemy_actions)

if tutorial_boss_enemy_turn == Attack:
    tutorial_boss_enemy_spontaneous_strike = [Hit, Miss, Miss, Miss]
    tutorial_boss_enemy_spontaneous_strike_chance = random.choice(tutorial_boss_enemy_spontaneous_strike)

tutorial_boss_enemy_attack = [Jab, Straight, Left_Hook, Right_Hook, Right_Uppercut]
tutorial_boss_turn_attack = random.choice(tutorial_boss_enemy_attack)

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

attack_move = input("What kind of attack do you want to use?  Choices: Jab/Straight/Left Hook/Right Hook/Right Uppercut ")
    if attack_move == "Jab":
        if player_stamina >= 10:
            player_stamina -= 10
            print(f"{player_story_name} goes for a beautiful jab! ")
            tutorial_boss_enemy_turn = random.choice(tutorial_boss_enemy_actions)
            time.sleep(1)           
            if tutorial_boss_enemy_turn == Defend:
                print(f"But {player_story_name}'s punch was skillfully evaded by an excellent block from {Tutorial_Boss.name}! ")
                Tutorial_Boss.health = Tutorial_Boss.health
                print(f"Health: {player_health} Stamina: {player_stamina} ")
                time.sleep(1)  
                continue

            if tutorial_boss_enemy_turn == Attack:
                if tutorial_boss_turn_attack == Jab:
                    if Tutorial_Boss.stamina >= 10:
                        Tutorial_Boss.stamina -= 10
                        print(f"And {Tutorial_Boss.name} tries for a jab! ")
                        time.sleep(1)
                        if tutorial_boss_enemy_spontaneous_strike_chance and player_spontaneous_strike_chance == Hit:
                            print(f"And we have a amazing spectalce! Both {player_story_name} and {Tutorial_Boss.name} hit each other at the same time! ")
                            player_health -= Jab.damage
                            Tutorial_Boss.health -= Jab.damage
                            print(f"Health: {player_health} Stamina: {player_stamina} ") 
                            time.sleep(1) 
                            continue

                        if tutorial_boss_enemy_spontaneous_strike_chance == Hit and player_spontaneous_strike_chance == Miss:
                            print(f"Oh! What a spectacle! Both competitiors crash into each other but {Tutorial_Boss.name}'s punch collides and {player_story_name}'s only misses by a large margain!")
                            player_health -= Jab.damage
                            Tutorial_Boss.health = Tutorial_Boss.health
                            print(f"Health: {player_health} Stamina: {player_stamina} ") 
                            time.sleep(1) 
                            continue

                        if tutorial_boss_enemy_spontaneous_strike_chance == Miss and player_spontaneous_strike_chance == Hit:
                            print(f"Oh! What do we have here?! {player_story_name} and {Tutorial_Boss.name} have swung at each other at the same time! However, {player_story_name}'s punch collides hard with {Tutorial_Boss.name}'s face and {Tutorial_Boss.name} only misses his face by a few inches! ")  
                            player_health = player_health 
                            Tutorial_Boss.health -= Jab.damage
                            print(f"Health: {player_health} Stamina: {player_stamina} ")
                            time.sleep(1)  
                            continue

                        if tutorial_boss_enemy_spontaneous_strike_chance and player_spontaneous_strike_chance == Miss:
                            print(f"Oh what a spectacle! Both {player_story_name} and {Tutorial_Boss.name} strike at each other with an enormous amount of force but they both miss! This is sure one hell of a fight! ")
                            player_health = player_health
                            Tutorial_Boss.health = Tutorial_Boss.health
                            print(f"Health: {player_health} Stamina: {player_stamina} ")
                            time.sleep(1)  
                            continue

                    if Tutorial_Boss.stamina < 10:
                        print(f"{Tutorial_Boss.name} has started to take a short break and let his guard down! ")
                        time.sleep(1)
                        Tutorial_Boss.stamina + 20
                        print(f"{player_story_name} uses this chance and strikes {Tutorial_Boss.name} with an incredible jab to the face! ")
                        Tutorial_Boss.health -= Jab.damage
                        time.sleep(1)
                        continue

                if tutorial_boss_turn_attack == Straight:
                    if Tutorial_Boss.stamina >= 30:
                        Tutorial_Boss.stamina -= 30
                        print(f"And {Tutorial_Boss.name} tries for a straight! ")
                        time.sleep(1)
                        if tutorial_boss_enemy_spontaneous_strike_chance and player_spontaneous_strike_chance == Hit:
                            print(f"And we have a amazing spectalce! Both {player_story_name} and {Tutorial_Boss.name} hit each other at the same time! ")
                            player_health -= Straight.damage 
                            Tutorial_Boss.health -= Jab.damage
                            print(f"Health: {player_health} Stamina: {player_stamina} ") 
                            time.sleep(1) 
                            continue

                        if tutorial_boss_enemy_spontaneous_strike_chance == Hit and player_spontaneous_strike_chance == Miss:
                            print(f"Oh! What a spectacle! Both competitiors crash into each other but {Tutorial_Boss.name}'s punch collides and {player_story_name}'s only misses by a large margain!")
                            player_health -= Straight.damage
                            Tutorial_Boss.health = Tutorial_Boss.health
                            print(f"Health: {player_health} Stamina: {player_stamina} ") 
                            time.sleep(1) 
                            continue

                        if tutorial_boss_enemy_spontaneous_strike_chance == Miss and player_spontaneous_strike_chance == Hit:
                            print(f"Oh! What do we have here?! {player_story_name} and {Tutorial_Boss.name} have swung at each other at the same time! However, {player_story_name}'s punch collides hard with {Tutorial_Boss.name}'s face and {Tutorial_Boss.name} only misses his face by a few inches! ")  
                            player_health = player_health
                            Tutorial_Boss.health -= Jab.damage
                            print(f"Health: {player_health} Stamina: {player_stamina} ")  
                            time.sleep(1)
                            continue

                        if tutorial_boss_enemy_spontaneous_strike_chance and player_spontaneous_strike_chance == Miss:
                            print(f"Oh what a spectacle! Both {player_story_name} and {Tutorial_Boss.name} strike at each other with an enormous amount of force but they both miss! This is sure one hell of a fight! ")
                            player_health = player_health
                            Tutorial_Boss.health = Tutorial_Boss.health
                            print(f"Health: {player_health} Stamina: {player_stamina} ") 
                            time.sleep(1) 
                            continue

                    if Tutorial_Boss.stamina < 30:
                        print(f"{Tutorial_Boss.name} has started to take a short break and let his guard down! ")
                        Tutorial_Boss.stamina + 20
                        time.sleep(1)
                        print(f"{player_story_name} uses this chance and strikes {Tutorial_Boss.name} with an incredible jab to the face! ")
                        Tutorial_Boss.health -= Jab.damage
                        time.sleep(1)
                        continue

                if tutorial_boss_turn_attack == Left_Hook:
                    if Tutorial_Boss.stamina >= 15:
                        Tutorial_Boss.stamina -= 15
                        print(f"And {Tutorial_Boss.name} tries for a left hook! ")
                        time.sleep(1)
                        if tutorial_boss_enemy_spontaneous_strike_chance and player_spontaneous_strike_chance == Hit:
                            print(f"And we have a amazing spectalce! Both {player_story_name} and {Tutorial_Boss.name} hit each other at the same time! ")
                            player_health -= Left_Hook.damage 
                            Tutorial_Boss.health -= Jab.damage
                            print(f"Health: {player_health} Stamina: {player_stamina} ") 
                            time.sleep(1) 
                            continue

                        if tutorial_boss_enemy_spontaneous_strike_chance == Hit and player_spontaneous_strike_chance == Miss:
                            print(f"Oh! What a spectacle! Both competitiors crash into each other but {Tutorial_Boss.name}'s punch collides and {player_story_name}'s only misses by a large margain!")
                            player_health -= Left_Hook.damage
                            Tutorial_Boss.health = Tutorial_Boss.health
                            print(f"Health: {player_health} Stamina: {player_stamina} ")  
                            time.sleep(1)
                            continue

                        if tutorial_boss_enemy_spontaneous_strike_chance == Miss and player_spontaneous_strike_chance == Hit:
                            print(f"Oh! What do we have here?! {player_story_name} and {Tutorial_Boss.name} have swung at each other at the same time! However, {player_story_name}'s punch collides hard with {Tutorial_Boss.name}'s face and {Tutorial_Boss.name} only misses his face by a few inches! ")   
                            player_health = player_health
                            Tutorial_Boss.health -= Jab.damage
                            print(f"Health: {player_health} Stamina: {player_stamina} ")  
                            time.sleep(1)
                            continue

                        if tutorial_boss_enemy_spontaneous_strike_chance and player_spontaneous_strike_chance == Miss:
                            print(f"Oh what a spectacle! Both {player_story_name} and {Tutorial_Boss.name} strike at each other with an enormous amount of force but they both miss! This is sure one hell of a fight! ")
                            player_health = player_health
                            Tutorial_Boss.health = Tutorial_Boss.health
                            print(f"Health: {player_health} Stamina: {player_stamina} ")  
                            time.sleep(1)
                            continue

                    if Tutorial_Boss.stamina < 45:
                        print(f"{Tutorial_Boss.name} has started to take a short break and let his guard down! ")
                        Tutorial_Boss.stamina + 20
                        time.sleep(1)
                        print(f"{player_story_name} uses this chance and strikes {Tutorial_Boss.name} with an incredible jab to the face! ")
                        Tutorial_Boss.health -= Jab.damage
                        time.sleep(1)
                        continue     

                if tutorial_boss_turn_attack == Right_Hook:
                    if Tutorial_Boss.stamina >= 45:
                        Tutorial_Boss.stamina -= 45
                        print(f"And {Tutorial_Boss.name} tries for a right hook! ")
                        time.sleep(1)
                        if tutorial_boss_enemy_spontaneous_strike_chance and player_spontaneous_strike_chance == Hit:
                            print(f"And we have a amazing spectalce! Both {player_story_name} and {Tutorial_Boss.name} hit each other at the same time! ")
                            player_health -= Right_Hook.damage
                            Tutorial_Boss.health -= Jab.damage
                            print(f"Health: {player_health} Stamina: {player_stamina} ")
                            time.sleep(1)  
                            continue

                        if tutorial_boss_enemy_spontaneous_strike_chance == Hit and player_spontaneous_strike_chance == Miss:
                            print(f"Oh! What a spectacle! Both competitiors crash into each other but {Tutorial_Boss.name}'s punch collides and {player_story_name}'s only misses by a large margain!")
                            player_health -= Right_Hook.damage
                            Tutorial_Boss.health = Tutorial_Boss.health
                            print(f"Health: {player_health} Stamina: {player_stamina} ")
                            time.sleep(1)  
                            continue

                        if tutorial_boss_enemy_spontaneous_strike_chance == Miss and player_spontaneous_strike_chance == Hit:
                            print(f"Oh! What do we have here?! {player_story_name} and {Tutorial_Boss.name} have swung at each other at the same time! However, {player_story_name}'s punch collides hard with {Tutorial_Boss.name}'s face and {Tutorial_Boss.name} only misses his face by a few inches! ") 
                            player_health = player_health
                            Tutorial_Boss.health -= Jab.damage
                            print(f"Health: {player_health} Stamina: {player_stamina} ") 
                            time.sleep(1) 
                            continue

                        if tutorial_boss_enemy_spontaneous_strike_chance and player_spontaneous_strike_chance == Miss:
                            print(f"Oh what a spectacle! Both {player_story_name} and {Tutorial_Boss.name} strike at each other with an enormous amount of force but they both miss! This is sure one hell of a fight! ")
                            player_health = player_health
                            Tutorial_Boss.health = Tutorial_Boss.health
                            print(f"Health: {player_health} Stamina: {player_stamina} ") 
                            time.sleep(1) 
                            continue

                    if Tutorial_Boss.stamina < 45:
                        print(f"{Tutorial_Boss.name} has started to take a short break and let his guard down! ")
                        Tutorial_Boss.stamina + 20
                        time.sleep(1)
                        print(f"{player_story_name} uses this chance and strikes {Tutorial_Boss.name} with an incredible jab to the face! ")
                        Tutorial_Boss.health -= Jab.damage
                        time.sleep(1)
                        continue                                    

                if tutorial_boss_turn_attack == Right_Uppercut:
                    if Tutorial_Boss.stamina >= 60:
                        Tutorial_Boss.stamina -= 60
                        print(f"And {Tutorial_Boss.name} tries for a right uppercut! ")
                        time.sleep(1)
                        if tutorial_boss_enemy_spontaneous_strike_chance and player_spontaneous_strike_chance == Hit:
                            print(f"And we have a amazing spectalce! Both {player_story_name} and {Tutorial_Boss.name} hit each other at the same time! ")
                            player_health -= Right_Uppercut.damage
                            Tutorial_Boss.health -= Jab.damage
                            print(f"Health: {player_health} Stamina: {player_stamina} ")
                            time.sleep(1)  
                            continue

                        if tutorial_boss_enemy_spontaneous_strike_chance == Hit and player_spontaneous_strike_chance == Miss:
                            print(f"Oh! What a spectacle! Both competitiors crash into each other but {Tutorial_Boss.name}'s punch collides and {player_story_name}'s only misses by a large margain!")
                            player_health -= Right_Uppercut.damage
                            Tutorial_Boss.health = Tutorial_Boss.health
                            print(f"Health: {player_health} Stamina: {player_stamina} ")
                            time.sleep(1)  
                            continue

                        if tutorial_boss_enemy_spontaneous_strike_chance == Miss and player_spontaneous_strike_chance == Hit:
                            print(f"Oh! What do we have here?! {player_story_name} and {Tutorial_Boss.name} have swung at each other at the same time! However, {player_story_name}'s punch collides hard with {Tutorial_Boss.name}'s face and {Tutorial_Boss.name} only misses his face by a few inches! ")
                            player_health = player_health
                            Tutorial_Boss.health -= Jab.damage
                            print(f"Health: {player_health} Stamina: {player_stamina} ") 
                            time.sleep(1) 
                            continue

                        if tutorial_boss_enemy_spontaneous_strike_chance and player_spontaneous_strike_chance == Miss:
                            print(f"Oh what a spectacle! Both {player_story_name} and {Tutorial_Boss.name} strike at each other with an enormous amount of force but they both miss! This is sure one hell of a fight! ")
                            player_health = player_health
                            Tutorial_Boss.health = Tutorial_Boss.health
                            print(f"Health: {player_health} Stamina: {player_stamina} ") 
                            time.sleep(1) 
                            continue

                    if Tutorial_Boss.stamina < 60:
                        print(f"{Tutorial_Boss.name} has started to take a short break and let his guard down! ")
                        Tutorial_Boss.stamina + 20
                        time.sleep(1)
                        print(f"{player_story_name} uses this chance and strikes {Tutorial_Boss.name} with an incredible jab to the face! ")
                        Tutorial_Boss.health -= Jab.damage
                        time.sleep(1)
                        continue

        if player_stamina < 10:
            print(f"{player_story_name} seems fatigued and doesn't have enough energy to perform his attack! ")
            time.sleep(1)
            print(f"Holy! {Tutorial_Boss.name} catches on to this and sends a tremendous body shot into {player_story_name}! That definitely looked like it broke something! ")
            player_health -= 30
            print(f"Health: {player_health} Stamina: {player_stamina} ")
            continue

    if attack_move == "Straight":
        if player_stamina >= 30:
            player_stamina -= 30
            print(f"{player_story_name} goes for a beautiful straight! ")
            tutorial_boss_turn = random.choice(tutorial_boss_enemy_actions)                       
            time.sleep(1)
            
        
        if player_stamina < 30:
            print(f"{player_story_name} seems fatigued and doesn't have enough energy to perform his attack! ")
            time.sleep(1)
            print(f"Holy! {Tutorial_Boss.name} catches on to this and sends a tremendous body shot into {player_story_name}! That definitely looked like it broke something! ")
            player_health -= 30
            print(f"Health: {player_health} Stamina: {player_stamina} ")
            continue
                            
    if attack_move == "Left Hook":
        if player_stamina >= 15:
            player_stamina -= 15
            print(f"{player_story_name} goes for a beautiful left hook! ")
            tutorial_boss_turn = random.choice(tutorial_boss_enemy_actions)
            time.sleep(1)   
        
        if player_stamina < 15:
            print(f"{player_story_name} seems fatigued and doesn't have enough energy to perform his attack! ")
            time.sleep(1)
            print(f"Holy! {Tutorial_Boss.name} catches on to this and sends a tremendous body shot into {player_story_name}! That definitely looked like it broke something! ")
            player_health -= 30
            print(f"Health: {player_health} Stamina: {player_stamina} ")
            continue

    if attack_move == "Right Hook":
        if player_stamina >= 45:
            player_stamina -= 60
            print(f"{player_story_name} goes for a beautiful right hook! ")
            tutorial_boss_turn = random.choice(tutorial_boss_enemy_actions)
            time.sleep(1)
        
        if player_stamina < 45:
            print(f"{player_story_name} seems fatigued and doesn't have enough energy to perform his attack! ")
            time.sleep(1)
            print(f"Holy! {Tutorial_Boss.name} catches on to this and sends a tremendous body shot into {player_story_name}! That definitely looked like it broke something! ")
            player_health -= 30
            print(f"Health: {player_health} Stamina: {player_stamina} ")
            continue

    if attack_move == "Right Uppercut":
        if player_stamina >= 60:
            player_stamina -= 60
            print(f"{player_story_name} goes for a beautiful right uppercut! ")
            tutorial_boss_turn = random.choice(tutorial_boss_enemy_actions)
            time.sleep(1)              
        
        if player_stamina < 60:
            print(f"{player_story_name} seems fatigued and doesn't have enough energy to perform his attack! ")
            time.sleep(1)
            print(f"Holy! {Tutorial_Boss.name} catches on to this and sends a tremendous body shot into {player_story_name}! That definitely looked like it broke something! ")
            player_health -= 30
            print(f"Health: {player_health} Stamina: {player_stamina} ")
            continue

    else:
        print("That's not a choice kid... ")
        continue