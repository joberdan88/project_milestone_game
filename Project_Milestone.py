"""
Adventure Game:
- Added three levels of choices with unique scenarios and outcomes.
- Included hidden choices and trick questions to enhance the complexity and creativity of the game.
"""

def adventure_game():
      # Step 1: Initial Scenario
      print("You are walking through a dark forest and find two items:a MATCH and a\n"
      "FLASHLIGHT.")
      step_1 = input("Which one do you want to pick up? ").lower()

      print()          

      # Step 2: Consequence of the Initial Choice
      if step_1 == "match":
            print("You pick up the match and strike it, and for a instant, the forest\n"
            "around you is illuminated. You see a large grizzly bear, and then the\n"
            "burns out.") 
            step_2 = input("Do you want to RUN, or HIDE behind a tree? ").lower()

            if step_2 == "run":
                  print("You are running screaming, the bear heard you, gets angry\n"
                  "and runs after. The bear is very fast, it approaches you but when\n"
                  "you realize it is close you scream even louder and run faster.")
                  step_3 = input("You see two path options: a BRIDGE and a RIVER, which\n"
                  "one do you choose? ").lower()
                  if step_3 == "bridge":
                        print("You run across the bridge but it falls down. Game Over!")
                  elif step_3 == "river":
                        print("You swim across the river and reach a safe place.\n"
                        "Congratulations!")
                  else:
                        print("Please enter with a valid option.")


            elif step_2 == "hide":
                  print("You hide behind a tree but the bears smells you and finds you.\n"
                  "Game Over!")
            else: 
                  print("Please enter with a valid option.")

      elif step_1 == "flashlight":
            print("You pick up the flashlight and turn it on. You see the pathway lit up\n"
            "in front of you, but you thought you also heard something off to the side.\n")
            step_2a = input("Do you want to FOLLOW the path or LOOK in the trees for\n"
            "the thing that the noise? ").lower()
            if step_2a == "follow":
                  print("You follow the path but halfway there an angry wolf appears and\n"
                  "catches you. Game Over!")
            elif step_2a == "look":
                  print("You look in the trees, and see a pair of glowing eyes, an angry\n"
                  "wolf appears, you get so scared you faint. The wolf smells you, thinks\n"
                  "you're dead, and leaves.")
                  step_3a = input("You wake up and decide to continue. Do you want.\n"
                  "Do you want to FOLLOW the path or SEARCH for shelter? ")
                  if step_3a == "follow":
                        print("You follow the path and find a safe cabin. Congratulations!")
                  elif step_3a == "search":
                        print("You search for shelter but get lost and the wolf finds you.\n"
                        "Game Over!")
                  else:
                        print("Please enter with a valid option.")
            else:
                  print("Please enter with a valid option.")

      else: print("Please enter with a valid option.")

adventure_game() 


"""
Adventure Game Design
Initial Scenario:
Prompt: You are walking through a dark forest and find two items: a MATCH and a FLASHLIGHT. Which one do you want to pick up?

- Choices: MATCH, FLASHLIGHT


If the user chooses "MATCH":
Prompt: You pick up the match and strike it, and for an instant, the forest around you is illuminated. You see a large grizzly bear, and then the match burns out. Do you want to RUN, or HIDE behind a tree?

- Choices: RUN, HIDE

If the user chooses "RUN":
Prompt: You are running and screaming, the bear hears you, gets angry and runs after you. The bear is very fast, it approaches you but when you realize it is close, you scream even louder and run faster. You see two path options: a BRIDGE and a RIVER. Which one do you choose?

- Choices: BRIDGE, RIVER

If the user chooses "BRIDGE":
Response: You run across the bridge but it collapses. Game Over!

If the user chooses "RIVER":
Response: You swim across the river and reach a safe place. Congratulations!


If the user chooses "HIDE":
Response: You hide behind a tree, but the bear smells you and finds you. Game Over!


If the user chooses "FLASHLIGHT":
Prompt: You pick up the flashlight and turn it on. You see the pathway lit up in front of you, but you thought you also heard something off to the side. Do you want to FOLLOW the path or LOOK in the trees for the thing that made the noise?

- Choices: FOLLOW, LOOK

If the user chooses "FOLLOW":
Response: You follow the path but halfway there an angry wolf appears and catches you. Game Over!

If the user chooses "LOOK":
Prompt: You look in the trees and see a pair of glowing eyes. An angry wolf appears, you get so scared you faint. The wolf smells you, thinks you're dead, and leaves. You wake up and decide to continue. Do you want to FOLLOW the path or SEARCH for shelter?

- Choices: FOLLOW, SEARCH

If the user chooses "FOLLOW":
Response: You follow the path and find a safe cabin. Congratulations!

If the user chooses "SEARCH":
Response: You search for shelter but get lost and the wolf finds you. Game Over!
"""
