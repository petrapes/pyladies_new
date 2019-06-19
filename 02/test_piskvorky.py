import piskvorky

def test_vyhodnot_x_wins():
    assert hra.vyhodnot("-------xxx----------") == "x"
    
def test_vyhodnot_o_wins():
    assert hra.vyhodnot("----------ooo-------") == "o"
    
def test_vyhodnot_remiza():
    assert hra.vyhodnot("xoxoxooxxooxxooxxoox") == "!"

def test_tah():
    assert hra.tah("---oxo---xooxxo-----", 0, "x") == "x--oxo---xooxxo-----"

def test_tah_pocitace():
    # test if it plays just on empty positions
    assert hra.tah_pocitace("ooxxooxxooxxooxxoox-") == "ooxxooxxooxxooxxooxx"