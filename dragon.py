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

