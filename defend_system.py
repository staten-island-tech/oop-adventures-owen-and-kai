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

def defend_system(player_story_name):
    while True:
        defend_move = input("What kind of defense do you want to use?  Choices: Block Forward/Block Side/Block Down ")
        if defend_move == "Block Forward":
            print(f"{player_story_name} tries to block a forward punch ")
            time.sleep(1)
            if tutorial_boss_enemy_turn == Attack:
                if tutorial_boss_turn_attack == Jab:
                    if Tutorial_Boss.stamina >= 10:
                        Tutorial_Boss.stamina -= 10
                        print(f"And {player_story_name} blocks a spectacular jab from {Tutorial_Boss.name}! ")
                        player_health = player_health
                        time.sleep(1)
                        continue

                    if Tutorial_Boss.stamina < 10:
                        print(f"But {Tutorial_Boss.name} has started to take a short break and doesn't attack at all! ")
                        time.sleep(1)
                        Tutorial_Boss.stamina + 20                                
                        Tutorial_Boss.health = Tutorial_Boss.health
                        time.sleep(1)
                        continue

                if tutorial_boss_turn_attack == Straight:
                    if Tutorial_Boss.stamina >= 30:
                        Tutorial_Boss.stamina -= 30
                        print(f"And {player_story_name} skillfully evades a spectacular straight from {Tutorial_Boss.name}! ")
                        player_health = player_health
                        time.sleep(1)
                        continue

                    if Tutorial_Boss.stamina < 30:
                        print(f"But {Tutorial_Boss.name} has started to take a short break and doesn't attack at all! ")
                        time.sleep(1)
                        Tutorial_Boss.stamina + 20                                
                        Tutorial_Boss.health = Tutorial_Boss.health
                        time.sleep(1)
                        continue

                if tutorial_boss_turn_attack == Left_Hook:
                    if Tutorial_Boss.stamina >= 15:
                        Tutorial_Boss.stamina -= 15
                        print(f"Oh! What do we have here! {player_story_name} tries to block a forward punch but {Tutorial_Boss.name} goes for a tremendous left hook to the face! ")
                        player_health -= Left_Hook.damage
                        time.sleep(1)
                        continue

                    if Tutorial_Boss.stamina < 15:
                        print(f"But {Tutorial_Boss.name} has started to take a short break and doesn't attack at all! ")
                        time.sleep(1)
                        Tutorial_Boss.stamina + 20                                
                        Tutorial_Boss.health = Tutorial_Boss.health
                        time.sleep(1)
                        continue

                if tutorial_boss_turn_attack == Right_Hook:
                    if Tutorial_Boss.stamina >= 45:
                        Tutorial_Boss.stamina -= 45
                        print(f"Oh! What a spectacle! {player_story_name} tries to block a forward punch but {Tutorial_Boss.name} goes for a bone_breaking right hook to the body! ")
                        player_health -= Right_Hook.damage
                        time.sleep(1)
                        continue

                    if Tutorial_Boss.stamina < 45:
                        print(f"But {Tutorial_Boss.name} has started to take a short break and doesn't attack at all! ")
                        time.sleep(1)
                        Tutorial_Boss.stamina + 20                                
                        Tutorial_Boss.health = Tutorial_Boss.health
                        time.sleep(1)
                        continue

                if tutorial_boss_turn_attack == Right_Uppercut:
                    if Tutorial_Boss.stamina >= 60:
                        Tutorial_Boss.stamina -= 60
                        print(f"Oh! What a surprise! {player_story_name} tries to block a forward punch but {Tutorial_Boss.name} goes for a jaw_breaking right uppercut to the chin! ")
                        player_health -= Right_Uppercut.damage
                        time.sleep(1)
                        continue   

                    if Tutorial_Boss.stamina < 60:
                        print(f"But {Tutorial_Boss.name} has started to take a short break and doesn't attack at all! ")
                        time.sleep(1)
                        Tutorial_Boss.stamina + 20                                
                        Tutorial_Boss.health = Tutorial_Boss.health
                        time.sleep(1)
                        continue                     

        if defend_move == "Block Side":
            print(f"{player_story_name} tries to block a punch to the side! ")

        if defend_move == "Block Down":
            print(f"{player_story_name} tries to block a uppercut! ")

        else:
            print("That's not a choice kid... ")
            continue