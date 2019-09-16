import wizard
import dragon
import random
import sys

w1 = wizard.Wizard(500, 500, 100, 100, 200,3)
d1 = dragon.Dragon(500, 200, 100, 100, 200)
endofWhile = False

w1.showStat()
# d1.showStat()
while endofWhile != True:
    ##Tour du wizard
    response = str(input("Que voulez vous faire ? \n 1 - Attaquer ; 2 - Prendre une potion ; 3 - Lancer un sort"))
    if response == "1":
        if d1.dragonChoice() == "1":
            d1.life_pt = d1.life_pt - d1.dragonDefense(w1.atk_pt)
            d1.showStat()
        elif d1.dragonChoice() == "2":
            d1.life_pt = d1.life_pt - d1.dragonDodge(w1.atk_pt)
            d1.showStat()
        else:
            d1.life_pt = w1.wizardAttack(d1.life_pt)
            print("Le dragon ne fait rien")
            d1.showStat()
    elif response == "2":
        w1.takePotion()
        w1.showStat()
    else:
        w1.launchSpell()
        w1.showStat()

## Vérifie si les deux adversaire sont toujours debout
    if d1.life_pt <= 0:
        endofWhile = True
        print("You win")
        break
    elif w1.life_pt < 0 or w1.mana_pt < 0:
        endofWhile = True
        print("You loose")
        break



    ##Tour du dragon
    print("Le dragon attaque")
    response = str(input("Que voulez vous faire ? \n 1 - Se défendre; 2 - Esquivé; 3 - Prendre une potion"))
    if response == "1":
        w1.life_pt = w1.life_pt - w1.wizardDefense(d1.atk_pt)
        w1.showStat()
    elif response == "2":
        w1.life_pt = w1.life_pt - w1.wizardDefense(d1.atk_pt)
        w1.showStat()
    else:
        w1.takePotion()
        w1.life_pt
        w1.showStat()

        ## Vérifie si les deux adversaire sont toujours debout
        if d1.life_pt <= 0:
            endofWhile = True
            print("You win")
            break
        elif w1.life_pt < 0 or w1.mana_pt < 0:
            endofWhile = True
            print("You loose")
            break