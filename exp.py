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

player_exp = 0
player_level = 1
if player_exp == 100:
    player_level == 2
    print(f"You have leveled up to {player_level}! ")

if player_exp == 250:
    player_level == 3
    print(f"You have leveled up to {player_level}! ")

if player_exp == 500:
    player_level == 4
    print(f"You have leveled up to {player_level}! ")

if player_exp == 1000:
    player_level == 5
    print(f"You have leveled up to {player_level}! ")

tutorial_boss_enemy_actions = [Attack, Attack, Attack, Defend]
tutorial_boss_enemy_turn = random.choice(tutorial_boss_enemy_actions)

if tutorial_boss_enemy_turn == Attack:
    tutorial_boss_enemy_spontaneous_strike = [Hit, Miss, Miss, Miss]
    tutorial_boss_enemy_spontaneous_strike_chance = random.choice(tutorial_boss_enemy_spontaneous_strike)

tutorial_boss_enemy_attack = [Jab, Straight, Left_Hook, Right_Hook, Right_Uppercut]
tutorial_boss_turn_attack = random.choice(tutorial_boss_enemy_attack)

player_spontaneous_strike = [Hit, Miss, Miss, Miss]
player_spontaneous_strike_chance = random.choice(tutorial_boss_enemy_spontaneous_strike)

def exp_system():
    while True:
        if Tutorial_Boss.health <= 0 and player_health > 0:
            print("Congrajulations on your win champ! ")
            exp_earned = 500
            player_exp + exp_earned
        
        if Tutorial_Boss > 0 and player_health <= 0:
            print("You lost this time, but it's okay, you'll get them next time. ")
            exp_earned = 250
            player_exp + exp_earned

        if Tutorial_Boss <= 0 and player_health <= 0:
            print("Not bad! It was a tie, but you should keep improving so it isn't one next time. ")
            exp_earned = 100
            player_exp + exp_earned