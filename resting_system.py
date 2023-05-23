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

def resting_system(player_story_name, player_pronoun3, player_stamina, player_health):
    while True:
        rest_move = input("How do you want to rest?  Choices: Relax Muscles/Put Guard Down/Full Body Relaxation ")
        if rest_move == "Relax Muscles":
            print(f"{player_story_name} seems to be relaxing {player_pronoun3.lower} muscles! ")
            player_stamina += 20
            time.sleep(1)
            if tutorial_boss_enemy_turn == Attack:
                if tutorial_boss_turn_attack == Jab:
                    if Tutorial_Boss.stamina >= 10:
                        Tutorial_Boss.stamina -= 10
                        print(f"Christ! {Tutorial_Boss.name} catches on to this and hits {player_story_name} with a nose-breaking jab to the face! ")
                        player_health -= Jab.damage
                        print(f"Health: {player_health} Stamina: {player_stamina} ")
                        time.sleep(1)
                        continue

                    if Tutorial_Boss.stamina < 10:
                        print(f"But {Tutorial_Boss.name} has started to take a short break and doesn't attack at all! ")
                        time.sleep(1)
                        Tutorial_Boss.stamina + 20                                
                        Tutorial_Boss.health = Tutorial_Boss.health
                        print(f"Health: {player_health} Stamina: {player_stamina} ")
                        time.sleep(1)
                        continue

                if tutorial_boss_turn_attack == Straight:
                    if Tutorial_Boss.stamina >= 30:
                        Tutorial_Boss.stamina -= 30
                        print(f"Christ! {Tutorial_Boss.name} catches on to this and hits {player_story_name} with a jaw-breaking straight to the face! ")
                        player_health -= Straight.damage
                        print(f"Health: {player_health} Stamina: {player_stamina} ")
                        time.sleep(1)
                        continue

                    if Tutorial_Boss.stamina < 30:
                        print(f"But {Tutorial_Boss.name} has started to take a short break and doesn't attack at all! ")
                        time.sleep(1)
                        Tutorial_Boss.stamina + 20                                
                        Tutorial_Boss.health = Tutorial_Boss.health
                        print(f"Health: {player_health} Stamina: {player_stamina} ")
                        time.sleep(1)
                        continue

                if tutorial_boss_turn_attack == Left_Hook:
                    if Tutorial_Boss.stamina >= 15:
                        Tutorial_Boss.stamina -= 15
                        print(f"Christ! {Tutorial_Boss.name} catches on to this and hits {player_story_name} with a mind-blowing left hook to the face! ")
                        player_health -= Left_Hook.damage
                        print(f"Health: {player_health} Stamina: {player_stamina} ")
                        time.sleep(1)
                        continue

                    if Tutorial_Boss.stamina < 30:
                        print(f"But {Tutorial_Boss.name} has started to take a short break and doesn't attack at all! ")
                        time.sleep(1)
                        Tutorial_Boss.stamina + 20                                
                        Tutorial_Boss.health = Tutorial_Boss.health
                        print(f"Health: {player_health} Stamina: {player_stamina} ")
                        time.sleep(1)
                        continue

                if tutorial_boss_turn_attack == Right_Hook:
                    if Tutorial_Boss.stamina >= 45:
                        Tutorial_Boss.stamina -= 45
                        print(f"Christ! {Tutorial_Boss.name} catches on to this and hits {player_story_name} with a skull-crushing right hook to the head! ")
                        player_health -= Left_Hook.damage
                        print(f"Health: {player_health} Stamina: {player_stamina} ")
                        time.sleep(1)
                        continue

                    if Tutorial_Boss.stamina < 45:
                        print(f"But {Tutorial_Boss.name} has started to take a short break and doesn't attack at all! ")
                        time.sleep(1)
                        Tutorial_Boss.stamina + 20                                
                        Tutorial_Boss.health = Tutorial_Boss.health
                        print(f"Health: {player_health} Stamina: {player_stamina} ")
                        time.sleep(1)
                        continue

                if tutorial_boss_turn_attack == Right_Uppercut:
                    if Tutorial_Boss.stamina >= 60:
                        Tutorial_Boss.stamina -= 60
                        print(f"Christ! {Tutorial_Boss.name} catches on to this and hits {player_story_name} with a neck-snapping right uppercut to the head! ")
                        player_health -= Left_Hook.damage
                        print(f"Health: {player_health} Stamina: {player_stamina} ")
                        time.sleep(1)
                        continue

                    if Tutorial_Boss.stamina < 60:
                        print(f"But {Tutorial_Boss.name} has started to take a short break and doesn't attack at all! ")
                        time.sleep(1)
                        Tutorial_Boss.stamina + 20                                
                        Tutorial_Boss.health = Tutorial_Boss.health
                        print(f"Health: {player_health} Stamina: {player_stamina} ")
                        time.sleep(1)
                        continue
                    
        if rest_move == "Put Guard Down":
            print(f"{player_story_name} seems to be relaxing putting {player_pronoun3.lower} guard down! ")

        if rest_move == "Full Body Relaxation":
            print(f"{player_story_name} seems to be relaxing fully relaxing {player_pronoun3.lower} body! ")
        
        else:
            print("That's not a choice kid... ")
            continue   