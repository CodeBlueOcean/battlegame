'''
Dragon Battle Game
'''
def main():
    wizard = "Wizard"
    elf = "Elf"
    human = "Human"
    orc = "Orc"
    end_game = "End Game"

    wizard_hp = 70
    elf_hp = 100
    human_hp = 200
    orc_hp = 90
    dragon_hp = 300

    wizard_damage = 150
    elf_damage = 100
    human_damage = 20
    orc_damage = 105
    dragon_damage = 50

    character_list = [wizard, elf, human, orc, end_game]

    for i, value in enumerate(character_list, 1):
        print("{}.) {}".format(i, value))

    character = (int(input("\nSelect A Number To Choose Your Character:")))

    while True:
        if character == 1:
            character = wizard
            my_hp = wizard_hp
            my_damage = wizard_damage
            break
        if character == 2:
            character = elf
            my_hp = elf_hp
            my_damage = elf_damage
            break
        if character == 3:
            character = human
            my_hp = human_hp
            my_damage = human_damage
            break
        # bonus 3
        if character == 4:
            character = orc
            my_hp = orc_hp
            my_damage = orc_damage
            break
        # bonus 4
        if character == 5:
            print("\nLosing Power. Maybe try again next time.\n")
            quit()
            break
        print("Unknown character")

    print(f"\nYou have chosen the character: {character}.")
    print("Health:", my_hp)
    print("Damage:", my_damage)

    while True:
        dragon_hp = dragon_hp - my_damage
        print(f"\nThe {character} damaged the Dragon!")
        if dragon_hp > 0:
            print(f"The dragon has {dragon_hp}left.\n")
        if dragon_hp <= 0:
            print(
                f"The Dragon has lost the battle. {character} wins! and {dragon_hp}left\n")
            break
        my_hp = my_hp-dragon_damage
        print(
            f"\nThe Dragon damaged the {character}! You have {my_hp} left!\n")
        if my_hp <= 0:
            print(f"The {character} has lost the battle.\n")
            break
        # bonus 5
        again = input("Do you want to play gain? Type, yes or no :")
        # made str input case insensitive
        if again.casefold() == "yes":
            main()
        else:
            quit()


main()
