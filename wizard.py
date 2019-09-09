class Wizard:
    def __init__(self, life_pt, mana_pt, atk_pt,def_pt,dodge_pt):
        self.life_pt = life_pt
        self.mana_pt = mana_pt
        self.atk_pt = atk_pt
        self.def_pt = def_pt
        self.dodge_pt = dodge_pt

    def takePotion(self):
        print("------------>")
        print("Prendre une potion")
        print("------------>")
        self.life_pt+=1000

    def launchSpell(self):
        print("------------>")
        print("Lancer un sort")
        print("------------>")
        self.atk_pt += 1000
        self.mana_pt -= 1000
    def dodge(self):
        print("------------>")
        print("Esquive")
        print("------------>")
        self.dodge_pt -= 100
    def wizardAttack(self, lp_dragon):
        print("Attaque de dragon")
        return lp_dragon - self.atk_pt
    def showStat(self):
        print("-------Stats----------")
        print("Life point " + str(self.life_pt))
        print("Mana point " + str(self.mana_pt))
        print("Attack point " + str(self.atk_pt))
        print("Defense point " + str(self.def_pt))
        print("Dodge point " + str(self.dodge_pt))
        print("---------------------------")
