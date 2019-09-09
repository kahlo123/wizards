import wizard
import dragon
import sys

w1 = wizard.Wizard(10, 10, 1000, 1000, 2000)
endofWhile = False
while endofWhile != True:
    response = str(input("Que voulez vous faire ? \n 1 - Attaquer ; 2 - Prendre une potion ; 3 - Lancer un sort"))
    if response == "1":
        w1.atk_pt
    elif response == "2":
        w1.takePotion()
    else:
        w1.launchSpell()

