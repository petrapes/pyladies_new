def rodne_cislo():
    while True:
        try:
            rc = input('Zadej rodne cislo ')
            rc1 = int(rc[:6])
            rc2 = int(rc[7:])
            cislo = int(rc[:6] + rc[7:])
        except ValueError:
            print('To neni cislo!')
        else:
            if rc[6] != "/":
                print('Cislo ma byt zadano ve formatu 6x cislice, /, 4x cislice')
            elif cislo % 11 != 0:
                print('Cislo neni sprvne, asi ses nekde prepsal')
            else:
                break
    return "Zadane cislo je spravne", datum(rc), pohlavi(rc)

def datum(rc):
	den = int(rc[4:6])
	mesic = int(rc[2:4])
	rok = int("19" + rc[0:2])

	if mesic > 12:
		mesic = (mesic - 50)
	else:
		mesic

	if rok < 18:
		rok = "20" + rc[0:2]
	else:
		rok
	
	return "Datum narozeni je:", den, mesic, rok

def pohlavi(rc):
	mesic = int(rc[2:4])

	if mesic > 12:
		return "Pohlavi: zena"
	else:
		return "Pohlavi: muz"


print(rodne_cislo())