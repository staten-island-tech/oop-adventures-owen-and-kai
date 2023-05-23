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
player_spontaneous_strike_chance = random.choice(player_spontaneous_strike)

def attack_system(player_health, player_stamina, player_story_name):
    while True:
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
                    tutorial_boss_turn_attack = random.choice(tutorial_boss_enemy_attack)
                    tutorial_boss_enemy_spontaneous_strike_chance = random.choice(tutorial_boss_enemy_spontaneous_strike)
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
                                Tutorial_Boss.health -= Jab.damage
                                print(f"Health: {player_health} Stamina: {player_stamina} ")
                                time.sleep(1)  
                                continue

                            if tutorial_boss_enemy_spontaneous_strike_chance and player_spontaneous_strike_chance == Miss:
                                print(f"Oh what a spectacle! Both {player_story_name} and {Tutorial_Boss.name} strike at each other with an enormous amount of force but they both miss! This is sure one hell of a fight! ")
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
                                Tutorial_Boss.health -= Jab.damage
                                print(f"Health: {player_health} Stamina: {player_stamina} ")  
                                time.sleep(1)
                                continue

                            if tutorial_boss_enemy_spontaneous_strike_chance and player_spontaneous_strike_chance == Miss:
                                print(f"Oh what a spectacle! Both {player_story_name} and {Tutorial_Boss.name} strike at each other with an enormous amount of force but they both miss! This is sure one hell of a fight! ")
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
                                Tutorial_Boss.health -= Jab.damage
                                print(f"Health: {player_health} Stamina: {player_stamina} ")  
                                time.sleep(1)
                                continue

                            if tutorial_boss_enemy_spontaneous_strike_chance and player_spontaneous_strike_chance == Miss:
                                print(f"Oh what a spectacle! Both {player_story_name} and {Tutorial_Boss.name} strike at each other with an enormous amount of force but they both miss! This is sure one hell of a fight! ")
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
                                Tutorial_Boss.health -= Jab.damage
                                print(f"Health: {player_health} Stamina: {player_stamina} ") 
                                time.sleep(1) 
                                continue

                            if tutorial_boss_enemy_spontaneous_strike_chance and player_spontaneous_strike_chance == Miss:
                                print(f"Oh what a spectacle! Both {player_story_name} and {Tutorial_Boss.name} strike at each other with an enormous amount of force but they both miss! This is sure one hell of a fight! ")
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
                                Tutorial_Boss.health -= Jab.damage
                                print(f"Health: {player_health} Stamina: {player_stamina} ") 
                                time.sleep(1) 
                                continue

                            if tutorial_boss_enemy_spontaneous_strike_chance and player_spontaneous_strike_chance == Miss:
                                print(f"Oh what a spectacle! Both {player_story_name} and {Tutorial_Boss.name} strike at each other with an enormous amount of force but they both miss! This is sure one hell of a fight! ")
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
                print("Sorry, you do not have enough stamina to perform this attack. ")
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
                print("Sorry, you do not have enough stamina to perform this attack. ")
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
                print("Sorry, you do not have enough stamina to perform this attack. ")
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
                print("Sorry, you do not have enough stamina to perform this attack. ")
                time.sleep(1)
                print(f"Holy! {Tutorial_Boss.name} catches on to this and sends a tremendous body shot into {player_story_name}! That definitely looked like it broke something! ")
                player_health -= 30
                print(f"Health: {player_health} Stamina: {player_stamina} ")
                continue

        else:
            print("That's not a choice kid... ")
            continue