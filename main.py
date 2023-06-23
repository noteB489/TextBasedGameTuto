print("Welcome to the Fantasy World!")
name = input("What is your name? ")
age = input("What is your age? ")

health = 10
items = [
    {
        "name": "Healing Potion",
        "effect": 5
    },
    {
        "name": "Dragon Scale Armor",
        "effect": 10
    },
    {
        "name": "Amulet of Protection",
        "effect": "prevent"
    },
]

def acquire_item(health):
    print("You found an item! Choose one to acquire:")
    for i, item in enumerate(items):
        print(f"{i + 1}. {item['name']}")

    choice = int(input("Enter the number of the item you want: ")) - 1

    if items[choice]["effect"] == "prevent":
        print("Congratulations! The item protects you from the next bad effect.")
    else:
        health += items[choice]["effect"]
        print(f"You acquired {items[choice]['name']} and gained {items[choice]['effect']} health.")

    return health

if int(age) >= 18:
    print("You are old enough to play! ")
    wants_to_play = input("Do you want to play? [yes|no] ").lower()
    if wants_to_play in ["yes", "y", "okay"]:
        print("Welcome,", name + "! Let the adventure begin!")
        print("You find yourself in a mysterious world filled with magic and fantasy creatures.")
        print("You suddenly realize that you have been transported to a realm beyond imagination.")
        print("You are starting with", health, "health.")

        left_or_right = input("As you explore, you come across a forked path. Will you go left or right? [left/right] ").lower()
        if left_or_right == "left":
            ans = input("You follow the path and reach a beautiful lake. Do you swim across or go around? [across/around] ").lower()
            if ans == "around":
                print("You decide to go around and reach the other side of the lake.")
            elif ans == "across":
                print("You manage to swim across, but a mischievous water sprite bites you, and you lose 5 health.")
                health -= 5
                print("You have", health, "health left.")

                # Check if the player wants to acquire an item
                acquire = input("While exploring further, you stumble upon a hidden chest. Do you want to search for items? [yes/no] ").lower()
                if acquire in ["yes", "y", "okay"]:
                    health = acquire_item(health)  # Call the item acquisition function

                ans = input("You notice a house and a river nearby. Which do you go to? [house/river] ")
                if ans == "house":
                    print("You approach the house and are greeted by a grumpy old wizard. He doesn't like visitors, and you lose 5 health.")
                    health -= 5
                    print("You have", health, "health left.")
                    if health <= 0:
                        print("You now have 0 health, and the wizard's magic overwhelms you... You have lost the game.")
                    else:
                        print("Despite the wizard's hostility, you manage to survive and prove your worth. Congratulations, you win!")
                else:
                    print("As you step into the river, you are caught in a strong current. The river carries you away, and you lose the game.")
            else:
                print("You hesitate for too long and lose your way. You are now lost in the unknown.")

        else:
            print("As you take a step to the right, the ground beneath you collapses, and you fall into a deep abyss. You have lost the game.")

    else:
        print("Maybe another time then... Farewell,", name + "!")
else:
    print("I'm sorry, but you are not old enough to embark on this adventure. Come back when you are older!")
