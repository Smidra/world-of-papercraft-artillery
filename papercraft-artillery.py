import math

# --- This is a hobby project, comments in czech ---

# --- Parametry země-houfnice dana ---
# Globální, no fuj!!
v0=16.828
g=9.81
xmax=51
xkrok=1
eps=1

# --- Krivky ---
# Odkomentuj kterou chceš vygenerovat
def povrch(x):
    # == Milesovka ==
    return (-0.014*(x-25)**2) +12
    
    # == Tsun-Li ==
    #if ( x<0 ):
    #    return 0
    #if( x > 51 ):
    #    return 0
    #return -1*(0.00006* ((x-46)**2) * ((x-4)**2) )+12
    
    # == Říp ==
    #return 2.5*math.cos(0.13*(x-25))+2.5

    # == Kolín ==
    #return 0

# --- Balistika ---
# u = uhel vystrelu
# a = posun houfnice vpravo po ose X
# b = posun houfnice nahoru po ose Y
# v = pocatecni rychlost
# g = gravitace
def balistika_y(x, u, a, b, v, g):
    ud = math.radians(u)
    y = (x-a)*math.tan(ud)-( (g* ((x-a)**2)) / ( 2*(v**2)*(math.cos(ud)**2) ) )+b
    return y

# --- Uhel dopadu ---
# odkud a jak strilime + na kterem X to dopadlo
def uhel_dopadu( u, a, b, v, g, x1):
    # dopocitej y1 v balistice_y(x1,..)
    # x2 = x1-eps  kde eps=1
    x2=x1-eps
    # dopocitej y1 a y2 v balistice_y(x2,..)
    y1 = balistika_y(x1, u, a, b, v, g)
    y2 = balistika_y(x2, u, a, b, v, g)
    # Spocti rozdil = y2-y1 [pozor, dopadnout muzu i zdola, zaporne uhly jsou v poradku]
    protilehla=y2-y1
    podstava=eps
    # tan(U_dopadu) = (rozdil) / (eps) => tedy tan-1[(rozdil)/(eps)] = U_dopadu
    uhel = math.degrees(math.atan((protilehla)/(podstava)))
    # return U_dopadu
    return uhel

# --- Nad povrchem ---
# spocita jak vysoko je strela nad povrchem
# ukazovatko - V jake souradnici x to resime
# u - uhel pod kterým jsme stříleli
# x - z jakého bodu jsme stříleli
# v - jakou rychlostí jsme stříleli
# g - gravitace
def nad_povrchem(ukazovatko, u, x, v, g):
    # Vypocitat yp povrchu
    yp = povrch(ukazovatko)
    # vypocitat yb balistiy
    yb = balistika_y(ukazovatko, u, x, povrch(x), v, g)
    # rozdil = yb - yp
    rozdil = yb - yp
    return rozdil

# --- Vypis navod na povrch ---
def povrch_navod():
    # Ctverecek
    for x in range(0,51,2):
        if(x%5 == 0):
            print(str(x)+";", end='')
        else:
            print(";", end='')
    
    print("")
    # Hodnota (vyska)
    for x in range(0,51,2):
        # hodnota krivky (y) pro kazdy ctverecek (x)
        hodnota=round(povrch(x), 1)
        print(str(hodnota)+";", end='')

# --- Vytiskni tabulku ---
# Popisek uhlu
print("~;↷;↶;", end='')
for u in range(0, 91, 2):
    print( str(u) + " °;" , end='')
print("↷;↶;")

# Pro kazdou pozici (x) na mape
for x in range(0, xmax, xkrok):
    # popisky vpravo
    print( str( round(povrch(x), 1) ) + ";" + str(x) + ";"+ str(50-x) + ";" , end='')
    
    # Pro kazdy uhel (u) od do 90
    for u in range(0, 91, 2):
        rozdil = 1
        ukazovatko = x
        # Pro kazdy dalsi ctverecek zjisti jak vysoko je strela nad zemi
        # Jakmile klesne pod zem tak konec
        while (rozdil >= 0):
            # Zjisti jak vysoko je nad povrchem
            rozdil = nad_povrchem(ukazovatko, u, x, v0, g)
            # ukazovatko ++
            ukazovatko += 1
        
        # Je blíže první pod nebo nejméně nad
        vyska_pred = nad_povrchem(ukazovatko-1, u, x, v0, g)
        vyska_po = nad_povrchem(ukazovatko, u, x, v0, g)
        # vyberu mensi
        dopad = ukazovatko
        if( vyska_pred <= abs(vyska_po) ):
            dopad = ukazovatko-1
        
        uhel = uhel_dopadu(u, x, povrch(x), v0, g, dopad)
        
        # -- Tisk --
        # strilime mimo plochu?
        if round(dopad,1) >= xmax:
            # prazdne policko
            print(";", end='')
        else:  
            # policko s dopadem
            print( str(round(dopad)) + " " + str(round(uhel)) + "°" + ";", end='')
    
    # popisky vlevo + newline
    print( str(x) + ";"+ str(50-x) )

# --- Vytiskni navod jak nakreslit level ---
#povrch_navod()
