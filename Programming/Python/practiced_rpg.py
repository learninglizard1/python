
#rpg game example
import os


os.system ('cls') #clear the screen for fresh display
name = input("Enter your name:").capitalize



player_class = {
    1: "Warrior",
    2: "Sorcerer",
    3: "Rogue"
}
warrior = {
    "Strength": 10,
    "Speed": 4,
    "Magic": 0
}

sorcerer = {
    "Strength": 2,
    "Speed": 6, 
    "Magic": 8
}

rogue = {
    "Strength": 4,
    "Speed": 8,
    "Magic": 2
}



print ("""
Select your player class:
1. Warrior
2. Sorcerer 
3. Rogue
""")

while True:
    choice = input("Choose a class:").strip()

    if choice == "" or choice.isalpha():
        print ("Invalid! Enter a number between 1 to 3")
        continue

    elif choice == "1":
        os.system ('cls')#clear the screen for fresh display
        print (f"""
Name: {name}
Class: {player_class[1]}
Description:{name} most powerful {player_class[1]} in tribe! {name} seeks challengers to test his might! {name} travel to gain glory!
Strength: {warrior['Strength']}
Speed: {warrior['Speed']}
Magic: {warrior['Magic']}
    """)
        break
        

    elif choice == "2":
        os.system ('cls')#clear the screen for fresh display
        print (f"""
Name: {name}
Class: {player_class[2]}
Description:{name} most powerful {player_class[2]} in tribe! {name} seeks challengers to test their mana and power! {name} travel to gain glory!
Strength: {sorcerer['Strength']}
Speed: {sorcerer['Speed']}
Magic: {sorcerer['Magic']}
    """)
        break

    elif choice == "3":
        os.system ('cls') #clear the screen for fresh display
        print (f"""
Name: {name}
Class: {player_class[3]}
Description:{name} most powerful {player_class[3]} in tribe! {name} seeks challengers to test their agility! {name} travel to gain glory!
Strength: {rogue['Strength']}
Speed: {rogue['Speed']}
Magic: {rogue['Magic']}
    """)
        break

    else:
        print ("Please pick a number between 1 to 3.")
        continue



