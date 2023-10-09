Gender = input("Is your character male?")
Gender = Gender.lower()
if Gender == "no":
    print("Your character is Black Widow")
else:
    Power = input("Does your character have Superpowers?")
    Power = Power.lower()
    if Power == "no":
        solo = input("Does your character have a solo film?")
        solo = solo.lower()
        if solo == "no":
            print("Your character is Hawkeye")
        else:
            print("Your character IronMan")
    else:
        shield = input("Does your character have a vibranium sheild?")
        shield = shield.lower()
        if shield == "yes" :
            print("Your character is Captain America")
        else:
            hammer = input("Does your character have a hammer")
            hammer = hammer.lower()
            if hammer == "yes" :
                print("Your character is Thor")
            else:
                print("Your character is Hulk!")
