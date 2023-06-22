print("Welcome to my second game!")
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
        print("Let's play!")
        print("You are starting with", health, "health")

        left_or_right = input("First choice: Left or Right? [left|right] ").lower()
        if left_or_right == "left":
            ans = input("Nice, you follow the path and reach a lake. Do you swim across or go around [across/around] ").lower()
            if ans == "around":
                print("You went around and reached the other side of the lake")
            elif ans == "across":
                print("You managed to get across, but were bit by a fish and lost 5 health")
                health -= 5
                print("You have", health, "health left ")

                # Check if the player wants to acquire an item
                acquire = input("Do you want to search for items? [yes|no] ").lower()
                if acquire in ["yes", "y", "okay"]:
                    health = acquire_item(health)  # Call the item acquisition function

                ans = input("You noticed a house and a river. Which do you go to? [river/house] ")
                if ans == "house":
                    print("You go to the house and are greeted by the owner... He doesn't like you and you lose 5 health ")
                    health -= 5
                    print("You have", health, "health left")
                    if health <= 0:
                        print("You now have 0 health and you lost the game... ")
                    else:
                        print("You have survived... You win! ")
                else:
                    print("You fell in the river and lose. ")
            else:
                print("You lost. ")

        else:
            print("You fell down and lost... ")

    else:
        print("Cya... ")
else:
    print("You are not old enough to play... ")
