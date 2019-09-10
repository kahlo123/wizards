import wizard
import dragon
import random
import sys

w1 = wizard.Wizard(10, 10, 1000, 1000, 2000)
d1 = dragon.Dragon(10, 10, 1000, 1000, 2000)
endofWhile = False

w1.showStat()
d1.showStat()
while endofWhile != True:
    response = str(input("Que voulez vous faire ? \n 1 - Attaquer ; 2 - Prendre une potion ; 3 - Lancer un sort"))
    if response == "1":
        d1.life_pt = w1.wizardAttack(d1.life_pt)
        d1.showStat()
    elif response == "2":
        w1.takePotion()
    else:
        w1.launchSpell()

    if d1.life_pt < 0:
        endofWhile = True
        print("You win")

