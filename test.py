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
    def showStat(self):
        print("-------Stats----------")
        print("Life point " + str(self.life_pt))
        print("Mana point " + str(self.mana_pt))
        print("Attack point " + str(self.atk_pt))
        print("Defense point " + str(self.def_pt))
        print("Dodge point " + str(self.dodge_pt))
        print("---------------------------")

p1 = Wizard(10,10,1000,1000,2000)
p1.showStat()
p1.takePotion()
p1.showStat()
p1.launchSpell()
p1.showStat()