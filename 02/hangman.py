hangman = [
        """
        -----------------
        """
        ,
        """ 
        +
        |
        |
        |
        |
        |
        ~~~~~~~
        ------------------
        """
        ,
        """
        +---.
        |
        |
        |
        |
        |
        ~~~~~~~
        ------------------
        """
        ,
        """
        +---.
        |   |
        |
        |
        |
        |
        ~~~~~~~
        ------------------
        """
        ,
        """
        +---.
        |   |
        |   O
        |
        |
        |
        ~~~~~~~
        ------------------
        """
        ,
        """
        +---.
        |   |
        |   O
        |   |
        |
        |
        ~~~~~~~
        ------------------
        """
        ,
        """
        +---.
        |   |
        |   O
        | --|
        |
        |
        ~~~~~~~
        ------------------
        """
        ,
        """
        +---.
        |   |
        |   O
        | --|--
        |
        |
        ~~~~~~~
        ------------------
        """
        ,
        """
        +---.
        |   |
        |   O
        | --|--
        |  /
        |
        ~~~~~~~
        ------------------
        """
        ,
        """
        +---.
        |   |
        |   O
        | --|--
        |  / \
        |
        ~~~~~~~
        ------------------"""]

import random
slova = ["projekt", "kvetina", "buchta"]

def vyber_nahodne_slovo(slova):
    # Vybira nahodne slovo
    tajne_slovo = random.choice(slova)
    return tajne_slovo

def start(hangman, spatna_pismena, spravna_pismena, tajne_slovo):
    print(hangman[len(spatna_pismena)])
    print()

    print("Spatna pismena:",end=" ")
    for pismeno in spatna_pismena:
        print(pismeno, end=" ")
    print()

    blanks = "_" * len(tajne_slovo)
    for i in range(len(tajne_slovo)):
        if tajne_slovo[i] in spravna_pismena:
            blanks = blanks[:i] + tajne_slovo[i] + blanks[i+1:]
    for pismeno in blanks:
        print(pismeno, end=" ")
    print()

def hadej(uhodnute):
    while True:
        print("Hadej pismeno: ")
        tip = input().lower()
        if len(tip) != 1:
            print("Zadavej jen jedno pismeno.")
        elif tip in spravna_pismena:
            print("Toto pismeno jsi uz hadal.")
        elif tip in spatna_pismena:
            print("Toto pismeno jsi uz hadal.")
        elif tip not in "abcdefghijklmnopqrstuvwxyz":
            print("Myslis si, ze nepoznam pismena")
        else:
            return tip

def hrajes_znova():
    print("Chces hrat znovu? ano/ne")
    return input().lower().startswith("a")

spatna_pismena = ""
spravna_pismena = ""
tajne_slovo = vyber_nahodne_slovo(slova)
konec_hry = False

while True:
    start(hangman, spatna_pismena, spravna_pismena, tajne_slovo)
    # zadani pismene
    tip = hadej (spravna_pismena + spatna_pismena)
    if tip in tajne_slovo:
        spravna_pismena = spravna_pismena + tip
        #vyhral?
        vsechna_pismena = True
        for i in range(len(tajne_slovo)):
            if tajne_slovo[i] not in spravna_pismena:
                vsechna_pismena = False
                break
        if vsechna_pismena:
            print("Ses nejlepsi, hadane slovo bylo:" + tajne_slovo)
            konec_hry = True
    else:
        spatna_pismena = spatna_pismena + tip
        if len(spatna_pismena) == len(hangman) - 1:
            start(hangman, spatna_pismena, spravna_pismena, tajne_slovo)
            print("Dosli ti pokusy, hadane cislo bylo:" + tajne_slovo)
            konec_hry = True
    if konec_hry:
        if hrajes_znova():
            spatna_pismena = ""
            spravna_pismena = ""
            konec_hry = False
            tajne_slovo = vyber_nahodne_slovo(slova)
        else:
            break