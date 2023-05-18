def main_menu_gui():
    while True:
        main_menu = input("Kai and Owen Productions Presents: Punch-A-Looza!  Choices: Play/Credits/Tutorial ")
        if main_menu == "Credits":
            credits = input("Main Developers: Kai and Owen Productions  Teacher: Mr. Whalen  Side Contributors: Yan Sharma  People we USED to copy from: Gabe Liberov and Yizhak Zoltan  Choices: Back ")

            if credits == 'Back':
                continue

            else:
                print("That's not a choice kid... ")
                continue
            
        if main_menu == "Tutorial":
            tutorial = input("The concept of this game is rather simple. You can use 6 different attacks that can be blocked with their corresponding blocks(e.g. Jabs will be blocked by the move Block Jab). You will be using these attacks and defenses in turns to avoid any exploits and spamming. Everytime you attack you will lose stamina which can be replenished by resting. However, resting will result in sacrificing your turn. That's really all there is to this game, so go out there and becoming the next boxing star of the world!  Choices: Back ")
            
            if tutorial == 'Back':
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