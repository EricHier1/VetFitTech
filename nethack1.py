import random

# Define constants for the game
WORLD_SIZE = 10
PLAYER_START_HEALTH = 20
MAX_ENEMY_HEALTH = 10
MAX_FOOD_HEALTH = 5

# Define the player character and their starting position
player = {
    "health": PLAYER_START_HEALTH,
    "x": WORLD_SIZE // 2,
    "y": WORLD_SIZE // 2,
}

# Define a list of enemies and their starting positions
enemies = []
for i in range(5):
    enemy = {
        "health": random.randint(1, MAX_ENEMY_HEALTH),
        "x": random.randint(0, WORLD_SIZE - 1),
        "y": random.randint(0, WORLD_SIZE - 1),
    }
    enemies.append(enemy)

# Define a list of food items and their starting positions
food = []
for i in range(5):
    item = {
        "health": random.randint(1, MAX_FOOD_HEALTH),
        "x": random.randint(0, WORLD_SIZE - 1),
        "y": random.randint(0, WORLD_SIZE - 1),
    }
    food.append(item)

# Define a function to print the game world to the console
def print_world():
    for y in range(WORLD_SIZE):
        for x in range(WORLD_SIZE):
            if x == player["x"] and y == player["y"]:
                print("@", end="")
            elif any(enemy["x"] == x and enemy["y"] == y for enemy in enemies):
                print("E", end="")
            elif any(item["x"] == x and item["y"] == y for item in food):
                print("F", end="")
            else:
                print(".", end="")
        print()

# Define the game loop
while player["health"] > 0:
    print_world()
    print(f"You have {player['health']} health.")
    move = input("Move (w/a/s/d): ")
    if move == "w":
        player["y"] -= 1
    elif move == "a":
        player["x"] -= 1
    elif move == "s":
        player["y"] += 1
    elif move == "d":
        player["x"] += 1
    else:
        print("Invalid move.")
        continue

    # Check for collisions with enemies and food
    for enemy in enemies:
        if enemy["x"] == player["x"] and enemy["y"] == player["y"]:
            player["health"] -= enemy["health"]
            enemies.remove(enemy)
            print(f"You lost {enemy['health']} health.")
            break
    for item in food:
        if item["x"] == player["x"] and item["y"] == player["y"]:
            player["health"] += item["health"]
            food.remove(item)
            print(f"You gained {item['health']} health.")
            break

print("Game over.")
