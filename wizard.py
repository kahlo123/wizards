import random
class Wizard:
    def __init__(self,name, life_pt, mana_pt, atk_pt,def_pt,dodge_pt, potion):
        self.name = name
        self.life_pt = life_pt
        self.mana_pt = mana_pt
        self.atk_pt = atk_pt
        self.def_pt = def_pt
        self.dodge_pt = dodge_pt
        self.potion = potion
    def wizardAttack(self, lp_dragon):
        print("Attaque du sorcier")
        return lp_dragon - self.atk_pt
    def wizardDefense(self , attack_dragon):
        if random.randint(1,6) > 4:
            print("Vous vous défender")
            return self.def_pt - attack_dragon
        else:
            print("Vous êtes touché !!")
            return attack_dragon

    def wizardDodge(self, attack_dragon):
        if random.randint(1, 6) > 4 and self.dodge_pt > 0:
            print("Vous esquiver")
            self.dodge_pt -= 100
        else:
            print("L'equive a échoué !!")
            return attack_dragon
    def takePotion(self):
        if self.potion > 0:
            print("------------>")
            print("Prendre une potion")
            print("------------>")
            self.life_pt += 500
            self.potion -= 1
        else:
            print("Vous n'avez plus de potion")
    def launchSpell(self):
        print("------------>")
        print("Lancer un sort")
        print("------------>")
        self.atk_pt += 1000
        self.mana_pt -= 100
    def showStat(self):
        print("             -------Wizard Stats-------")
        print("                  Life point " + str(self.life_pt))
        print("                  Mana point " + str(self.mana_pt))
        print("                  Attack point " + str(self.atk_pt))
        print("                  Defense point " + str(self.def_pt))
        print("                  Dodge point " + str(self.dodge_pt))
        print("             --------------------------")


