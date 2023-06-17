print("Welcome to my second game!")
name = input("What is your name? ")
age = input("What is your age? ")

health = 10

if int(age) >= 18:
  print("You are old enough to play! ")
  wants_to_play = input("Do you want to play? [yes|no] ").lower()
  if wants_to_play == "yes" or "y" or "okay":
    print("Let's play!")
    print("You are starting with", health, "health")

    left_or_right = input("First choice: Left or Right? [left|right] ").lower()
    if left_or_right == "left":
      ans = input(
        "Nice, you follow the path and reach a lake, Do you swim across or go around [across/around] "
      ).lower()
      if ans == "around":
        print("You went around and reached the other side of the lake")
      elif ans == "across":
        print(
          "You managed to get across, but were bit by a fish and lost 5 health"
        )
        health -= 5
        print("You have", health, "health left ")
        ans = input(
          "You noticed a house and a river. Which do you go to? [river/house] "
        )
        if ans == "house":
          print(
            "You go to the house and are gretted by the onwer... He doesn't like you and you lose 5 health "
          )
          health -= 5
          print("You have", health, " health left")
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
