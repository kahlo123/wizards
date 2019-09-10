class Dragon:
    def __init__(self, life_pt, mana_pt, atk_pt,def_pt,dodge_pt):
        self.life_pt = life_pt
        self.mana_pt = mana_pt
        self.atk_pt = atk_pt
        self.def_pt = def_pt
        self.dodge_pt = dodge_pt
    def dragonAttak(self, lp_wizard):
        print("Attaque de dragon")
        return lp_wizard - self.atk_pt
    def showStat(self):
        print("-------Dragon Stats----------")
        print("Life point " + str(self.life_pt))
        print("Mana point " + str(self.mana_pt))
        print("Attack point " + str(self.atk_pt))
        print("Defense point " + str(self.def_pt))
        print("Dodge point " + str(self.dodge_pt))
        print("---------------------------")
