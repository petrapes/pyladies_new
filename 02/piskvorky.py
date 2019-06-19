def vyhodnot(pole):
    # vraci vyhodnoceni pole
    if "xxx" in pole:
        return "x"
    elif "ooo" in pole:
        return "o"
    elif "-" in pole:
        return "-"
    else:
        return "!"

def tah_hrace(pole):
    # zkontroluje, ze tah hrace dava smysl
    while True:
        pozice = int(input("Zadej cislo policka:"))
        if pozice < 0:
            print("zaporna policka nejsou")
        elif pozice > 19:
            print("to je moc")
        elif pole[pozice] != "-":
            print("tam uz to nejde")
        else:
            break
    return tah(pole, pozice, "o")

def tah_pocitace(pole):
    # definuje tah pocitace
    import random
    while True:
        policko = random.randint(0,19)
        if pole[policko] == "-":
            return tah(pole, policko, "x")

def tah (pole, cislo_policka, symbol):
    return (pole[:cislo_policka] + symbol + pole[cislo_policka+1:])

def piskvorky1d():
    pole = "--------------------"
    while True:
        print(pole)
        pole = tah_hrace(pole)
        print(tah_pocitace(pole))
        pole = tah_pocitace(pole)
        vyhodnot(pole)
        if vyhodnot(pole) != "-":
            break
    print(pole)
    print("Vyhrava", vyhodnot(pole))

piskvorky1d()