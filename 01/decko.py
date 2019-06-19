rc = input("Zadej rodne cislo:")
numbers = ["0","1","2","3","4","5","6","7","8","9"]

def kontrola(rc):
	rc2 = list(rc)
	if len(rc2) != 11:
		return "Format neni spravne"
	for _ in rc2[:6] and rc2[7:]:
		if _ in numbers:
			return "Format je spravne"
		else:
			return "Format neni spravne"
	if rc2[6] != "/":
		return "Format neni spravne"
	else:
		return "Format je spravne"

def delitelnost(rc):
	cast1 = rc[:6]
	cast2 = rc[7:]
	cislo = cast1 + cast2
	i = int(cislo)
	if i % 11 == 0:
		return "Cislo je delitelne 11"
	else:
		return "Cislo neni delitelne 11"

def datum(rc):
	den = rc[4:6]
	mesic = rc[2:4]
	rok = "19" + rc[0:2]

	den2 = int(den)
	mesic2 = int(mesic)
	rok2 = int(rok)

	if mesic2 > 12:
		mesic2 = (mesic2 - 50)
	else:
		mesic2

	if rok2 < 18:
		rok2 = "20" + rc[0:2]
	else:
		rok2
	
	return(print("Datum narozeni je:", den2, mesic2, rok2))

def pohlavi(rc):
	mesic = rc[2:4]
	mesic2 = int(mesic)

	if mesic2 > 12:
		return "Pohlavi: zena"
	else:
		return "Pohlavi: muz"

print(kontrola(rc))
print(delitelnost(rc))
print(datum(rc))
print(pohlavi(rc))

