import wizard
import dragon
import random
import sys

w1 = wizard.Wizard(100, 200, 100, 100, 200)
d1 = dragon.Dragon(100, 200, 100, 100, 200)
endofWhile = False

w1.showStat()
d1.showStat()
while endofWhile != True:
    response = str(input("Que voulez vous faire ? \n 1 - Attaquer ; 2 - Prendre une potion ; 3 - Lancer un sort"))
    if response == "1":
        if d1.dragonChoice() == "1":
            d1.life_pt = d1.life_pt - d1.dragonDefense(w1.atk_pt)
        elif d1.dragonChoice() == "2":
            if d1.dragonDodge():
                d1.life_pt = w1.wizardAttack(d1.life_pt)
        else:
            print("Le dragon ne fait rien")
            d1.life_pt = w1.wizardAttack(d1.life_pt)
    elif response == "2":
        w1.takePotion()
    else:
        w1.launchSpell()

    w1.life_pt = d1.dragonAttak(w1.life_pt)
    w1.showStat()

    if d1.life_pt < 0:
        endofWhile = True
        print("You win")
    elif w1.life_pt < 0 or w1.mana_pt < 0:
        endofWhile = True
        print("You loose")

