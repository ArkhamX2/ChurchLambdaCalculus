from lib.hero import Hero
from lib.weapon import Weapon
from lib.armor import Armor, ArmorType
from lib.damage import Damage, DamageType
from lib.dice import Dice
from lib.race import Race
import random

randomNames = [
    "Kirill Smirnov",
    "Salazar Lizzard",
    "Richard Lion Heart",
    "Pier Baguet",
    "Toyama Tokanava",
    "Franceska DeBronko",
    "Gladiator9000",
    "Anonymous",
    "Silent Traveler"]

races = [
    Race("Human"),
    Race("Elf"),
    Race("Dwarf"),
    Race("Orc"),
    Race("Lizzard")
]


def init_heroes(numberOfHeroes: int):
    heroes = []

    while len(heroes) != numberOfHeroes:
        hero = Hero(
            randomNames[random.randint(0, len(randomNames) - 1)],
            random.randint(150, 180),
            random.randint(50, 100),
            races[random.randint(0, len(races) - 1)])
        if len(heroes) % 2 == 0:
            hero.strength += 1
        else:
            hero.agility += 1
        heroes.append(hero)

    return heroes


def init_arena(heroes: [Hero]):
    gladiator_sword = Weapon("Gladiator sword", Damage([Dice(6), Dice(4)]), DamageType.slashing, 50, 100)
    gladiator_spear = Weapon("Gladiator spear", Damage([Dice(4), Dice(4), Dice(4)]), DamageType.pircing, 70, 100)

    gladiator_armor = Armor("Gladiator armor", 11, ArmorType.Medium, True, 100, 100)

    for hero in heroes:
        hero.PickWeapon(gladiator_sword if hero.strength >= hero.agility else gladiator_spear)
        hero.PickArmor(gladiator_armor)


def checkIfAnybodyAlive(heroes: [Hero]):
    counter = 0
    for hero in heroes:
        if hero.health > 0:
            counter += 1
    return counter > 1;


def fight(heroes: [Hero]):
    while checkIfAnybodyAlive(heroes):
        print("_____________________________________________")
        for hero in heroes:
            if hero.health > 0:
                for opponent in heroes:
                    if opponent.health > 0 and hero!=opponent:
                        if hero.Attack(opponent.armor.defenceClass):
                            heroDamage = hero.DealDamage()
                            opponent.Health -= heroDamage
                            print(f"{hero.name}{hero.health} атакует {opponent.name}{opponent.health} и наносит {heroDamage} единиц урона")
                        else:
                            print(f"{hero.name}{hero.health} промахивается по {opponent.name}{opponent.health}")

                        if opponent.health <= 0:
                            print(f"{opponent.name}{opponent.health} побеждён")

                        break

    for hero in heroes:
        if hero.health > 0:
            return hero


if __name__ == '__main__':
    heroes = init_heroes(10)
    init_arena(heroes)
    for hero in heroes:
        print(hero)

    winner = fight(heroes)

    print(f"{winner.name} - победитель арены!")