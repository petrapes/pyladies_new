key = int(input("Key:"))
plaintext = input("Vloz text k zasifrovani:")
ciphertext = ""
for znak in plaintext:
	i = ord(znak)
	i = i + key
	# jdeme pres "z"?
	if (i > ord("z")):
		i = i - 26
	znak = chr(i)
	ciphertext = ciphertext + znak
# vysledek
print("Zasifrovana zprava:", ciphertext)