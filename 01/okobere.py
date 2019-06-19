from random import randrange
karta = randrange(2,11)
print("Pocet bodu", karta)
odpoved = input("Chcete pokracovat?")
while odpoved != "ne":
    from random import randrange
    dalsi = randrange(2,11)
    soucet = karta + dalsi
    print("Pocet bodu", soucet)
    if soucet > 21:
        print("prohravas")
        break
    elif soucet == 21:
        print("gratulujeme")
        break
    else:
        odpoved = input("Chcete pokracovat?")
    karta = soucet

print("game over")
