class Kocka:
    def __init__(self, jmeno, zivot):
        self.jmeno = jmeno
        self.zivot = zivot
    
    def zamnoukej(self):
        print("{}: Mnau!".format(self.jmeno))
    
    def je_ziva(self, zivot):
        if self.zivot < 9 and self.zivot > 0:
            print("Jsem ziva")
        else:
            print("Jsem mrtva")

    def uber_zivot(self):
        if self.zivot < 9 or self.zivot > 0:
            self.zivot -= 1
            print("Pocet zivotu:", self.zivot)
        else:
            pass
    
    def snez (self, jidlo):
        if jidlo == "ryba" and self.zivot < 9:
            self.zivot += 1
            print("Pocet zivotu:", self.zivot)
        else:
            print("Dik")
            print("Pocet zivotu:", self.zivot)

mourek = Kocka("Mourek", 9)
mourek.zamnoukej()
mourek.snez("ryba")

