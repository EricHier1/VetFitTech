import time
import sys
import random

def print_slow(text):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        #time.sleep(0.02)
    print("")

def start_game():
    print_slow("Welcome to the text-based adventure game!")
    print_slow("Inspired by Planescape: Torment, this game will take you on a journey through a world filled with strange creatures and environments.")
    character_creation()
    
def character_creation():
    print_slow("First, let's create your character.")
    name = input("What's your character's name? ")
    print_slow(f"Hello, {name}.")
    choose_class()

def choose_class():
    print_slow("Choose your character's class:")
    print_slow("1. Fighter")
    print_slow("2. Wizard")
    print_slow("3. Rogue")
    
    class_choice = input("Enter the number of your choice: ")
    if class_choice == "1":
        character_class = "Fighter"
    elif class_choice == "2":
        character_class = "Wizard"
    elif class_choice == "3":
        character_class = "Rogue"
    else:
        print_slow("Invalid choice. Please try again.")
        choose_class()
        return
    
    print_slow(f"You have chosen the {character_class} class.")
    starting_area()

def starting_area():
    print_slow("You find yourself in a dimly lit tavern.")
    print_slow("A mysterious figure approaches you and offers you a quest.")
    print_slow("Do you accept the quest? (Y/N)")
    choice = input().lower()
    if choice == 'y':
        print_slow("The mysterious figure gives you a map and a cryptic message.")
        first_decision()
    elif choice == 'n':
        print_slow("The mysterious figure disappears into the shadows.")
        print_slow("You decide to spend your days in the tavern, never knowing what adventure awaited you.")
        game_over()
    else:
        print_slow("Invalid choice. Please try again.")
        starting_area()

def first_decision():
    print_slow("You have the map and the cryptic message in hand.")
    print_slow("You leave the tavern and begin your adventure.")
    second_area()

def second_area():
    print_slow("You arrive at a crossroads. There are three paths before you.")
    print_slow("1. Head north towards a dense forest.")
    print_slow("2. Head east to a mountain pass.")
    print_slow("3. Head south to a murky swamp.")

    choice = input("Enter the number of your choice: ")

    if choice == "1":
        dense_forest()
    elif choice == "2":
        mountain_pass()
    elif choice == "3":
        swamp()
    else:
        print_slow("Invalid choice. Please try again.")
        second_area()

def dense_forest():
    print_slow("You venture into the dense forest.")
    print_slow("As you walk, you encounter a wounded traveler.")
    print_slow("Do you:")
    print_slow("1. Help the traveler.")
    print_slow("2. Ignore the traveler and continue.")

    choice = input("Enter the number of your choice: ")

    if choice == "1":
        help_traveler()
    elif choice == "2":
        print_slow("You ignore the traveler and continue your journey.")
        third_area()
    else:
        print_slow("Invalid choice. Please try again.")
        dense_forest()

def mountain_pass():
    print_slow("You traverse the treacherous mountain pass.")
    print_slow("A sudden avalanche blocks your path!")
    print_slow("Do you:")
    print_slow("1. Try to find another way around.")
    print_slow("2. Attempt to clear the path.")

    choice = input("Enter the number of your choice: ")

    if choice == "1":
        find_another_way()
    elif choice == "2":
        clear_path()
    else:
        print_slow("Invalid choice. Please try again.")
        mountain_pass()

def swamp():
    print_slow("You carefully navigate the murky swamp.")
    print_slow("A mysterious figure offers you a deal.")
    print_slow("Do you:")
    print_slow("1. Accept the deal.")
    print_slow("2. Decline the deal and continue.")

    choice = input("Enter the number of your choice: ")

    if choice == "1":
        accept_deal()
    elif choice == "2":
        decline_deal()
    else:
        print_slow("Invalid choice. Please try again.")
        swamp()

def help_traveler():
    print_slow("You decide to help the wounded traveler.")
    print_slow("The traveler is grateful and gives you a valuable item before leaving.")
    # You can add a function to handle adding the item to the player's inventory here.
    third_area()

def find_another_way():
    print_slow("You search for another way around the avalanche.")
    print_slow("After some time, you find a hidden path that leads you to your destination.")
    third_area()

def clear_path():
    print_slow("You attempt to clear the path, but it takes a significant amount of time and energy.")
    # You can add a function to handle reducing the player's health or energy here.
    third_area()

def accept_deal():
    print_slow("You accept the mysterious figure's deal.")
    print_slow("The figure gives you a powerful artifact but warns you of the consequences.")
    # You can add a function to handle adding the artifact to the player's inventory here.
    third_area()

def decline_deal():
    print_slow("You decline the mysterious figure's deal.")
    print_slow("The figure disappears into the shadows, leaving you to continue your journey.")
    third_area()

def third_area():
    print_slow("You find a hidden cave entrance. Do you enter?")
    print_slow("1. Yes")
    print_slow("2. No")

    choice = input("Enter the number of your choice: ")

    if choice == "1":
        hidden_cave()
    elif choice == "2":
        print_slow("You decide not to enter the cave and continue your journey.")
        fourth_area()
    else:
        print_slow("Invalid choice. Please try again.")
        third_area()

def hidden_cave():
    print_slow("You enter the hidden cave and find a sleeping dragon guarding a treasure chest.")
    print_slow("Do you:")
    print_slow("1. Attempt to sneak past the dragon and take the treasure.")
    print_slow("2. Leave the cave quietly, avoiding the dragon.")

    choice = input("Enter the number of your choice: ")

    if choice == "1":
        steal_treasure()
    elif choice == "2":
        print_slow("You leave the cave quietly, avoiding the sleeping dragon.")
        fourth_area()
    else:
        print_slow("Invalid choice. Please try again.")
        hidden_cave()

def steal_treasure():
    success = random.randint(0, 1)  # 50% chance of success
    if success:
        print_slow("You successfully sneak past the dragon and take the treasure.")
        # Add the treasure to the player's inventory here.
        fourth_area()
    else:
        print_slow("The dragon wakes up and attacks you!")
        dragon_battle()
        
def fourth_area():
    print_slow("You reach the final destination of your journey.")
    print_slow("A grand battle awaits you.")
    print_slow("You face a powerful enemy that blocks your path.")
    print_slow("Do you:")
    print_slow("1. Attempt to reason with the enemy.")
    print_slow("2. Prepare for battle.")

    choice = input("Enter the number of your choice: ")

    if choice == "1":
        reason_with_enemy()
    elif choice == "2":
        final_battle()
    else:
        print_slow("Invalid choice. Please try again.")
        fourth_area()

import random

def reason_with_enemy():
    success = random.randint(0, 1)  # 50% chance of success
    if success:
        print_slow("You successfully reason with the enemy, and they let you pass.")
        print_slow("Congratulations, you have completed the journey!")
    else:
        print_slow("The enemy is not interested in reasoning with you. The battle begins!")
        final_battle()

def final_battle():
    player_hp = 100  # Example player health, replace with actual player stats
    enemy_hp = 100  # Example enemy health
    player_attack = 20  # Example player attack, replace with actual player stats
    enemy_attack = 10  # Example enemy attack

    while player_hp > 0 and enemy_hp > 0:
        print_slow("Battle Menu:")
        print_slow("1. Attack")
        print_slow("2. Defend")
        print_slow("3. Use a potion")

        choice = input("Enter the number of your choice: ")

        if choice == "1":
            enemy_hp -= player_attack
            print_slow(f"You attacked the enemy for {player_attack} damage!")
        elif choice == "2":
            player_hp += 10  # Example defense value
            print_slow("You defended and regained 10 health!")
        elif choice == "3":
            player_hp += 30  # Example potion heal value
            print_slow("You used a potion and regained 30 health!")
        else:
            print_slow("Invalid choice. Please try again.")
            continue

        if enemy_hp <= 0:
            break

        player_hp -= enemy_attack
        print_slow(f"The enemy attacked you for {enemy_attack} damage!")

        if player_hp <= 0:
            print_slow("You have been defeated by the powerful enemy.")
            print_slow("Game Over.")
        else:
            print_slow("You have defeated the enemy in the grand battle!")
            print_slow("Congratulations, you have completed the journey!")



def dragon_battle():
    player_strength = 10  # Example player strength, replace with actual player stats
    dragon_strength = random.randint(8, 20)  # Example dragon strength

    if player_strength > dragon_strength:
        print_slow("You have defeated the dragon!")
        print_slow("You take the treasure and continue your journey.")
        # Add the treasure to the player's inventory here.
        fourth_area()
    else:
        print_slow("You have been defeated by the dragon.")
        print_slow("Game Over.")




def game_over():
    print_slow("Game Over.")
    play_again = input("Do you want to play again? (Y/N) ").lower()
    if play_again == 'y':
        start_game()
    elif play_again == 'n':
        print_slow("Thanks for playing! Goodbye!")
        sys.exit()
    else:
        print_slow("Invalid choice. Please try again.")
        game_over()

if __name__ == "__main__":
    start_game()
