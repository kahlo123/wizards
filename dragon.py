import random
class Dragon:
    def __init__(self, life_pt, mana_pt, atk_pt,def_pt,dodge_pt):
        self.life_pt = life_pt
        self.mana_pt = mana_pt
        self.atk_pt = atk_pt
        self.def_pt = def_pt
        self.dodge_pt = dodge_pt
    def dragonAttak(self, lp_wizard):
        print("Attaque de dragon")
        if random.randint(1,6) > 4:
            print("Le magicien a été touché !!!")
            return lp_wizard - self.atk_pt
        else:
            print("L'attaque à échoué !!")
            return lp_wizard
    def dragonDefense(self , attack_wizard):
        if random.randint(1,6) > 4:
            print("Le dragon se défend")
            return self.def_pt - attack_wizard
        else:
            print("Le dragon est touché !!")

            return attack_wizard
    def dragonDodge(self , wizard_atk):
        print("Le dragon essaye d'esquivé")
        if random.randint(1,6) > 4 and self.dodge_pt > 0:
            print("Le dragon à esquivé")
            self.dodge_pt -= 50
            return 0
        else:
            print("Le dragon n'a pas esquivé")
            return wizard_atk
    def dragonChoice(self):
        return str(random.randint(1,3))
    def showStat(self):
        print("             -------Dragon Stats-------")
        print("                  Life point " + str(self.life_pt))
        print("                  Mana point " + str(self.mana_pt))
        print("                  Attack point " + str(self.atk_pt))
        print("                  Defense point " + str(self.def_pt))
        print("                  Dodge point " + str(self.dodge_pt))
        print("             --------------------------")


