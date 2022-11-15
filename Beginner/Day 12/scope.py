####### Scope ########

# enemies = 1
#
# def increase_enemies():
#     enemies = 2
#     print(f"enemies inside function: {enemies}")
#
#
# increase_enemies()
# print(f"enemies outside function: {enemies}")

# Local scope

#
# def drink_potion():
#     potion_strength = 2
#     print(potion_strength)
#
#
# drink_potion()
#
# # Global scope
# player_health = 10
#
#
# def drink_potion_2():
#     potion_strength = 2
#     print(player_health)
#
#
# drink_potion_2()
#
#
# # There is no Block Scope
#
# game_level = 3
# enemy = ["Skeleton", "Zombie", "Alien"]
#
# if game_level < 5:
#     new_enemy = enemy[0]
#
# print(new_enemy)
#
# # Modifying Global Scope
#
# enemies = 1
#
#
# def increase_enemies():
#     # global enemies
#     # enemies = 2
#     print(f"enemies inside function: {enemies}")
#     return enemies + 1
#
#
# increase_enemies()
# print(f"enemies outside function: {enemies}")

# Global Constants

PI = 3.1419
URL = "https://www.google.com"

