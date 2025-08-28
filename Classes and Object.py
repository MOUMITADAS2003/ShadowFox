#  1.Avengers is a Marvel’s American Superheroes team, Now you want to
#  showcase your programming skills by representing the Avengers team using
#  classes. Create a class called Avenger and create these six superheroes using this
#  class. 


# Defining the Avenger class
class Avenger:
    def __init__(self, name, superpower, weapon):
        self.name = name
        self.superpower = superpower
        self.weapon = weapon

    def display_info(self):
        print(f"Name: {self.name}")
        print(f"Superpower: {self.superpower}")
        print(f"Weapon: {self.weapon}")
        print("-" * 30)


# Creating Avengers objects
captain_america = Avenger("Captain America", "Enhanced strength, agility", "Vibranium Shield")
iron_man = Avenger("Iron Man", "Genius intellect, powered armor suit", "Arc Reactor Suit")
black_widow = Avenger("Black Widow", "Expert spy, martial artist", "Electro-shock batons")
hulk = Avenger("Hulk", "Superhuman strength, regeneration", "His Rage")
thor = Avenger("Thor", "God of Thunder, immortality", "Mjolnir (Hammer)")
hawkeye = Avenger("Hawkeye", "Expert archer, precision shooting", "Bow and Arrows")

# Displaying information
avengers_team = [captain_america, iron_man, black_widow, hulk, thor, hawkeye]

print("Avengers Team Roster:\n")
for avenger in avengers_team:
    avenger.display_info()



 
#  2. super_heroes = ["Captain America", "Iron Man", "Black Widow", "Hulk",
#  "Thor", "Hawkeye"] 



# Avenger class
class Avenger:
    def __init__(self, name):
        self.name = name
    
    def display_info(self):
        print(f"Avenger: {self.name}")


# List of superheroes
super_heroes = ["Captain America", "Iron Man", "Black Widow", "Hulk", "Thor", "Hawkeye"]

# Creating Avenger objects dynamically
avengers_team = [Avenger(hero) for hero in super_heroes]

# Displaying info
print("Avengers Team:\n")
for avenger in avengers_team:
    avenger.display_info()





# 3. Your Avenger class should have these properties: 
# 1. Name 
# 2. Age 
# 3. Gender 
# 4. Super Power 
# 5. Weapon 



# Defining the Avenger class
class Avenger:
    def __init__(self, name, age, gender, super_power, weapon):
        self.name = name
        self.age = age
        self.gender = gender
        self.super_power = super_power
        self.weapon = weapon

    def display_info(self):
        print(f"Name       : {self.name}")
        print(f"Age        : {self.age}")
        print(f"Gender     : {self.gender}")
        print(f"Super Power: {self.super_power}")
        print(f"Weapon     : {self.weapon}")
        print("-" * 40)


# Creating Avenger objects with details
captain_america = Avenger("Captain America", 100, "Male", "Enhanced strength, agility", "Vibranium Shield")
iron_man = Avenger("Iron Man", 48, "Male", "Genius intellect, powered armor suit", "Arc Reactor Suit")
black_widow = Avenger("Black Widow", 35, "Female", "Expert spy, martial artist", "Electro-shock batons")
hulk = Avenger("Hulk", 40, "Male", "Superhuman strength, regeneration", "His Rage")
thor = Avenger("Thor", 1500, "Male", "God of Thunder, immortality", "Mjolnir (Hammer)")
hawkeye = Avenger("Hawkeye", 41, "Male", "Expert archer, precision shooting", "Bow and Arrows")

# List of Avengers
avengers_team = [captain_america, iron_man, black_widow, hulk, thor, hawkeye]

# Displaying all Avengers info
print("Avengers Team Roster:\n")
for avenger in avengers_team:
    avenger.display_info()




# 4. Captain America has Super strength, Iron Man has Technology, Black Widow
#  is superhuman, Hulk has Unlimited Strength, Thor has super Energy and
#  Hawkeye has fighting skills as superpowers. 




# Avenger class
class Avenger:
    def __init__(self, name, age, gender, super_power, weapon):
        self.name = name
        self.age = age
        self.gender = gender
        self.super_power = super_power
        self.weapon = weapon

    def display_info(self):
        print(f"Name       : {self.name}")
        print(f"Age        : {self.age}")
        print(f"Gender     : {self.gender}")
        print(f"Super Power: {self.super_power}")
        print(f"Weapon     : {self.weapon}")
        print("-" * 40)


# Creating Avengers with given superpowers
captain_america = Avenger("Captain America", 100, "Male", "Super Strength", "Vibranium Shield")
iron_man = Avenger("Iron Man", 48, "Male", "Technology", "Arc Reactor Suit")
black_widow = Avenger("Black Widow", 35, "Female", "Superhuman", "Electro-shock batons")
hulk = Avenger("Hulk", 40, "Male", "Unlimited Strength", "His Rage")
thor = Avenger("Thor", 1500, "Male", "Super Energy", "Mjolnir (Hammer)")
hawkeye = Avenger("Hawkeye", 41, "Male", "Fighting Skills", "Bow and Arrows")

# List of Avengers
avengers_team = [captain_america, iron_man, black_widow, hulk, thor, hawkeye]

# Displaying all Avengers info
print("Avengers Team Roster:\n")
for avenger in avengers_team:
    avenger.display_info()




# 5. Weapons: Shield, Armor, Batons, No Weapon for hulk, Mjölnir, Bow, and
#  Arrows 


# Avenger class
class Avenger:
    def __init__(self, name, age, gender, super_power, weapon):
        self.name = name
        self.age = age
        self.gender = gender
        self.super_power = super_power
        self.weapon = weapon

    def display_info(self):
        print(f"Name       : {self.name}")
        print(f"Age        : {self.age}")
        print(f"Gender     : {self.gender}")
        print(f"Super Power: {self.super_power}")
        print(f"Weapon     : {self.weapon}")
        print("-" * 40)


# Creating Avengers with superpowers & weapons
captain_america = Avenger("Captain America", 100, "Male", "Super Strength", "Shield")
iron_man = Avenger("Iron Man", 48, "Male", "Technology", "Armor")
black_widow = Avenger("Black Widow", 35, "Female", "Superhuman", "Batons")
hulk = Avenger("Hulk", 40, "Male", "Unlimited Strength", "No Weapon")
thor = Avenger("Thor", 1500, "Male", "Super Energy", "Mjölnir")
hawkeye = Avenger("Hawkeye", 41, "Male", "Fighting Skills", "Bow and Arrows")

# List of Avengers
avengers_team = [captain_america, iron_man, black_widow, hulk, thor, hawkeye]

# Displaying Avengers info
print("Avengers Team Roster:\n")
for avenger in avengers_team:
    avenger.display_info()




# 6. Create methods to get the information about each superhero


# Avenger class
class Avenger:
    def __init__(self, name, age, gender, super_power, weapon):
        self.name = name
        self.age = age
        self.gender = gender
        self.super_power = super_power
        self.weapon = weapon

    # Getter methods
    def get_name(self):
        return self.name

    def get_age(self):
        return self.age

    def get_gender(self):
        return self.gender

    def get_super_power(self):
        return self.super_power

    def get_weapon(self):
        return self.weapon

    # Display all info
    def display_info(self):
        print(f"Name       : {self.get_name()}")
        print(f"Age        : {self.get_age()}")
        print(f"Gender     : {self.get_gender()}")
        print(f"Super Power: {self.get_super_power()}")
        print(f"Weapon     : {self.get_weapon()}")
        print("-" * 40)


# Creating Avengers
captain_america = Avenger("Captain America", 100, "Male", "Super Strength", "Shield")
iron_man = Avenger("Iron Man", 48, "Male", "Technology", "Armor")
black_widow = Avenger("Black Widow", 35, "Female", "Superhuman", "Batons")
hulk = Avenger("Hulk", 40, "Male", "Unlimited Strength", "No Weapon")
thor = Avenger("Thor", 1500, "Male", "Super Energy", "Mjölnir")
hawkeye = Avenger("Hawkeye", 41, "Male", "Fighting Skills", "Bow and Arrows")

# List of Avengers
avengers_team = [captain_america, iron_man, black_widow, hulk, thor, hawkeye]

# Display info for each Avenger
print("Avengers Team Roster:\n")
for avenger in avengers_team:
    avenger.display_info()

# Example of using individual getter methods
print("🔹 Example: Accessing single hero's details")
print(f"{iron_man.get_name()} uses {iron_man.get_weapon()} and his power is {iron_man.get_super_power()}.")





# 7. Create a method is_leader() which will tell if the superhero is a leader or not. 



# Avenger class
class Avenger:
    def __init__(self, name, age, gender, super_power, weapon):
        self.name = name
        self.age = age
        self.gender = gender
        self.super_power = super_power
        self.weapon = weapon

    # Getter methods
    def get_name(self):
        return self.name

    def get_age(self):
        return self.age

    def get_gender(self):
        return self.gender

    def get_super_power(self):
        return self.super_power

    def get_weapon(self):
        return self.weapon

    # Display all info
    def display_info(self):
        print(f"Name       : {self.get_name()}")
        print(f"Age        : {self.get_age()}")
        print(f"Gender     : {self.get_gender()}")
        print(f"Super Power: {self.get_super_power()}")
        print(f"Weapon     : {self.get_weapon()}")
        print(f"Leader     : {'Yes' if self.is_leader() else 'No'}")
        print("-" * 40)

    # Method to check if Avenger is leader
    def is_leader(self):
        return self.name == "Captain America"


# Creating Avengers
captain_america = Avenger("Captain America", 100, "Male", "Super Strength", "Shield")
iron_man = Avenger("Iron Man", 48, "Male", "Technology", "Armor")
black_widow = Avenger("Black Widow", 35, "Female", "Superhuman", "Batons")
hulk = Avenger("Hulk", 40, "Male", "Unlimited Strength", "No Weapon")
thor = Avenger("Thor", 1500, "Male", "Super Energy", "Mjölnir")
hawkeye = Avenger("Hawkeye", 41, "Male", "Fighting Skills", "Bow and Arrows")

# List of Avengers
avengers_team = [captain_america, iron_man, black_widow, hulk, thor, hawkeye]

# Display info for each Avenger
print("Avengers Team Roster:\n")
for avenger in avengers_team:
    avenger.display_info()

# Example usage of is_leader
print("🔹 Checking leadership status:")
for avenger in avengers_team:
    print(f"{avenger.get_name()} - Leader? {'Yes' if avenger.is_leader() else 'No'}")
