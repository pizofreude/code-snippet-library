# # A base class for all enemies
# class Enemy:
#     def move(self):
#         print("Moving")

#     def attack(self):
#         print("Attacking")

#     def die(self):
#         print("Dying")

# # A subclass of Enemy for tanks
# class Tank(Enemy):
#     def move(self):
#         print("Enemy incoming with a tank!")

#     def attack(self):
#         print("Enemy attacking with a tank")

#     def die(self):
#         print("Enemy's tank exploded and died")

#     # Add the health attribute
#     health = 100

# # A subclass of Enemy for soldiers
# class Soldier(Enemy):
#     def move(self):
#         print("Enemies foot soldiers are on the move!")

#     def attack(self):
#         print("Foot soldiers attacking with a gun")

#     def die(self):
#         print("Dying like a soldier")

#     # Add the health attribute
#     health = 50

# # A class for the player
# class Player(Enemy):
#     def __init__(self, health, attack_power):
#         self.health = health
#         self.attack_power = attack_power

#     def move(self):
#         print("I'm moving like a pro player")

#     def attack(self, enemy):
#         enemy.health -= self.attack_power
#         if enemy.health <= 0:
#             enemy.die()

#     def die(self):
#         print("Dying like a player")

# def main():
#     # Create a tank enemy
#     tank = Tank()

#     # Create a soldier enemy
#     soldier = Soldier()

#     # Create a player
#     player = Player(100, 20)

#     # Move the tank and soldier
#     tank.move()
#     soldier.move()

#     # Attack the tank and soldier
#     player.attack(tank)
#     player.attack(soldier)

#     # Kill the tank and soldier
#     tank.die()
#     soldier.die()

# if __name__ == "__main__":
#     main()


# A base class for all enemies
class Enemy:
    def move(self):
        print("Moving")

    def attack(self):
        print("Attacking")

    def die(self):
        print("Dying")

# A subclass of Enemy for tanks
class Tank(Enemy):
    def move(self):
        print("Enemy incoming with a tank!")

    def attack(self):
        print("Enemy attacking with a tank")

    def die(self):
        print("Enemy's tank exploded and died")

    # Add the health attribute
    health = 100

# A subclass of Enemy for soldiers
class Soldier(Enemy):
    def move(self):
        print("Enemies foot soldiers are on the move!")

    def attack(self):
        print("Foot soldiers attacking with a gun")

    def die(self):
        print("Foot soldiers died like a toy soldier...")

    # Add the health attribute
    health = 50

# A class for the player
class Player(Enemy):
    def __init__(self, health, attack_power):
        self.health = health
        self.attack_power = attack_power

    def move(self):
        print("I'm moving like a pro player")

    def attack(self, enemy):
        print(f"I attacked the enemy with my {self.attack_power} power!")
        enemy.health -= self.attack_power
        if enemy.health <= 0:
            enemy.die()

    def die(self):
        print("Dying like a player")

def main():
    # Create a tank enemy
    tank = Tank()

    # Create a soldier enemy
    soldier = Soldier()

    # Create a player
    player = Player(100, 20)

    # Move the tank and soldier
    tank.move()
    soldier.move()

    # Attack the tank and soldier
    print("I'm attacking the enemy tank!")
    player.attack(tank)
    print("I'm attacking the enemy foot soldiers!")
    player.attack(soldier)

    # Kill the tank and soldier
    print("The enemy tank exploded and died!")
    tank.die()
    print("The enemy foot soldiers died!")
    soldier.die()

    print("I won the game!")

if __name__ == "__main__":
    main()
